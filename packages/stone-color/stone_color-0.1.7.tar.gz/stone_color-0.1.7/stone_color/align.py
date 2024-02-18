import os

from .messages import printf

def center(__str: str, rm=0, lm=0):
    columns = os.get_terminal_size().columns
    rspaces = " " * rm
    lspaces = " " * lm

    for s in __str.splitlines():
        center_column = (columns - len(s)) // 2
        spaces = " "*center_column
        printf(spaces + lspaces + s + rspaces)

def right(__str: str, rm=0, lm=0):
    columns = os.get_terminal_size().columns
    rspaces = " " * rm
    lspaces = " " * lm


    for s in __str.splitlines():
        right_column = (columns - len(s))
        spaces = " "*right_column
        printf(spaces + lspaces + s + rspaces)
