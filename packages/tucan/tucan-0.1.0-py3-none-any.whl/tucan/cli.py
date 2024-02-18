"""Module helper for the CLI of tucan"""
import click
from tucan import __version__ as _ver_
from tucan import __name__ as _name_


def add_version(f):
    """
    Add the version of the tool to the help heading.
    :param f: function to decorate
    :return: decorated function
    """
    doc = f.__doc__
    f.__doc__ = "Package " + _name_ + " v" + _ver_ + "\n\n" + doc
    return f


@click.group()
@add_version
def main():
    r"""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣼⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠴⢶⡶⣖⣒⠒⡺⣏⠙⡏⠉⠀⢀⣀⠀⠈⠙⠲⣄⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⣫⣤⠀⠀⡰⣿⡇⠀⠁⣽⡆⢷⡖⠛⢉⣭⣉⠳⣄⠀⠈⢧⡀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣟⠀⠈⠁⠀⠀⠀⠀⠀⠀⠘⣽⣟⠈⣷⡀⣿⣼⢿⠀⢹⠀⠀⠈⢧⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠙⠀⠀⠀⠀⠀⢠⢄⣤⣠⣰⣽⣿⡀⠘⡇⠙⠛⢋⣠⡾⠀⠀⠀⢸⡆⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠓⣸⢼⣟⣛⣛⣿⡿⠻⠛⠻⠏⠁⣉⡽⠋⠉⠉⢉⡞⠁⠀⠀⠀⠀⡇⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠟⠛⠉⠁⠀⠈⠉⠉⠛⠒⡶⠖⠋⠉⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⡇⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⠤⢤⣷⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⡤⠞⠉⠙⢦⠀⠀⠀⠀⠀⠀⣠⢰⠇⠀⠀⠀⠀⠀⢀⡏⢀⡼⠃⠀⠀⠀⠀⠀⢿⡀⠀
                ⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠁⣸⠀⠀⠀⠀⠀⠀⣼⠁⡾⠁⠀⠀⠀⠀⠀⠀⠘⡇⠀
                ⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢀⡏⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀
                ⠀⠀⡴⠲⠦⣤⣀⡀⢹⡄⠀⠀⠀⠀⠹⡄⠀⠀⠀⡟⢦⡀⠀⢀⣠⠞⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀
                ⠀⠈⠳⠤⣄⣀⠈⠉⠉⠁⠀⠀⠀⡤⠖⠛⡲⣄⠀⡇⠀⠈⠉⠉⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
                ⠀⠀⠀⣠⣤⣨⣽⡓⠲⢤⣄⡀⠀⠙⢻⠟⣵⣾⣧⣻⡀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡇⠀⠀⠀⠀⠀⠀⢸⡇
                ⠀⠀⡾⣡⣿⡟⣸⢿⣷⡄⠀⠙⣆⠀⠘⠛⠁⠈⢿⠻⣷⡀⠀⢰⡀⠀⠀⠀⠀⠈⣷⠀⢰⠀⢀⠀⠀⢸⠃
                ⠀⠸⠓⠛⠉⠀⠸⣮⣃⡷⠀⠀⠘⣦⠀⠀⠀⠀⠈⠧⣾⠻⣦⡈⢷⣄⠀⠀⠀⢀⣹⣆⣿⡀⢹⠀⠀⣸⠀
                ⠀⠐⠊⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠘⣧⠈⠙⣦⣟⢿⡖⠚⠋⠀⠉⠙⣧⣿⡆⢀⡏⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⢀⣸⣷⣴⠏⣠⡞⢹⡗⠒⠛⠀⠀⠀⠘⣧⣼⠁⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠰⣏⣡⠾⠋⠻⢯⡀⠀⡇⠀⠀⠀⠀⠀⠀⢹⡃⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⠀⢸⣇⡶⠟⠻⣼⠇⠀⡇⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀⢘⣧⡀⣟⠲⣤⣀⠀⠀⠀⠀⢷⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⣠⣶⣿⢿⡏⣿⢹⣄⠀⠉⠛⠲⠶⠶⢾⡆⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣋⣿⣷⣯⠿⠃⠀⠉⢷⣄⣄⠀⠀⠀⠈⡇⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠚⠲⣴⡇⠀

    -----------------------------   TUCAN   -----------------------------

    You are now using the Command line interface of Tucan package,
    a set of tools created at CERFACS (https://cerfacs.fr).
    It is a set of basic helpers around Fortran and Python language

    Checkout anubis and marauder's map packages, two Cerfacs tools
    able to explore respectively the history and geography of codes,
    which both are based upon Tucan.

    """
    pass


@main.command()
@click.argument("filename", type=str, nargs=1)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def clean(filename, dump):
    """
    Unformat a fortran of python single file.

    \b
    - Merge multiline statements to one line
    - Split ';' statements
    - Strip comments.
    - Strip blank lines.
    """
    from tucan.unformat_main import unformat_main

    statements = unformat_main(filename)

    base = filename.split("/")[-1].split(".")[0]
    print(statements)

    statements.dump_code("./" + base + "._rfmt")

    if dump:
        statements.dump_json("./" + base + ".json")


# @main.command()
# @click.argument("path", type=str, nargs=1)
# def package_clean(path):
#     """
#     Unformat a fortran and / or python folder.
#     """

#     import json
#     from loguru import logger

#     from tucan.package_analysis import (
#         rec_travel_through_package,
#         clean_extensions_in_paths,
#         run_unformat,
#     )

#     logger.info("Recursive path gathering ...")
#     paths = rec_travel_through_package(path)
#     logger.info("Cleaning the paths ...")
#     paths = clean_extensions_in_paths(paths)
#     logger.info("Running unformat ...")
#     statements = run_unformat(paths)

#     newfile = "statements_cleaned.json"
#     logger.info(f"Data dumped to {newfile}")
#     with open(newfile, "w") as fout:
#         json.dump(statements, fout, indent=2, sort_keys=True)


@main.command()
@click.argument("filename", type=str, nargs=1)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def struct(filename, dump):
    """
    Extract structure of a fortran or python single file.

    \b
    - Find the nested structures of a code
    - Find the callables in each structure
    - Evaluate sizes, CCN
    """
    import json
    from loguru import logger

    from tucan.struct_main import struct_main
    from tucan.struct_common import struct_summary_str

    struct_ = struct_main(filename)
    logger.info("Found following structure:\n" + struct_summary_str(struct_))
    base = filename.split("/")[-1].split(".")[0]
    if dump:
        newfile = base + ".json"
        logger.info(f"Data dumped to {newfile}")
        with open(newfile, "w") as fout:
            json.dump(struct_, fout, indent=2, sort_keys=True)


# @main.command()
# @click.argument("path", type=str, nargs=1)
# def package_struct(path):
#     """
#     Extract structure of a fortran and / or python folder.
#     """
#     from tucan.package_analysis import (
#         rec_travel_through_package,
#         clean_extensions_in_paths,
#         run_struct,
#     )
#     from loguru import logger
#     import json

#     logger.info("Recursive path gathering ...")
#     paths = rec_travel_through_package(path)
#     logger.info("Cleaning the paths ...")
#     paths = clean_extensions_in_paths(paths)
#     logger.info("Running struct ...")
#     full_struct = run_struct(paths)

#     newfile = "full_struct.json"
#     logger.info(f"Data dumped to {newfile}")
#     with open(newfile, "w") as fout:
#         json.dump(full_struct, fout, indent=2, sort_keys=True)


@main.command()
@click.argument("filename", type=str, nargs=1)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def imports(filename, dump):
    """
    Extract imports of a single file.
    """
    import json
    from loguru import logger

    from tucan.imports_main import imports_main
    from tucan.imports_common import imports_summary_str

    imports_ = imports_main(filename)
    logger.info("Found following structure:\n" + imports_summary_str(imports_))
    if dump:
        base = filename.split("/")[-1].split(".")[0]
        newfile = base + "_imports.json"
        logger.info(f"Data dumped to {newfile}")
        with open(newfile, "w") as fout:
            json.dump(imports_, fout, indent=2, sort_keys=True)



@main.command()
@click.argument("filename", type=str, nargs=1)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def ifdef_scan(filename, dump):
    """
    Extract Ifdef variables of a single file.
    """
    import json
    from loguru import logger
    from tucan.clean_ifdef import scan_ifdef_variables
   

    with open(filename,"r") as fin:
        lines = fin.read().split("\n")
        
    gv_, lv_ = scan_ifdef_variables(lines)
    gv_s = ", ".join(gv_)
    lv_s = ", ".join(lv_)
    
    logger.info(f"Global ifdef variables : {gv_s}")
    if lv_:
        logger.info(f"Found local ifdef variables : {lv_s}")
    else:
        logger.info("No local ifdef variables")

    if dump:
        base = filename.split("/")[-1].split(".")[0]
        newfile = base + "_ifdefs.json"
        logger.info(f"Data dumped to {newfile}")
        out={"global":gv_ , "local": lv_}
        with open(newfile, "w") as fout:
            json.dump(out, fout, indent=2, sort_keys=True)




@main.command()
@click.argument("filename", type=str, nargs=1)
@click.option(
    "-v",
    "--variables",
    type=str,
    default=None,
    # multiple=True,
    help="Variable to resolve ifdefs. Comma separated ',', no spaces : -v ARG1,ARG2",
)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def ifdef_clean(filename, variables,dump):
    """
    Show a file with idefs resolved
    """
    from loguru import logger
    from tucan.clean_ifdef import remove_ifdef_from_module
    logger.critical(variables)
    
    if variables is None:
        variables=[]
    else:
        variables=variables.split(",")

    logger.critical(variables)
    with open(filename,"r") as fin:
        lines = fin.read().split("\n")
     
    lines = remove_ifdef_from_module(lines,variables)
    
    logger.success("Ifdefs resolved:")
    for line in lines:
        print(line)
    if dump:
        newfile=filename+"_ifdef_resolved"
        lines.append("# the ifdefs were resolved by tucan")
        v_s = ", ".join(variables)
        lines.append(f"# IFdef Variables: {variables}")
        with open(newfile, "w") as fout:
            fout.writelines(lines)

@main.command()
@click.argument("path", type=str, nargs=1)
@click.option(
    "-d",
    "--dump",
    is_flag=True,
    help="dump json data",
)
def ifdef_scan_pkge(path, dump):
    """
    Extract Ifdef variables of a single file.
    """
    import json,os
    from loguru import logger
    from tucan.clean_ifdef import run_ifdef_pkg_analysis
    from tucan.package_analysis import (
        rec_travel_through_package,
        get_package_files,
    )
    
    logger.info("Recursive path gathering ...")
    paths = rec_travel_through_package(path)
    logger.info("Cleaning the paths ...")
    files = get_package_files(paths,os.getcwd())


    out = run_ifdef_pkg_analysis(files)
    gv_s = ", ".join(out["global"])
    logger.info(f"Global ifdef variables : {gv_s}")
    for file,lv_ in out["local"].items():
        if lv_:
            lv_s = ", ".join(lv_)
            logger.info(f"Local to {file} : {lv_s}")
    
    if dump:
        newfile = path + "package_ifdefs.json"
        logger.info(f"Data dumped to {newfile}")
        with open(newfile, "w") as fout:
            json.dump(out, fout, indent=2, sort_keys=True)

# @main.command()
# @click.argument("path", type=str, nargs=1)
# def package_imports(path):
#     """
#     Extract imports of a fortran and / or python folder.
#     """
#     from tucan.package_analysis import (
#         rec_travel_through_package,
#         clean_extensions_in_paths,
#         run_imports,
#     )
#     from loguru import logger
#     import json

#     logger.info("Recursive path gathering ...")
#     paths = rec_travel_through_package(path)
#     logger.info("Cleaning the paths ...")
#     paths = clean_extensions_in_paths(paths)
#     logger.info("Running struct ...")
#     full_imports = run_imports(paths)
#     newfile = "package_imports.json"
#     logger.info(f"Data dumped to {newfile}")
#     with open(newfile, "w") as fout:
#         json.dump(full_imports, fout, indent=2, sort_keys=True)


@main.command()
@click.argument("path", type=str, nargs=1)
def package_analysis(path):
    """
    Extract struct and the imports of a fortran and / or python folder. (For now)
    """
    from tucan.package_analysis import (
        rec_travel_through_package,
        get_package_files,
        run_full_analysis,
    )
    from loguru import logger
    import json, os

    logger.info("Recursive path gathering ...")
    paths = rec_travel_through_package(path)
    logger.info("Get files ...")
    files = get_package_files(paths, os.getcwd())
    logger.info("Running struct ...")
    full_analysis = run_full_analysis(files)

    newfile = "package_analysis.json"
    logger.info(f"Data dumped to {newfile}")
    with open(newfile, "w") as fout:
        json.dump(full_analysis, fout, indent=2, sort_keys=True)
