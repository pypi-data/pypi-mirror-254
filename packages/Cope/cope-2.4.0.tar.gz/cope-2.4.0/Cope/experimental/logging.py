# from .colors import LOG_COLOR, coloredOutput, WARN
from ..debugging import print_context
from enum import Enum
from ._config import config

class LogLevel(Enum):
    NONE = 0
    LOGGING = 1
    WARNINGS = 2
    ERRORS = 3

def log(message, levelReq=LogLevel.LOGGING):
    if not __debug__: return
    if config.verbosity >= levelReq.value:
        print_context(2)
        print(message, style='log')

def warn(message):
    if not __debug__: return
    log(message, color=WARN)
warning = warn

def unreachableState(message=''):
    if not __debug__: return
    if len(message):
        warn(f'Unreachable State Reached: {message}')
    else:
        warn('Unreachable State Reached!')
unreachable = unreachableState
