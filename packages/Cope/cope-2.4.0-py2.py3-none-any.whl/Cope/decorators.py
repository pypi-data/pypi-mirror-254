"""
Miscellaneous decorators that can be useful
"""

from .debugging import get_metadata, called_as_decorator, print_debug_count, get_context, print_context
from .misc import interpret_percentage
from warnings import warn
# from .colors import coloredOutput, darken
# from ._config import config
_todoCalls = set()
hide_todo = False


class EpistemologicalWarning(UserWarning):
    """ This is a joke/pet peeve of mine for people who say they're 100% confident in something """
    pass

def todo(feature:str=None, enabled:bool=True, blocking:bool=False, limit:bool=True):
    # Can be manually turned on or off with hideAllTodos(bool).
    """ Leave reminders for yourself to finish parts of your code.
        Can also be used as a decorator (for functions or classes) to print a reminder and optionally
        throw a NotImplemented error on being called/constructed.
        Parameters:
            enabled: enable or disable printed warnings
            blocking: raise an error, instead of just warning you
            limit: if called multiple times, and this is true, only print once
    """

    if not __debug__:
        return

    metadata = get_metadata(2)
    situation = called_as_decorator('todo', metadata)
    # First off, if we're limiting calls, check if we've already been called
    uniqueID = (metadata.lineno, metadata.filename)
    if limit and uniqueID in _todoCalls:
        return
    else:
        _todoCalls.add(uniqueID)

    def printTodo(disableFunc):
        if not hide_todo and enabled:
            print_debug_count()
            print(get_context(metadata, path=True, func=False if disableFunc else None), end='', style=color)
             # This is coincidental, but it works
            print(f'TODO: {feature.__name__ if disableFunc else feature}')
            if blocking:
                raise NotImplementedError(feature)

    # Being used as a function decorator, or we're not sure
    if situation in (1, 3):
        def wrap(func):
            def innerWrap(*funcArgs, **funcKwArgs):
                printTodo(True)
                if blocking:
                    raise NotImplementedError(feature)
                return feature(*funcArgs, **funcKwArgs)
            return innerWrap
        return wrap

    elif situation == 2:
        def wrap(clas):
            def raiseErr(*_, **kw_):
                raise NotImplementedError(feature)
            printTodo(True)
            if blocking:
                feature.__init__ = raiseErr
        return feature
    else:
        printTodo(False)

def confidence(level:float):
    if not __debug__:
        return

    level = interpret_percentage(level) * 100

    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):

            # This is a pet-peeve
            if level > 100:
                raise TypeError(f"You can't be {level}% confident, that's not how it works.")
            elif level == 100:
                raise EpistemologicalWarning(f'Are you *sure* you\'re 100% confident? (not 99.99%?)')
            # Definite Failure
            elif level < 10:
                raise UserWarning(f"{func.__name__} will almost certainly going to fail. ({level}% confidence)")
            # Likely Failure
            elif level <= 50:
                print_context(3, func=False, color='warn')
                print(f"Warning: {func.__name__} will probably fail. ({level}% confidence)", style='warn')
            # Possible Failure
            elif level < 80:
                # print_context(3, func=False, color='confidence_warning')
                print(f"Warning: {func.__name__} might not work. ({level}% confidence)", style='confidence_warning')

            return func(*funcArgs, **funcKwArgs)
        return innerWrap
    return wrap

def depricated(why=''):
    if not __debug__:
        return

    def wrap(func):
        def innerWrap(*funcArgs, **funcKwArgs):

            print_context(2, color='warn')
            warn(f"{func.__name__} is Depricated{': ' if len(why) else '.'}{why}")

            return func(*funcArgs, **funcKwArgs)
        return innerWrap
    return wrap

def reprise(obj: type, *args, **kwargs) -> type:
    """
    A class decorator that sets the __repr__ member to the __str__ member.
    Not super useful, but nice for quick custom classes.
    """
    obj.__repr__ = obj.__str__
    return obj


confident = confidence
untested = confidence(51)
tested = confidence(95)
