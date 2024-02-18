"""Global function to handle the struct analysis of various languages"""
from loguru import logger

from tucan.unformat_py import unformat_py
from tucan.unformat_ftn import unformat_ftn
from tucan.unformat_c import unformat_c
from tucan.struct_py import extract_struct_py
from tucan.struct_ftn import extract_struct_ftn
from tucan.struct_c import extract_struct_c


def struct_main(filename: str) -> dict:
    """
    Extract structure of a fortran or python file.
    - Find the nested structures of a code
    - Find the callables in each structure
    - Evaluate sizes, CCN

    Args:
        filename (str): Name of the file (with its path) to parse.

    Returns:
        dict: Structure analyzed, with complexity, size, name, path, lines span, etc.

    """
    logger.info(f"Struct analysis on {filename}")
    try:
        with open(filename, "r") as fin:
            code = fin.read().splitlines()
    except UnicodeDecodeError:
        return {}

    code = [line.lower() for line in code]  # Lower case for all

    if filename.lower().endswith(".py"):
        logger.debug(f"Python code detected ...")
        statements = unformat_py(code)
        struct_ = extract_struct_py(statements)
    elif filename.lower().endswith((".f", ".F", ".f77", ".f90")):
        logger.debug(f"Fortran code detected ...")
        statements = unformat_ftn(code)
        struct_ = extract_struct_ftn(statements)
    elif filename.lower().endswith((".c", ".cpp", ".cc")):
        logger.debug(f"C/C++ code detected ...")
        statements = unformat_c(code)
        struct_ = extract_struct_c(statements)
    else:
        ext = filename.lower().split(".")[-1]
        logger.error(f"Extension {ext} not supported, exiting ...")
        return {}

    return struct_


def create_empty_struct(filename: str) -> dict:
    """
    Function to create an empty structure output.

    Args:
        filename (str): Name of the file (with its path) to parse.

    Returns:
        dict: Empty structure dict i.e. with defaults values.
    """
    struct_ = {
        filename: {
            "CCN": 1,
            "NLOC": 1,
            "callables": [],
            "contains": [],
            "lines": [0, 0],
            "linestart": None,
            "name": filename,
            "path": [filename],
            "ssize": 0,
            "statements": [],
            "type": None,
        }
    }
    return struct_
