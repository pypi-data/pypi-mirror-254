import re
from typing import Tuple
from loguru import logger
from tucan.unformat_common import Statements
from tucan.struct_common import (
    find_words_before_left_parenthesis,
    buffer_item,
    stack_item,
    struct_from_stack,
    struct_augment,
)
from tucan.kw_lang import KEYWORDS_PY


def extract_struct_py(statements: Statements) -> dict:
    """Main calls to build structure form statements

    statements is the output of tucan.unformat_py.unformat_py
    """

    clean_code = statements.to_code()
    all_structs = _extract_on_cleaned_py(statements)
    all_structs = struct_augment(all_structs,clean_code,find_callables_py,compute_ccn_approx_py)
    return all_structs


def _extract_on_cleaned_py(stmts: Statements) -> dict:
    """Extract structure from cleaned statements."""
    buffer = []
    stack = []
    path = []
    last_indent = 0
    last_line = None
    stat_idx = -1
    for line, (line_idx1, line_idx2) in zip(stmts.stmt, stmts.lines):
        stat_idx += 1
        indent = int(len(re.findall(r"\s{4}|\s\t+", line)))

        # Find correctly the indentation without accessing spaces in strings
        indent = re.findall(r"^\s+", line)
        if indent:
            indent = int(len(indent[0]) / 4)
        else:
            indent = 0

        # Evaluate indentation level for path and buffer
        if indent > last_indent:
            if indent > last_indent + 1:
                logger.warning(
                    f"Multiple indent at {path} for '{line}' with last indent : {last_indent} and current : {indent}"
                )
                indent = last_indent + 1
            type_, name = parse_name_py(last_line)

            path.append(name)
            buffer.append(
                buffer_item(
                    type_=type_,
                    name=name,
                    first_line=last_line,
                    line_idx=last_idx,
                    statement_idx=stat_idx,
                )
            )
            last_line = line
            last_idx = line_idx2
            last_indent = indent
            continue

        elif indent < last_indent:
            for _ in range(last_indent - indent):
                (type_, name, first_line, line_idx, statement_idx) = buffer[-1]
                stack.append(
                    stack_item(
                        type_=type_,
                        name=name,
                        path=path.copy(),
                        start_line_idx=line_idx,
                        start_statement_idx=statement_idx,
                        start_line=first_line,
                        end_line_idx=last_idx,
                        end_statement_idx=stat_idx,
                        end_line=line,
                    )
                )
                path.pop(-1)
                buffer.pop(-1)
            last_line = line
            last_indent = indent
            last_idx = line_idx1
            continue

        last_line = line
        last_indent = indent
        last_idx = line_idx1

    return struct_from_stack(
        stack, main_types=["def", "class"], skip_types=["if", "for"]
    )


def parse_name_py(line: str) -> Tuple[str, str]:
    """expect a lowercase stripped line
    takes the second word as the name
    """
    type_ = line.strip().split()[0]

    try:
        name = line.strip().replace("(", " ").split()[1].replace(":", " ").split()[0]
    except IndexError:
        name = "dummy"

    return type_, name


##### Main structs

def find_callables_py(code: list) -> list:
    """Find callables in python"""
    candidates = []
    for line in code:
        if not line.strip().startswith("def") and not line.strip().startswith("class"):
            candidates.extend(find_words_before_left_parenthesis(line.strip()))
    matches = [cand.strip() for cand in set(candidates) if cand not in KEYWORDS_PY]

    return sorted(matches)  # Must be sorted for testing

def find_annotations_from_args_py(line:str) -> dict:
    """Find annotation in arguments"""
    id1 = line.find('(')
    id2 = line.rfind(')')
    out={}
    for arg in line[id1+1: id2].split(","):
        if ":" in arg:
            arg,type_=arg.split("=")[0].split(":")
            out[arg]=type_
    return out
            

def compute_ccn_approx_py(code: list) -> int:
    """Count decision points (if, else if, do, select, etc.)"""
    decision_points = re.findall(r"(?i)(if |elif|for|try|except )", "\n".join(code))
    complexity = len(decision_points) + 1
    return complexity
