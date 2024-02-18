"""
Tucan module to handle the import parsing of all files.
"""
from loguru import logger

from tucan.unformat_py import unformat_py
from tucan.unformat_ftn import unformat_ftn
from tucan.imports_py import imports_py
from tucan.imports_ftn import imports_ftn


def imports_main(filename: str) -> dict:
    """
    Extract the imports of a code file.

    Args:
        filename (str): Name of the file (with its path) to parse.

    Returns:
        dict: Imports functions stored by filename as key.
    """
    logger.info(f"Analyzing the imports for {filename}")
    try:
        with open(filename, "r") as fin:
            code = fin.read().splitlines()
    except UnicodeDecodeError:
        return {}

    code = [line.lower() for line in code]  # Lower case for all

    imports_ = {}
    if filename.lower().endswith(".py"):
        logger.debug(f"Python code detected ...")
        statements = unformat_py(code)
        imports_ = imports_py(statements)
    elif filename.lower().endswith((".f", ".F", ".f77", ".f90")):
        logger.debug(f"Fortran code detected ...")
        statements = unformat_ftn(code)
        imports_ = imports_ftn(statements)
    else:
        ext = filename.lower().split(".")[-1]
        logger.error(f"Extension {ext} not supported, exiting ...")
        return {}
    return imports_
