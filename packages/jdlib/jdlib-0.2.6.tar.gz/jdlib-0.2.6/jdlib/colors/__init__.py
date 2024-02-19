import sys

from jdlib.colors.ansi import Background, Foreground, Style

def write(text, bg=None, fg=None, style=None, end=''):
    if bg is not None:
        text = bg + text + Background.RESET
    if fg is not None:
        text = fg + text + Foreground.RESET
    if style is not None:
        text = style + text + Style.RESET
    sys.stdout.write(text + end)

def success(text):
    write(text, fg=Foreground.GREEN, style=Style.BRIGHT, end='\n')

def error(text):
    write(text, fg=Foreground.RED, style=Style.BRIGHT, end='\n')

def warning(text):
    write(text, fg=Foreground.YELLOW, style=Style.BRIGHT, end='\n')

def info(text):
    write(text, fg=Foreground.BLUE, style=Style.BRIGHT, end='\n')
