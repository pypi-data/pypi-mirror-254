from typing import List
from loguru import logger

from tucan.unformat_common import (
    Statements,
    new_stmts,
    get_indent,
    eat_spaces,
    remove_strings,
    clean_blanks,
    clean_inline_comments,
    rm_parenthesis_content,
    clean_pure_comments,
    align_multiline_blocks,
    split_multi_statement_lines,
    get_indent,
)

from tucan.kw_lang import KEYWORDS_C

# TODO remove all spaces and reformat?
def remove_space_in_front_of_variables(stmts: Statements) -> Statements:
    """_summary_

    Args:
        stmts (Statements): _description_

    Returns:
        Statements: _description_
    """
    new_stmt = []
    new_lines = []
    for line, (lstart, lend) in zip(stmts.stmt, stmts.lines):
        stmt = line
        for keyword in KEYWORDS_C:
            if keyword in line.split() and "=" in line:
                if line.split()[1] == "=":
                    stmt = line.replace(line.split()[0] + " =", line.split()[0] + "=")
                    logger.warning(
                        f"A C Keywords {keyword} is used as a variable in the code. Bad Practice Should Be Avoided"
                    )
                continue
            continue

        new_stmt.append(stmt)
        new_lines.append([lstart, lend])

    return Statements(new_stmt, new_lines)


def align_unfinished_lines(stmts: Statements) -> Statements:
    """Align lines not finished by ; """
    new_stmt = []
    new_lines = []
    stmt = None
    level=0
    for line, (lstart, lend) in zip(stmts.stmt, stmts.lines):

        for char in line:
            if char == "{":
                level +=1
            if char == "}":
                level -=1
    
        # exception for includes
        if line.startswith("#"):
            new_stmt.append(line)
            new_lines.append([lstart, lend])
            continue

        if stmt is None:
            stmt = line.rstrip()
            istart = lstart
        else:
            stmt += " "+line.strip()

        if stmt.endswith(";") or (stmt.endswith("}") and level==0):
            new_stmt.append(stmt)
            new_lines.append([istart, lend])
            stmt=None
        
       
    if stmt is not None and stmt.strip() != "":
        logger.warning(f"Last statement not finished by ; \n {stmt}")
    return Statements(new_stmt, new_lines)


def split_multiple_statements(stmts: Statements) -> Statements:
    """Split lines with multiples ; """
    new_stmt = []
    new_lines = []
    for line, (lstart, lend) in zip(stmts.stmt, stmts.lines):
        if line.lstrip().startswith("for "):
            new_stmt.append(line)
            new_lines.append([lstart, lend])
            continue



        stmt = line.rstrip(";").rstrip()
        indent=get_indent(line)
        for item in stmt.split(";"):
            new_stmt.append(indent+item.strip()+";")
            new_lines.append([lstart, lend])
        
    return Statements(new_stmt, new_lines)


def split_declarations(stmts: Statements) -> Statements:
    """Split functions declarations, to make clean signatures """
    new_stmt = []
    new_lines = []
    tail = " ###==============================="

   

    def _need_split(buffer:str)->bool:
        try:
            cleanstr = rm_parenthesis_content(buffer[:-1])
            type_,name_ = cleanstr.lstrip().split()
            if "=" not in name_:
                return True
        except ValueError:
            pass
        return False


    for line, (lstart, lend) in zip(stmts.stmt, stmts.lines):
        buffer=""
        for char in line:
            buffer+=char
            if char == "{":
                if _need_split(buffer):
                    new_stmt.append(buffer+tail)
                    new_lines.append([lstart, lend])
                    buffer=get_indent(line)+"    "
            if char == "}":
                pass
        new_stmt.append(buffer)
        new_lines.append([lstart, lend])
    return Statements(new_stmt, new_lines)


def unformat_c(code: List[str]) -> Statements:
    """
    Unformat C code by stripping comments and moving leading '&' characters.

    Args:
        code (List[str]): List of C code lines.

    Returns:
        List[Tuple[str, Tuple[int, int]]]: List of unformatted code statements along with line number ranges.
    """
    stmts = new_stmts(code)
    stmts.stmt = eat_spaces(stmts.stmt)
    stmts.stmt = remove_strings(stmts.stmt, '"')
    stmts.stmt = remove_strings(stmts.stmt, "'")
    stmts = align_multiline_blocks(stmts, "/*", "*/")
    stmts = clean_inline_comments(stmts, "/*") # this ine must follow the align multiline block
    stmts = clean_inline_comments(stmts, "//")
    stmts = clean_blanks(stmts)                # this one must follow the clean inline, to remove blank lines
    stmts = align_unfinished_lines(stmts)
    stmts = split_multiple_statements(stmts)
    stmts = split_declarations(stmts)
    
    #stmts = remove_space_in_front_of_variables(stmts)

    return stmts
