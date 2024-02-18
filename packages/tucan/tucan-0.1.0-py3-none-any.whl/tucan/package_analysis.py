"""Module that aims to analyze a whole package based 
on the other unitary function of the package"""

from pathlib import Path
from loguru import logger
from tucan.unformat_main import unformat_main
from tucan.struct_main import struct_main
from tucan.imports_main import imports_main


def rec_travel_through_package(path: str,  optional_paths: list = None,) -> list:
    """
    List all paths from a folder and its subfolders recursively.

    RECURSIVE
    """
    if not optional_paths:
        optional_paths = []

    current_paths_list = [path, *optional_paths]

    # Move to absolute Path objects
    current_paths_list =[ Path(p_) for p_ in current_paths_list]

    paths_ = []
    for current_path in current_paths_list:
        for element in current_path.iterdir():
            if element.is_dir():
                path_str = element.as_posix()
                paths_.extend(rec_travel_through_package(path_str))
            else:
                if element.as_posix() not in paths_:
                    if not element.as_posix().split("/")[-1].startswith("."):
                        paths_.append(element.as_posix())
    return paths_


def clean_extensions_in_paths(paths_list: list) -> list:
    """
    Remove unwanted path extensions and duplicates.

    Args:
        paths_list (list): List of all paths gatheres through recursive analysis

    Returns:
        list: List of cleaned paths.
    """
    clean_paths = []
    for path in paths_list:
        if path.endswith((".py", ".f90", ".f", ".F", ".f77", ".c")):
            clean_paths.append(path)

    return [
        *set(clean_paths),
    ]


def get_package_files(clean_paths: list, relpath: str) -> dict:
    """
    Return all the files useful for a package analysis, with their absolut paths
    """

    files = []
    for path_ in clean_paths:
        if not Path(path_).is_dir():
#            logger.info(f"Append :{path_}")
            files.append(path_)

    files = clean_extensions_in_paths(files)
    
    if not files:
        logger.warning(f"No files found in the paths provided")

    files = [Path(relpath)/Path(p_) for p_ in files]
    
    out = {}
    for file in files:
        path_ = file.relative_to(Path(relpath)).as_posix()
        out[path_]=file.as_posix()
    return out


def run_full_analysis(files: dict) -> dict:
    """
    Gather the data associated to the functions and the imports within a file

    Args:
        files (dict): key: short_name , value: absolute paths

    Returns:
        dict: _description_
    """

    full_analysis = {}
    
    for file ,path_ in files.items():
        full_analysis[file] = {"imports": imports_main(path_)}
        full_analysis[file].update(struct_main(path_))
    logger.success("Analyze completed.")
    return full_analysis


def run_unformat(clean_paths: list) -> dict:
    """
    Gather the unformated version of code files within a dict.

    Args:
        clean_paths (list): List of cleaned paths.

    Returns:
        dict: File path as key, item as a list of lines with their line number span
    """
    statements = {}
    for file in clean_paths:
        statements[file] = unformat_main(file).to_nob()

        nbr_of_stmt = 0
        if statements[file]:
            nbr_of_stmt = len(statements[file])
        logger.info(f"Found {nbr_of_stmt} statements for {file}")

    return statements


def run_struct(clean_paths: list) -> dict:
    """
    Gather the data associated to the functions within a file.

    Args:
        clean_paths (list): List of cleaned paths.

    Returns:
        dict: File path as key, item as dict with function names and their data (NLOC, CCN, etc.)
    """
    full_struct = {}
    files = []

    for path_ in clean_paths:
        if not Path(path_).is_dir():
            files.append(path_)

    files = clean_extensions_in_paths(files)
    for file in files:
        full_struct[file] = struct_main(file)
        total_stmts = 0
        for _, data in full_struct[file].items():
            total_stmts += data["ssize"]
        logger.info(f"Found {total_stmts} statements for {file}")

    return full_struct


def run_imports(clean_paths: list) -> dict:
    """
    Gather the imports within a file.

    Args:
        clean_paths (list): List of cleaned paths.

    Returns:
        dict: File path as key, dict of function with their imports as item.
    """
    full_imports = {}
    files = []

    for path_ in clean_paths:
        if not Path(path_).is_dir():
            files.append(path_)

    files = clean_extensions_in_paths(files)
    for file in files:
        full_imports[file] = imports_main(file)
    logger.success("Imports found.")
    return full_imports

