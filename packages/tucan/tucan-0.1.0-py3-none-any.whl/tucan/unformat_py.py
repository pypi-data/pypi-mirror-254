from loguru import logger
from typing import List

from tucan.unformat_common import (
    Statements,
    new_stmts, 
    remove_strings,
    clean_blanks,
    eat_spaces,
    clean_inline_comments,
    #align_multiline_blocks,
    split_multi_statement_lines,
    get_indent
)

COMB_CHARS = {
    "'''":"\xaa",
    '"""':"\xbb"
}

def remove_combined_chars(code: List[str]) -> List[str]:
    """replace combined chars with single char alternatives"""
    new_code=[]
    for line in code:
        rline=line
        for cchar,rchar in COMB_CHARS.items():
            rline=rline.replace(cchar,rchar)
        new_code.append(rline)
    return new_code


def getback_combined_chars(code: List[str]) -> List[str]:
    """replace combined chars with single char alternatives, back"""
    new_code=[]
    for line in code:
        rline=line
        for cchar,rchar in COMB_CHARS.items():
            rline=rline.replace(rchar,cchar)
        new_code.append(rline)
    return new_code


def align_continuation_lines(stmts:Statements)->Statements:
    """Merge lines using \\ symbol at continuation line"""
    new_stmt=[]
    new_lines=[]
    last_line=""
    for line, (lstart,lend) in zip(stmts.stmt,stmts.lines):
        if last_line.endswith("\\"):
            new_stmt[-1]=last_line[:-1]+" "+line.strip()
            new_lines[-1][1]=lend
        else:
            new_stmt.append(line)
            new_lines.append([lstart,lend])

        last_line=new_stmt[-1]
    return Statements(new_stmt,new_lines)


def align_multiline_strings(stmts:Statements, markup:str)->Statements:
    new_stmt=[]
    new_lines=[]
    buffer =""
        
    in_multiline=False
    for line, (lstart,lend) in zip(stmts.stmt,stmts.lines):
        
        
        if in_multiline:
            line=" "+line.lstrip()
        
        if not in_multiline:
            last_start=lstart

        for char in line:
            if char==markup:
                if not in_multiline:
                    in_multiline=True
                else:
                    in_multiline=False
            buffer+=char
        # end of line reached...

        if not in_multiline:
            new_stmt.append(buffer)
            new_lines.append([last_start,lend])
            buffer =""
    
            
    return Statements(new_stmt,new_lines)


def align_context_block(stmts:Statements)->Statements:
    """
    Join statements on [({})] 
    
    Args:
        stmts (stmts): List of unformatted code statements along with line number ranges.
    Returns:
        Statements: List of unformatted code statements along with line number ranges. Everything in
            a parenthesis is now a one liner.
    """
    new_stmt=[]
    new_lines=[]
    inside_block_context=[]
    buffer=""
    for line, (lstart,lend) in zip(stmts.stmt,stmts.lines):
        if not inside_block_context:
            this_start=lstart
            indent=get_indent(line)

        for char in line.lstrip():
            buffer+=char
            if char in ["(","[","{",]:
                inside_block_context.append(char)
                continue
            if char in [")","]","}"]:
                try:
                    inside_block_context.pop(-1)
                except IndexError:
                    logger.warning(f"line {lstart} , unmatched context closing symbol -{char}-")
                continue
                
        #EOL reached !

        if not inside_block_context:
            new_stmt.append(indent+buffer)
            new_lines.append([this_start, lend])
            buffer=""

    return Statements(new_stmt,new_lines)  



def split_fstrings(code:List[str], fstring_char:str, other_char:str)->List[str]:
    new_stmt=[]

    for line in code:
        inside_fstring_context=False
        #inside_escape_context=False
        buffer=""
        last_char=" "
        for char in line:
            if char== fstring_char:
                if last_char=="f" :
                    inside_fstring_context=True
                else:
                    inside_fstring_context=False

            if inside_fstring_context and char ==other_char:
                char="_"

            buffer+=char

            if inside_fstring_context:
                if char=="{":
                    
                    buffer =buffer[:-2] + fstring_char + "{"
                    #inside_escape_context=True
                elif char=="}":
                    #buffer+=char
                    buffer+=fstring_char  # insert one quotation after }
                    #inside_escape_context=True
            
            last_char=char

        new_stmt.append(buffer)
    return new_stmt



def unformat_py(code: List[str]) -> Statements:
    """
    Unformat Python code by stripping comments and breaking multiline statements.

    Args:
        code (List[str]): List of Python code lines.

    Returns:
        Statements: List of unformatted code statements along with line number ranges.
    """
    stmts = new_stmts(code)
    stmts.stmt = eat_spaces(stmts.stmt)
    stmts.stmt = remove_combined_chars(stmts.stmt)
    stmts = align_continuation_lines(stmts) 
    stmts = align_multiline_strings(stmts, "\xaa")
    stmts = align_multiline_strings(stmts, "\xbb") 

    stmts.stmt = remove_strings(stmts.stmt,"\xaa")
    stmts.stmt = remove_strings(stmts.stmt,"\xbb")
    stmts.stmt = split_fstrings(stmts.stmt,"'",'"')
    stmts.stmt = split_fstrings(stmts.stmt,'"',"'")
    stmts.stmt = remove_strings(stmts.stmt,"'")
    stmts.stmt = remove_strings(stmts.stmt,'"')
    
    stmts = clean_inline_comments(stmts,"#") 
    stmts = clean_blanks(stmts)
    stmts = split_multi_statement_lines(stmts)
    stmts = align_context_block(stmts)
    
    stmts.stmt = getback_combined_chars(stmts.stmt)
    return stmts
