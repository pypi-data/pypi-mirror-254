from dataclasses import dataclass

# ANSI 24 bit - RGB colors
def chex(hex: str):
    r,g,b = tuple(int(hex.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    return "\033[38;2;{};{};{}m".format(r,g,b)

# ANSI 8 bit - 256 colors
def cansi(color: int):
    return "\033[38;5;{}m".format(color)

# ANSI 3/4 bit
def clegacy(color: int):
    return "\033[{}m".format(color)

def ansistr(__str: str, color: int):
    return cansi(color) + __str + cansi(0)

def legacy_ansistr(__str: str, color: int):
    return clegacy(color) + __str + cansi(0)


def hexstr(__str: str, hex: str):
    return chex(hex) + __str + "\033[0m"

@dataclass
class DefaultColors:
    black = cansi(0)
    red = cansi(1)
    green = cansi(2)
    yellow = cansi(3)
    blue = cansi(4)
    magenta = cansi(5)
    cyan = cansi(6)
    silver = cansi(7)
    grey = cansi(8)
    highred = cansi(9)
    highgreen = cansi(10)
    highyellow = cansi(11)
    highblue = cansi(12)
    highmagenta = cansi(13)
    highcyan = cansi(14)
    white = cansi(15)
    reset = "\033[0m"
