from os import get_terminal_size, system
import inspect
import re

# class TermHelper():
term_size = get_terminal_size().columns


def top_wrap(string, char="*"):
    system("clear")
    term_wrap(string, char)


def term_wrap(string, char="*"):
    star_line(char)
    center_string_stars(string, char)
    star_line(char)


def star_line(char="*"):
    print(char[0] * term_size)


def center_string_stars(string, char="*"):
    half_size = (term_size - len(string) - 2) / 2
    half_stars = char[0] * int(half_size)
    print(f"{half_stars} {string} {half_stars}")


def kv_print(obj):
    frame = inspect.currentframe()
    try:
        context = inspect.getframeinfo(frame.f_back).code_context
        caller_lines = ''.join([line.strip() for line in context])
        m = re.search(r'kv_print\s*\((.+?)\)$', caller_lines)
        if m:
            key = m.group(1)
            print(f'{key} => {obj}')
    finally:
        del frame
