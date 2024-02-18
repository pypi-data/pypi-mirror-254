from sys import stdout, stderr
import re

from . import color

colors = color.DefaultColors

_alert = colors.highred + "[!]" + colors.reset
_warn = colors.highyellow + "[@]" + colors.reset
_info = colors.cyan + "[?]" + colors.reset 
_success = colors.green + "[+]" + colors.reset
_error = colors.red + "[-]" + colors.reset 

auto_reset = False

def alertf(*objs, end="\n", sep=" ", file=stderr, flush=False):
    file.write(_alert + " " + sep.join(map(str, objs)) + end)
    if flush:
        file.flush()

def warnf(*objs, end="\n", start="", sep=" ", file=stderr, flush=False):
    file.write(start +_warn + " " + sep.join(map(str, objs)) + end)
    if flush:
        file.flush()

def infof(*objs, end="\n", start="", sep=" ", file=stderr, flush=False):
    file.write(start + _info + " " + sep.join(map(str, objs)) + end)
    if flush:
        file.flush()

def successf(*objs, end="\n", start="", sep=" ", file=stderr, flush=False):
    file.write(start + _success + " " + sep.join(map(str, objs)) + end)
    if flush:
        file.flush()
    

def errorf(*objs, end="\n", start="", sep=" ", file=stderr, flush=False):
    file.write(start + _error + " " + sep.join(map(str, objs)) + end)
    if flush:
        file.flush()

def printf(*objs, end="\n", sep=" ", file=stdout, flush=False):
    __text = sep.join(map(str, objs)) + end

    def color_replace(match):
        hex = match.group(1)

        if hex == "reset":
            return "\033[0m"
        else:
            return color.chex(hex)

    __text = re.sub(r"\{#([^}]+)\}", color_replace, __text)
    
    if auto_reset:
        __text += "\033[0m"

    file.write(__text) 
    
    if flush:
        file.flush()
    
