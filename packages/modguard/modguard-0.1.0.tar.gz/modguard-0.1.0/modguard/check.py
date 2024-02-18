import ast
import os
from dataclasses import dataclass

from .boundary import BoundaryTrie
from .errors import ModguardParseError


@dataclass
class ErrorInfo:
    location: str
    error: str


def file_to_module_path(file_path: str):
    # Replace os-specific path separators with '.'
    module_path = file_path.replace(os.sep, ".")

    # Strip the extension and handle '__init__.py' files
    if module_path.endswith(".py"):
        module_path = module_path[:-3]  # Remove '.py' extension
    if module_path.endswith(".__init__"):
        module_path = module_path[:-9]  # Remove '.__init__' for package directories
    if module_path == "__init__":
        return "."

    return module_path


class BoundaryFinder(ast.NodeVisitor):
    def __init__(self):
        self.is_modguard_boundary_imported = False
        self.found_boundary = False

    def visit_ImportFrom(self, node):
        # Check if 'Boundary' is imported specifically from 'modguard'
        if node.module == "modguard" and any(
            alias.name == "Boundary" for alias in node.names
        ):
            self.is_modguard_boundary_imported = True
        self.generic_visit(node)

    def visit_Import(self, node):
        # Check if 'modguard' is imported, and if so, we will need additional checks when 'Boundary' is called
        for alias in node.names:
            if alias.name == "modguard":
                self.is_modguard_boundary_imported = True
        self.generic_visit(node)

    def visit_Call(self, node):
        if self.is_modguard_boundary_imported:
            if isinstance(node.func, ast.Attribute) and node.func.attr == "Boundary":
                if (
                    isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "modguard"
                ):
                    self.found_boundary = True
            elif isinstance(node.func, ast.Name) and node.func.id == "Boundary":
                # This handles the case where 'Boundary' is imported directly: from modguard import Boundary
                # We are currently ignoring the case where this is still the wrong Boundary (if it has been re-assigned)
                self.found_boundary = True
        self.generic_visit(node)


def has_boundary(file_path: str) -> bool:
    with open(file_path, "r") as file:
        file_content = file.read()

    try:
        parsed_ast = ast.parse(file_content)
        boundary_finder = BoundaryFinder()
        boundary_finder.visit(parsed_ast)
        return boundary_finder.found_boundary
    except SyntaxError as e:
        raise ModguardParseError(f"Syntax error in {file_path}: {e}")


class ImportVisitor(ast.NodeVisitor):
    def __init__(self, current_mod_path: str, is_package: bool = False):
        self.current_mod_path = current_mod_path
        self.is_package = is_package
        self.imports = []

    def visit_ImportFrom(self, node):
        # For relative imports (level > 0), adjust the base module path
        if node.level > 0:
            num_paths_to_strip = node.level - 1 if self.is_package else node.level
            base_path_parts = self.current_mod_path.split(".")
            if num_paths_to_strip:
                base_path_parts = base_path_parts[:-num_paths_to_strip]
            base_mod_path = ".".join([*base_path_parts, node.module])
        else:
            base_mod_path = node.module

        for name_node in node.names:
            self.imports.append(f"{base_mod_path}.{name_node.asname or name_node.name}")

        # Continue traversing the tree
        self.generic_visit(node)


def get_imports(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_content = file.read()

    try:
        parsed_ast = ast.parse(file_content)
        mod_path = file_to_module_path(file_path)
        import_visitor = ImportVisitor(
            is_package=file_path.endswith("__init__.py"), current_mod_path=mod_path
        )
        import_visitor.visit(parsed_ast)
        return import_visitor.imports
    except SyntaxError as e:
        raise ModguardParseError(f"Syntax error in {file_path}: {e}")


def check(root: str) -> list[ErrorInfo]:
    if not os.path.isdir(root):
        return [ErrorInfo(location="", error=f"The path {root} is not a directory.")]

    boundary_trie = BoundaryTrie()
    boundary_trie.insert(root)
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                if has_boundary(file_path):
                    mod_path = file_to_module_path(file_path)
                    boundary_trie.insert(mod_path)

    errors = []
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                current_mod_path = file_to_module_path(file_path)
                current_nearest_boundary = boundary_trie.find_nearest(current_mod_path)
                assert (
                    current_nearest_boundary is not None
                ), "Checking file outside of boundaries!"
                import_mod_paths = get_imports(file_path)
                for mod_path in import_mod_paths:
                    nearest_boundary = boundary_trie.find_nearest(mod_path)
                    if (
                        nearest_boundary is not None
                        and not current_nearest_boundary.startswith(nearest_boundary)
                    ):
                        errors.append(
                            ErrorInfo(
                                location=file_path,
                                error=f"Import {mod_path} in {file_path} is blocked by boundary {nearest_boundary}",
                            )
                        )

    return errors
