CSI = '\033['


def get_escape_sequence(code):
    return CSI + str(code) + 'm'


class ANSI:
    CSI = '\033['

    def __init__(self):
        for code in dir(self):
            if not code.startswith('_'):
                setattr(self, code, get_escape_sequence(getattr(self, code)))


class BG(ANSI):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    DEFAULT = 49
    RESET = 0


class FG(ANSI):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39
    RESET = 0


class SGR(ANSI):
    BRIGHT = 1
    DIM = 2
    NORMAL = 22
    RESET = 0


Background = BG()
Foreground = FG()
Style = SGR()
