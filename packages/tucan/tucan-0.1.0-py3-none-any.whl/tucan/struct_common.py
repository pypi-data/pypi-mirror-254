"""
Module that gather the most common functions of struct.
"""

import re
from typing import Tuple, List,Callable
from copy import deepcopy
from loguru import logger

def path_clean(path: list, paths_to_clean: Tuple[list]):
    """Remove the unwanted steps of the paths"""
    indexes_to_clean = []
    for ptc in paths_to_clean:
        if list2pathref(path).startswith(list2pathref(ptc)):
            indexes_to_clean.append(len(ptc) - 1)
    new_path = []
    for i, step in enumerate(path):
        if i not in indexes_to_clean:
            new_path.append(step)
    return new_path


def list2pathref(path: list) -> str:
    """The way we will refer to path here in strings"""
    return ".".join(path)


def pathref_ascendants(pathstr: str) -> List[str]:
    """Return all ascendends of a path"""
    out = []
    path = pathstr.split(".")
    while len(path) > 1:
        path.pop(-1)
        out.append(list2pathref(path))
    return out


def struct_summary_str(main_structs: dict) -> str:
    out = []
    for part, data in main_structs.items():
        out.append(f'\n{data["type"]} {part} :')
        out.append(
            f'    At path {data["path"]}, name {data["name"]}, lines {data["lines"][0]} -> {data["lines"][-1]}'
        )
        out.append(f'    {data["ssize"]} statements over {data["NLOC"]} lines')
        out.append(f'    Complexity {data["CCN"]}')
        if data["callables"]:
            list_str = "\n       - " + "\n       - ".join(data["callables"])

            out.append(f'    Refers to {len(data["callables"])} callables:{list_str}')
        else:
            out.append(f"    Contains no callables")
        if data["contains"]:
            list_str = "\n    - " + "\n    - ".join(data["contains"])
            out.append(f'    Contains {len(data["contains"])} elements:{list_str}')
        else:
            out.append(f"    Contains no inner structures")
        
        if data["annotations"]:
            keyvals=[ keys+":"+values for key,values in data["annotations"].items()]
            list_str = "\n       - " + "\n       - ".join(keyvals)

            out.append(f'    Refers to {len(keyvals)} callables:{list_str}')
        else:
            out.append(f"    Contains no annotations")
        

    return "\n".join(out)


def find_words_before_left_parenthesis(line: str) -> List[str]:
    """Find all words before a left parenthesis in a line"""

    # Adding a threshold to avoid long running time (most likely for big arithmetic lines)
    # Act like a pre-check
    if line.count("(") > 50 or line.count("(") == 0:
        line = ""

    # Define a regular expression pattern to find words before a left parenthesis
    pattern = r"(.*?\S)\("
    # Use re.findall to find all matches in the code
    matches = re.findall(pattern, line)
    clean_matches = []

    tokens = ",+-/*<>=;|(){}[]:~ "
    for match_ in matches:
        token=""
        for i in range(len(match_),0,-1):
            if match_[i-1] in tokens:
                break
            token=match_[i-1]+token
        
        if token != "":
            clean_matches.append(token)
    return clean_matches


########################################################
# BUFFER of detection


def buffer_item(
    type_: str,
    name: str,
    first_line: str,
    line_idx: int,
    statement_idx: int,
) -> Tuple[str, str, str, int, int]:
    """Forces buffers to keep the same logic across languages"""
    return (
        type_,
        name,
        first_line,
        line_idx,
        statement_idx,
    )


########################################################
# STACK of detection


def stack_item(
    type_: str,
    name: str,
    path: list,
    start_line_idx: int,
    start_statement_idx: int,
    start_line: str,
    end_line_idx: int,
    end_statement_idx: int,
    end_line: str,
) -> Tuple[str, str, list, int, int, str, int, int, str]:
    """Forces stacks to keep the same logic across languages"""

    try:
        if path[-1] != name:  # last item of path should be name
            logger.warning(f"Path {str(path)} does not end with {name}")
    except IndexError:
        raise RuntimeError(f"Structure -{name}- has no path")

    return (
        type_,
        name,
        path,
        start_line_idx,
        start_statement_idx,
        start_line,
        end_line_idx,
        end_statement_idx,
        end_line,
    )


def struct_from_stack(stack: list, main_types: list, skip_types: list = None) -> dict:
    """Build a dictionary of all structures"""
    # Build nested structure
    struct = {}
    if skip_types is None:
        skip_types = []

    path_to_skip = []
    for type_, name, path, *_ in stack:
        if type_ in skip_types:
            path_to_skip.append(path)

    for (
        type_,
        name,
        path,
        start_line_idx,
        start_statement_idx,
        start_line,
        end_line_idx,
        end_statement_idx,
        end_line,
    ) in stack:
        # logger.warning(path)
        # logger.warning(path_to_skip)
        cleaned_path = path_clean(path, path_to_skip)
        # logger.warning(cleaned_path)
        if type_ in main_types:
            struct[list2pathref(cleaned_path)] = {
                "path": cleaned_path,
                "name": name,
                "type": type_,
                "linestart": start_line,
                "lines": [start_line_idx, end_line_idx],
                "statements": [start_statement_idx, end_statement_idx], #Warning: here statements starts at 1!!!
                "contains": [],
                "annotations":{},
            }

    return struct


def get_struct_sizes(struct: dict) -> dict:
    """Compute the size of strict items (statefull)"""
    struct_aspects = {}
    for part, data in struct.items():
        struct_aspects[part] = {}
        struct_aspects[part]["NLOC"] = data["lines"][-1] - data["lines"][0] + 1
        struct_aspects[part]["ssize"] = data["statements"][-1] - data["statements"][0]
        struct_aspects[part]["callables"] = []
        struct_aspects[part]["CCN"] = []
    return struct_aspects



def replace_self(list_:list, parent:str)->list:
    """Replace the self keyword in a parentality path"""
    return  [
        item.replace("self.", parent+".")
        for item in list_
    ]    


def _strip_safe_lines(beg:int, end:int, safes: List[list])->List:
    """Return an iterable stripped from safe zones
    beg=100
    end = 110
    safes = [[103,104],[106,109]]

    100
    101
    102
    105
    
    """
    iter_=[]
    for i in range(beg,end+1):
        blocked=False
        for safe in safes:
            if i>=safe[0] and i<=safe[1]:    
                #print(f"{i} blocked")
                blocked=True
        if not blocked:
            iter_.append(i)
    return iter_


def struct_actual_lines(struct_in:dict, name:str)->list:
    """returns an iterable with only the statement relative to this part
    excluding contained parts.
    
    WARNING:The -1 on statements is systematic because statements numbering is starting at 1
    """
    data = struct_in[name]
    safes= []
    for sub_name in data["contains"]:
        safes.append([struct_in[sub_name]["statements"][0]-1,struct_in[sub_name]["statements"][1]-1])

    return _strip_safe_lines(data["statements"][0]-1,data["statements"][1]-1,safes)


def struct_augment(struct_in: dict, clean_code:List[str],find_callables:Callable, compute_ccn:Callable) -> dict:
    """Complete the description of each struct item"""
    struct = deepcopy(struct_in)
    # first lines computation
    for _, data in struct.items():
        data["NLOC"] = data["lines"][-1] - data["lines"][0] + 1
        data["ssize"] = data["statements"][-1] - data["statements"][0] + 1

    # add internal links
    for part, data in struct.items():
        path = data["path"]
        if len(data["path"]) > 1:
            parent = data["path"][:-1]
            try:
                struct[list2pathref(parent)]["contains"].append(list2pathref(path))
            except KeyError:
                pass
                #will happen for scripts, with "dummy" not always referenced.
            struct[part]["parent"]=list2pathref(parent)
        else:
            struct[part]["parent"]=None

    # add language specific analyses
    for part, data in struct.items():
        actual_lines=struct_actual_lines(struct,part)
        sub_code = [clean_code[i] for i in actual_lines]
        # logger.critical(part)
        # for i,line in enumerate(clean_code):
        #     if i  in actual_lines:
        #         logger.success(line)
        #     else:
        #         logger.warning(line)
        data["callables"] = find_callables(sub_code)
        if struct[part]["parent"] is not None:
            data["callables"] = replace_self(data["callables"],struct[part]["parent"])
        if struct[part]["type"] in ["class"]:
            data["contains"] = replace_self(data["contains"],part)
            data["callables"] = replace_self(data["callables"],part)

        data["CCN"] = compute_ccn(sub_code)

    return struct
