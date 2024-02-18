"""
Tucan module to get the imports of a python file
"""
from tucan.unformat_common import Statements


def imports_py(statements: Statements) -> dict:
    """
    Main function to search the imports in a python file.

    Args:
        statements (Statements): List of unformatted code statements along with line number ranges.

    Returns:
        dict: Dict with the module or function name associated with its various imports.
    """
    imports_dict = python_imports(statements)

    return imports_dict


def python_imports(stmts: Statements) -> dict:
    """
    Parse the python code to check for the imports and update the imports database.

    Args:
        stmts (Statements): List of unformatted code statements along with line number ranges.

    Returns:
        imports_dict (dict): Dict with the module or function name associated with its various imports.
    """
    imports_dict = {}
    for line in stmts.stmt:
        if "import " not in line:
            pass

        # Parsing "as" imports (ex: numpy as np) for later identification
        if line.strip().startswith("import "):
            module_from = line.split("import ")[-1].strip()
            if " as " in line:
                alias = line.split(" as ")[-1].strip()
                module_from = module_from.split(" as ")[0].strip()
                imports_dict[module_from] = {"alias": alias, "explicit": []}
            else:
                module_from = module_from.split(",")
                for mod_from in module_from:
                    imports_dict[mod_from.strip()] = {"explicit": []}

        # Parsing "from XXX import XXX", i.e. specific imports
        if line.strip().startswith("from ") and "import" in line.strip():
            module_from = line.split("import ")[0].split("from ")[-1].strip()
            func_imported = line.split("import ")[1:]
            # Handle the case from XXXX import XXXX as XXXX
            if "as " in func_imported[0]:
                mod_and_alias = func_imported[0].split("as ")
                func_imported = {
                    "alias": mod_and_alias[1].strip(),
                    "explicit": [mod_and_alias[0].strip()],
                }  # Name of function is saved not the alias yet

            # Handle imports on multiple lines
            elif func_imported[0].startswith("("):
                func_imported = func_imported[0].split("(")[-1]
                func_imported = func_imported.split(")")[0]
                func_imported = {
                    "explicit": [func_.strip() for func_ in func_imported.split(",")]
                }

            else:
                func_imported = func_imported[0].split(",")
                func_imported = {"explicit": [func_.strip() for func_ in func_imported]}

            imports_dict[module_from] = func_imported

    return imports_dict
