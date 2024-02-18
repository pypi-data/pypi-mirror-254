"""Global function to handle the unformat of various languages"""
from loguru import logger

from tucan.unformat_py import unformat_py
from tucan.unformat_ftn import unformat_ftn
from tucan.unformat_c import unformat_c


def unformat_main(filename: str) -> list:
    """
    Main function to call to get an unformated version of the code

    Args:
        filename (str): _description_

    Returns:
        list: _description_
    """
    with open(filename, "r") as fin:
        code = fin.read().splitlines()

    code = [line.lower() for line in code]  # Lower case for all

    if filename.lower().endswith(".py"):
        logger.debug(f"Python code detected ...")
        statements = unformat_py(code)
    elif filename.lower().endswith((".f", ".F", ".f77", ".f90")):
        logger.debug(f"Fortran code detected ...")
        statements = unformat_ftn(code)
    elif filename.lower().endswith((".c", ".cpp", ".cc")):
        logger.debug(f"C/C++ code detected ...")
        statements = unformat_c(code)
    else:
        ext = filename.lower().split(".")[-1]
        logger.error(f"Extension {ext} not supported, exiting ...")
        statements = []

    return statements
