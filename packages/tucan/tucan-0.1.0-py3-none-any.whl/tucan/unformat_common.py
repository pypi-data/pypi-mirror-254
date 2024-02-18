"""
Module that gather the most common functions of unformat
"""

from __future__ import annotations
from typing import Tuple,List
from dataclasses import dataclass
from loguru import logger
import json


@dataclass
class Statements():
    stmt:List[str]= None
    lines:List[Tuple[int,int]]= None

    def __str__(self):
        out=""
        for line,(i1,i2) in zip(self.stmt,self.lines):
            out+= f"({i1}-{i2})  {line}\n"
        out += "======================="
        out += f"Statements found : {len(self.stmt)}"
        return out
    
    def to_code(self):
        out=[f"{stmt}\n" for stmt in self.stmt]
        return out
    
    def to_nob(self):
        return [[st, lsp] for st,lsp in zip(self.stmt, self.lines)]

    def dump_json(self,newfile):
        
        logger.info(f"Data dumped to {newfile}")
        with open(newfile,"w") as fout:
            json.dump(self.to_nob(),fout,indent=2,sort_keys=True)

    def dump_code(self,newfile):
        
        with open(newfile,"w") as fout:
            fout.writelines(self.to_code())
        print(f"\n\nCleaned version dumped in {newfile}")



def new_stmts(code:List[str])->Statements:
    return Statements(
        code,
        [[i+1,i+1] for i,_ in enumerate(code)]
    )


def remove_strings(code:List[str], string_char:str)->List[str]:
    new_stmt=[]

    for line in code:
        inside_string_context=False
        buffer=""
        tmp_buffer=""
        for char in line:
            if char == string_char:
                if not inside_string_context:
                    inside_string_context=True
                else:
                    buffer+=f"{char}___"
                    inside_string_context=False
                    tmp_buffer=""
                #buffer+=char
            
            if not inside_string_context:
                buffer+=char
            else:
                tmp_buffer+=char

        if inside_string_context: #if the string context is not ended ath the end of the line, put the skipped chars
            buffer+=tmp_buffer

        new_stmt.append(buffer)
    return new_stmt


def rm_parenthesis_content(buffer:str, lchar:str="(", rchar:str=")", greedy=True)->str:
    """Remove the content of parenthesis"""
    lvl=0
    out=""
    for char in buffer:
        if lvl==0:
            out+=char
        if char == lchar:
            lvl+=1
            
        if char == rchar:
            lvl-=1
    
    if greedy:
        out = out.replace( lchar, "")
        out = out.replace( rchar, "")
    return out
        

def clean_blanks(stmts:Statements)->Statements:
    """
    Perform the first pass to strip comments and blank lines.

    Args:
        code (List[str]): List of code lines.

    Returns:
        List[Tuple[str, int]]: List of code lines without comments and blank lines.
    """
    new_stmt=[]
    new_lines=[]
    for line, lines_span in zip(stmts.stmt,stmts.lines):
        if line.strip() == "":  # Blank lines
            continue

        new_stmt.append(line)
        new_lines.append(lines_span)
        
    # Add final newline if missing. Useful to finish cleanly the parsing
    if new_stmt:
        if new_stmt[-1] != "":
            new_stmt.append("")
            last_line=new_lines[-1][0]
            new_lines.append([last_line+1,last_line+1])
        
    return Statements(new_stmt,new_lines)


def eat_spaces(code:List[str])->List[str]:
    """Remove unwanted multiple spacing """
    new_stmt = []
    for line in code:
        out=get_indent(line)
        
        prevchar=None    
        for i,char in enumerate(line.strip()):
            try:
                next_char=line.strip()[i+1]
            except IndexError:
                next_char=None
            
            if char == " ":
                if prevchar not in [" ",":",";",","] and next_char not in [":",";",","] :
                    out+=char
                else:
                    pass # no space needed if " " precedes, or a punctuation is before or after
            else:
                out+=char

            prevchar=char
        new_stmt.append(out)  
    return new_stmt



def clean_inline_comments(stmts:Statements, symbol:str="#")->Statements:
    """
   
    """
    new_stmt=[]
    new_lines=[]
    for line, lines_span in zip(stmts.stmt,stmts.lines):
        
        if symbol in line:
            line=line.split(symbol)[0].rstrip()
            if line.strip()=="":
                continue
        new_stmt.append(line)
        new_lines.append(lines_span)
        
    return Statements(new_stmt,new_lines)

def clean_pure_comments(stmts:Statements, symbol:str="#")->Statements:
    """
   
    """
    new_stmt=[]
    new_lines=[]
    for line, lines_span in zip(stmts.stmt,stmts.lines):
        if line.startswith(symbol):
            continue
        new_stmt.append(line)
        new_lines.append(lines_span)
    return Statements(new_stmt,new_lines)


def split_multi_statement_lines(stmts:Statements)->Statements:
    """Split statements on ;"""
    new_stmt=[]
    new_lines=[]
    for line, (lstart,lend) in zip(stmts.stmt,stmts.lines):
        if ";" not in line:
            new_stmt.append(line)
            new_lines.append([lstart,lend])
        else:
            indent=get_indent(line)
            for stmt in line.split(";"):
                new_stmt.append(indent+stmt.strip())
                new_lines.append([lstart,lend])
    return Statements(new_stmt,new_lines)


def align_multiline_blocks(stmts:Statements, markup_in:str,markup_out:str)->Statements:
    
    proxy_in = markup_in
    proxy_out = markup_out
    if len(markup_in)>1:
        proxy_in="\xaa"
    if len(markup_out)>1:
        proxy_out="\xbb"

    new_stmt=[]
    new_lines=[]
    buffer =""
        
    in_multiline=False
    for line, (lstart,lend) in zip(stmts.stmt,stmts.lines):
        if in_multiline:
            line=" "+line.lstrip()
        
        if not in_multiline:
            last_start=lstart


        for char in line.replace(markup_in,proxy_in).replace(markup_out,proxy_out):
            if char==proxy_in:
                in_multiline=True
                buffer+=markup_in
            elif char==proxy_out:
                in_multiline=False
                buffer+=markup_out
            else:
                buffer+=char
        # end of line reached...
        #buffer = buffer.replace(proxy_in,markup_in).replace(proxy_out,markup_out)
        if not in_multiline:
            new_stmt.append(buffer)
            new_lines.append([last_start,lend])
            buffer =""
    
            
    return Statements(new_stmt,new_lines)

def get_indent(line:str)->str:
    _indent=""
    for char in line:
        if char == "\t":
            _indent+="    "
        elif char != " ":
            break
        else:
            _indent+=" "
    return _indent