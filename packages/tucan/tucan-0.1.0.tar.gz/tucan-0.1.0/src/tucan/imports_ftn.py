"""
Tucan module to get the imports of a fortran file
"""
from tucan.unformat_common import Statements


def imports_ftn(statements: Statements) -> dict:
    """
    Main function to search the imports in a fortran file.

    Args:
        statements (Statements): List of unformatted code statements along with line number ranges.

    Returns:
        dict: Dict with the module or function name associated with its various imports.
    """
    imports_dict = fortran_imports(statements)

    return imports_dict


def fortran_imports(stmts: Statements) -> dict:
    """
    Parse the fortran code given as a list of strings to get the module name if there is one
    as well as the various imports present in the file.

    Args:
        stmts (Statements): List of unformatted code statements along with line number ranges.

    Returns:
        fimports (dict): Dict with the module or function name associated with its various imports.

    """

    fimports = {}
    # Modules only
    for line in stmts.stmt:
        # strip used to avoid indentation mistakes

        if line.lower().strip().startswith("use "):
            module_from = line.strip().split()[1].split(",")[0]
            specific_use = []
            if "only" in line.lower():
                # remove dots, due to "only:" or "only :"
                use = line.split(":")[-1]
                specific_use = use.strip().split(",")
                specific_use = [func.strip() for func in specific_use]
            fimports[module_from] = {"specific": specific_use}

    # TODO: add detection of outside function and subroutine apart from modules (raw implicit imports)

    return fimports
