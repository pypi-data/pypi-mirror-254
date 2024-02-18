import re
from loguru import logger
from tucan.unformat_common import Statements
from tucan.struct_common import (
    find_words_before_left_parenthesis,
    buffer_item,
    stack_item,
    struct_from_stack,
    struct_augment,
)
from tucan.unformat_common import (
    rm_parenthesis_content
)

from tucan.kw_lang import STRUCTURES_FTN,NESTS_FTN,OTHERS_FTN


PARTS = sorted(STRUCTURES_FTN, reverse=True)
NESTS =sorted(NESTS_FTN, reverse=True)
INTRINSICS= OTHERS_FTN


def extract_struct_ftn(stmts: Statements) -> dict:
    """Main calls to build structure form statements

    statements is the output of tucan.unformat_ftn.unformat_ftn
    """
    clean_code = stmts.to_code()
    all_structs = _extract_on_cleaned_ftn(stmts)
    all_structs = struct_augment(all_structs, clean_code, find_callables_ftn, compute_ccn_approx_ftn)
    return all_structs


def _extract_on_cleaned_ftn(stmts: Statements, verbose=False) -> dict:
    """Extract structure from cleaned statements."""
    buffer = []
    stack = []
    path = []

    entry_ = []
    out_ = []
    stat_idx = 0
    for line, (line_idx1, line_idx2) in zip(stmts.stmt, stmts.lines):
        stat_idx += 1
        # you must also note nests because bare end statement can jam the system
        # kw are listed in reverse order to try longer kwords first: type_real before
        #for part in sorted(STRUCTURES_FTN + NESTS_FTN, reverse=True):
        for part in sorted(PARTS + NESTS, reverse=True):
            if line.lstrip().startswith(part+" "):
               
                if line.lstrip().startswith("type") and line.split()[1].startswith("("):
                    continue
                if line.lstrip().startswith("type_is"):
                    continue
                
                if line.strip().startswith("module_procedure"):
                    continue

                entry_.append(part)
                name = _parse_name_ftn(line,line_idx1)
                fname = ".".join(path)+"."+name
                if verbose:
                    logger.critical(f"START l.{line_idx1} for "+fname)
                buffer.append(
                    buffer_item(
                        type_=part,
                        name=name,
                        first_line=line,
                        line_idx=line_idx1,
                        statement_idx=stat_idx,
                    )
                )
                path.append(name)
                break # must not look at the following part, or both function and function_elemental will trigger

        if line.strip().startswith("end ") or line.strip() == "end":
            out_.append(line)
            try:
                (type_, name, line_start, line_idx, statement_idx) = buffer[-1]  #Here
            except IndexError:
                logger.critical(f"No buffer for line {line_idx1}:{line}")

            fname = ".".join(path)#+"."+name
            if verbose:
                logger.critical(f"END   l.{line_idx1} for "+fname)
            stack.append(
                stack_item(
                    type_=type_,
                    name=name,
                    path=path.copy(),
                    start_line_idx=line_idx,
                    start_statement_idx=statement_idx,
                    start_line=line_start,
                    end_line_idx=line_idx2,
                    end_statement_idx=stat_idx,
                    end_line=line,
                )
            )
            path.pop(-1)
            buffer.pop(-1)
            continue

    # Check specific to fortran
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
        if type_.split("_")[0].strip() not in end_line:  # TODO , why ',' here.
            pathstr=".".join(path)
            logger.debug(
                f"End mismatch \nat {pathstr} :\n '{start_line_idx}' to '{end_line_idx}'.\n For {type_} in {end_line}"
            )
    if len(entry_) != len(out_):
        logger.error(
            "Missing one structure statement such as end if... removing file from current analysis"
        )
        return {}

    return struct_from_stack(stack, main_types=PARTS)


def _parse_name_ftn(line: str, line_nb:int):
    """expect a lowercase stripped line
    takes the second word as the name
    """

    line = rm_parenthesis_content(line)
    
    if line.split()[0] in NESTS:
        name = line.split()[0]+str(line_nb)
        if "#LABEL" in line:
            name+= "_"+line.split("#")[-1].split(":")[-1].strip()
        return name
    
    if line.split()[0].startswith("type"):
        name= line.split(":")[-1].strip()
        return name

    line = line.replace(":"," ") # to get rid of ::
    try:
        name = line.split()[1]
    except IndexError:
        name = line.split()[0]+str(line_nb)
        
    
    return name


##### FTN specific functions


def find_callables_ftn(code: list) -> list:
    """Find callables in python"""
    candidates = []
    for line in code:
        if " call " in line:
            candidates.append(line.split("(")[0].split()[-1])
        else:
            candidates.extend(find_words_before_left_parenthesis(line.strip()))
    # NB we expect lines like 'call mysubroutine()' to be caught by left parenthesis law$
    matches = [cand for cand in set(candidates) if cand not in INTRINSICS]

    return sorted(matches)  # Must be sorted for testing


def compute_ccn_approx_ftn(code: list) -> int:
    """Count decision points (if, else if, do, select, etc.)"""
    decision_points = re.findall(
        r"(?i)(if |else if|do |select case|select default)", "\n".join(code)
    )
    complexity = len(decision_points) + 1
    return complexity
