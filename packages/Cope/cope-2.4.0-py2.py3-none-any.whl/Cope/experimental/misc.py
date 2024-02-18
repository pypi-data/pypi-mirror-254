# from .decorators import todo, confidence
from .imports import dependsOnPackage
from ..debugging import get_varname, called_as_decorator, debug, get_metadata
# from .colors import ERROR
import re
import subprocess
from os.path import join
from random import randint
import sys
# from math import floor

# @todo('Make this use piping and return the command output', False)
def runCmd(args):
    """ Run a command and terminate if it fails. """
    try:
        ec = subprocess.call(' '.join(args), shell=True)
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
        ec = 1
    if ec:
        sys.exit(ec)

def center(string):
    """ Centers a string for printing in the terminal """
    from os import get_terminal_size
    for _ in range(int((get_terminal_size().columns - len(string)) / 2)): string = ' ' + string
    return string


# TODO: Failing
def insert_newlines(string:str, max_line_length:int) -> str:
    """ Inserts newline characters into `string` in order to keep `string` under `max_line_length`
        characters long, while not inserting a newline in the middle of a word
    """
    # split the string into a list of words
    words = string.split()
    # initialize the result as an empty string
    result = ""
    # initialize the current line as an empty string
    current_line = words[0]
    # iterate over the words in the list
    for word in words[1:]:
        # if the current line plus the next word would exceed the maximum line length,
        # add a newline character to the result and reset the current line
        if len(current_line) + 1 + len(word) > max_line_length:
            result += current_line + "\n"
            current_line = word
        else:
            # add the word to the current line and a space character after it
            current_line += " " + word
    return result

def assertValue(param, *values, blocking=True):
    paramName = get_varname(param)
    if not called_as_decorator('assertValue'):
        if param not in values:
            err = TypeError(f"Invalid value for {paramName}, must be one of: {values}")
            if blocking:
                raise err
            else:
                debug(err)
    else:
        print('TODO: AssertValue usage as a decorator')
