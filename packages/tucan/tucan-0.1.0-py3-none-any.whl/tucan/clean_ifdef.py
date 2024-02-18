from typing import List
from loguru import logger


def scan_ifdef_variables(lines: List[str]) -> list:
    """Detect ifdef variables

    cancels inner variables"""
    out = []
    inner_defined = []
    for line in lines:
        if (
            line.startswith("#ifdef")
            or line.startswith("#elif")
            or line.startswith("#if ")
        ):
            rhs = line.split()[1]

            rhs = rhs.replace("defined(", "")
            rhs = rhs.replace(")", "")

            rhs = rhs.replace("||", " ")
            rhs = rhs.replace("&&", " ")

            out.extend(rhs.split())
        if line.startswith("#define"):
            definition = line.split()
            inner_defined.append(definition[1])

        inner_def = sorted(set(inner_defined))
        global_def= sorted(set(out))
        global_def = [item for item in global_def if item not in inner_defined]
        
    return global_def,inner_def


def remove_ifdef_from_module(lines: List[str], definitions: List[str]) -> List[str]:
    """Cleaned version of a code"""

    def _evaluate_context(context: list) -> bool:
        """Interpret the cntext to see if next lines will be included or not"""
        final_context = [bools_[-1] for bools_ in context]
        if eval(" and ".join(final_context)):
            included = True
        else:
            included = False
        return included

    out = []
    context = []
    for line in lines:
        if not context:
            included = True
        if line.startswith(("#ifdef", "#elif", "#if ")):
            rhs = line.split()[1]

            # clean right hand side
            rhs = rhs.replace("defined(", "")
            rhs = rhs.replace(")", "")
            rhs = rhs.replace("||", " || ")
            rhs = rhs.replace("&&", " && ")

            # assemble expression as string
            expr = ""
            for item in rhs.split():
                if item in definitions:
                    expr += "True "
                elif item == "||":
                    expr += "or "
                elif item == "&&":
                    expr += "and "
                else:
                    expr += "False "

            # increment context
            if line.startswith("#if"):
                context.append([str(eval(expr))])  # append to the main list
            if line.startswith("#elif"):
                context[-1].append(
                    str(eval(expr))
                )  # append to the sublist of the last element

            included = _evaluate_context(context)

            logger.warning(line)
            print("Line     :", line)
            print("Context  :", context)
            print("Included :", included)

        elif line.startswith("#else"):
            #  if  elif  else
            #  True False False
            #  False True False
            #  False False True
            # all of the previous if/eli in the context must be false for else to be true

            status = "True"
            for bool_ in context[-1]:
                if bool_ == "True":  # if any of previous is true, status is False.
                    status = "False"
            context[-1].append(status)

            included = _evaluate_context(context)

            logger.warning(line)
            print("Line     :", line)
            print("Context  :", context)
            print("Included :", included)

        elif line.startswith("#endif"):
            context.pop(-1)
            if not context:
                included = True
            logger.critical(line)
            print("Line     :", line)
            print("Context  :", context)
            print("Included :", included)

        elif line.startswith("#define"):
            if included:
                definitions.append(line.split()[1])
        elif line.startswith("#"):
            logger.critical("Pragma not recognised:", line)
        else:
            if included:
                out.append(line)
                logger.success(line)
            else:
                logger.error(line)
                out.append("")

    return out


def run_ifdef_pkg_analysis(files: dict) -> dict:
    """
    Gather the data associated to the functions and the imports within a file

    Args:
        files (dict): key: short_name , value: absolute paths

    Returns:
        dict: _description_
    """

    ifdef_analysis = {
        "global": [],
        "local": {},

    }
    
    gvars = []
    for file ,path_ in files.items():
        with open(path_,"r") as fin:
            lines = fin.read().split("\n")
        
        gv_, lv_ = scan_ifdef_variables(lines)
        
        gvars.extend(gv_)
        ifdef_analysis["local"][file]=lv_

    ifdef_analysis["global"]=sorted(set(gvars))
    logger.success("Analysis completed.")
    return ifdef_analysis

# with open("templates_ifdef.f","r") as fin:
#     lines = fin.read().split("\n")

# vars = scan_ifdef_variables(lines)
# print("Found "+ ", ".join(vars))

# out =remove_ifdef_from_module(lines,["OUIPI1","MOREARG","LVL1"])

# print("\n".join(out))
