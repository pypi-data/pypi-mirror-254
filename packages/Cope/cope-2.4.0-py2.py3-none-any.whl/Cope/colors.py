import math
# import color-names
from typing import Tuple, Literal
from ._named_colors import named_colors
from .misc import translate
from colorsys import *

def distinct_color(n: int) -> tuple:

    # Credit to chatGPT
    # First, ensure if it's 0, we return black
    if n == 0:
        return 0, 0, 0
    angle = n * 137.508
    r = int(math.sin(angle) * 127 + 128)
    g = int(math.sin(angle + 2 * math.pi / 3) * 127 + 128)
    b = int(math.sin(angle + 4 * math.pi / 3) * 127 + 128)
    return r, g, b

# TODO: add input support for hsv, hls, and yiq
# TODO: add input & output support for hsv, hls, and yiq with 0-255 instead of 0-1
def parse_color(*args, rtn:Literal['html', 'rgb', 'rgba', 'opengl', 'hsv', 'hls', 'yiq']='rgb', **kwargs) -> 'type(rtn)':
    """ One color function to rule them all!
        Parses a color, however you care to pass it, and returns it however you like.

        Input Schemes:
            * Positional parameters
                * parse_color(255, 255, 255, 255)
                * parse_color(255, 255, 255)
            * tuple or list
                * parse_color((255, 255, 255, 255))
                * parse_color((255, 255, 255))
            * Keyword parameters/dict
                * parse_color(r=255, g=255, b=255, a=255)
                * parse_color({'r': 255, 'g': 255, 'b': 255, 'a': 255})
                * parse_color(red=255, green=255, blue=255, alpha=255)
                * parse_color({'red': 255, 'green': 255, 'blue': 255, 'alpha': 255})
            * OpenGL style colors (between -1 and 1)
                * parse_color(1., 1., 1.)
                * parse_color((1., 1., 1.))
            * Hex colors
                * parse_color('#FFFFFF')
                * parse_color('#ffffff')
            * Named colors
                * parse_color('white')
            * "Random" distinct colors
                * parse_color(1)
            * Anything that has r, g, b attributes or red, green, blue attributes (callable or not)
                * parse_color(QColor(255, 255, 255))

        Return Schemes:
            * 'html'
                * #FFFFFF
            * 'rgb'
                * (255, 255, 255)
            * 'rgba'
                * (255, 255, 255, 255)
            * 'opengl'
                * (1., 1., 1., 1.)
            * 'hsv'
                * (0., 0., 1.)
            * 'hls'
                * (0., 1., 0.)
            * 'yiq'
                * (1., 0., 0.)

        If `a` is not provided, but it is selected to be returned, it defaults to the max (255, usually)

        NOTE: Don't pass OpenGL colors as dicts or as keyword arguements. It will interpret them as
            RGBA parameters.
    """
    assert len(args) or len(kwargs)
    a = 255
    r = None
    g = None
    b = None

    if len(args):
        if isinstance(args[0], str):
            # We've been given a hex string
            if args[0].startswith('#'):
                r, g, b = map(lambda n: int(n, 16), args[0][1::2])
            # We've been given the name of a color
            else:
                if (r, g, b := named_colors.get(args[0].lower())) is None:
                    raise TypeError(f'{args[0]} is not a recognized color name')

        # We've been given a list of values
        elif isinstance(args[0], (tuple, list)):
            if len(args[0]) not in (3, 4):
                raise TypeError(f'Incorrect number ({len(args[0])}) of color parameters given. Please give either 3 or 4 parameters')
            else:
                # We've been given an OpenGL color
                if all([isinstance(i, float) and i >= -1 and i <= 1 for i in args[0]]):
                    if len(args[0]) == 3:
                        r, g, b = [translate(i, -1, 1, 0, 255) for i in args[0]]
                    else:
                        r, g, b, a = [translate(i, -1, 1, 0, 255) for i in args[0]]

                # Otherwise, interpret them as ints between 0 and 255
                if len(args[0]) == 3:
                    r, g, b = args[0]
                else:
                    r, g, b, a = args[0]

        # We've been given a single integer
        elif isinstance(args[0], (int, float)) and len(args) == 1:
            r, g, b = distinct_color(int(args[0]))

        # We've been given a dict, for some reason
        elif isinstance(args[0], dict) and len(args) == 1:
            kwargs.update(args[0])

        # We've been given something with color attributes
        elif hasattr(args[0], 'red') and hasattr(args[0], 'green') and hasattr(args[0], 'blue'):
            if hasattr(args[0], 'alpha'):
                if hasattr(args[0].red, '__call__') and hasattr(args[0].green, '__call__') and hasattr(args[0].blue, '__call__') and hasattr(args[0].alpha, '__call__'):
                    r, g, b, a = r.red(), r.green(), r.blue(), r.alpha()
                else:
                    r, g, b, a = r.red, r.green, r.blue, r.alpha

            else:
                if hasattr(args[0].red, '__call__') and hasattr(args[0].green, '__call__') and hasattr(args[0].blue, '__call__'):
                    r, g, b = r.red(), r.green(), r.blue()
                else:
                    r, g, b = r.red, r.green, r.blue

        # Try other color attributes
        elif hasattr(args[0], 'r') and hasattr(args[0], 'g') and hasattr(args[0], 'b'):
            if hasattr(args[0], 'a'):
                if hasattr(args[0].r, '__call__') and hasattr(args[0].g, '__call__') and hasattr(args[0].b, '__call__') and hasattr(args[0].a, '__call__'):
                    r, g, b, a = r.r(), r.g(), r.b(), r.a()
                else:
                    r, g, b, a = r.r, r.g, r.b, r.a
            else:
                if hasattr(args[0].r, '__call__') and hasattr(args[0].g, '__call__') and hasattr(args[0].b, '__call__'):
                    r, g, b = r.r(), r.g(), r.b()
                else:
                    r, g, b = r.r, r.g, r.b

        # We've been given seperate color parameters
        elif len(args) in (3, 4):
            assert isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float))

            # We've been given an OpenGL color
            if all([isinstance(i, float) and i >= -1 and i <= 1 for i in args]):
                if len(args) == 3:
                    r, g, b = [translate(i, -1, 1, 0, 255) for i in args]
                else:
                    r, g, b, a = [translate(i, -1, 1, 0, 255) for i in args]

            # Otherwise, interpret them as ints between 0 and 255
            if len(args) == 3:
                r, g, b = args
            else:
                r, g, b, a = args
        elif len(args) not in (3, 4):
            raise TypeError(f'Incorrect number ({len(args)}) of color parameters given. Please give either 3 or 4 parameters')

    # Now handle keyword args. If a keyword arg is specified, it should override other methods
    r = r if ((_r := (kwargs.get('r') or kwargs.get('red'))) is None) else _r
    g = g if ((_g := (kwargs.get('g') or kwargs.get('green'))) is None) else _g
    b = b if ((_b := (kwargs.get('b') or kwargs.get('blue'))) is None) else _b
    a = a if ((_a := (kwargs.get('a') or kwargs.get('alpha'))) is None) else _a

    # _r, _g, _b, _a = (
    #     (kwargs.get('r') or kwargs.get('red')),
    #     (kwargs.get('g') or kwargs.get('green')),
    #     (kwargs.get('b') or kwargs.get('blue')),
    #     (kwargs.get('a') or kwargs.get('alpha')),
    # )
    # We've been given an OpenGL color
    # if all([isinstance(i, float) and i >= -1 and i <= 1 for i in colors]):
    #     # if all(colors[:3]):
    #     r = r if _r is None else r
    #     r = r if _r is None else r
    #     if colors[3] is None:
    #         r, g, b = [translate(i, -1, 1, 0, 255) for i in colors]
    #     else:
    #         r, g, b, a = [translate(i, -1, 1, 0, 255) for i in colors]


    if r is None or b is None or g is None:
        # We're not sure how to interpret the parameters given
        raise TypeError(f'Unsure how to interpret the parameters given (or no parameters were given)')

    # Make sure they're the right type
    r, g, b, a = [int(i) for i in (r, g, b, a)]

    # ─── NOW WE RETURN ──────────────────────────────────────────────────────────────
    # We now have r, g, b and a (255 by default) between 0 and 255
    match rtn.lower():
        case 'html':
            return f'#{r:02x}{g:02x}{b:02x}'
        case 'rgb':
            return r, g, b
        case 'rgba':
            return r, g, b, a
        case 'hsv':
            return rgb_to_hsv(*[translate(i, 0, 255, 0, 1) for i in (r, g, b)])
        case 'hls':
            return rgb_to_hls(*[translate(i, 0, 255, 0, 1) for i in (r, g, b)])
        case 'yiq':
            return rgb_to_yiq(*[translate(i, 0, 255, 0, 1) for i in (r, g, b)])
        case 'opengl':
            # Does OpenGL include alpha?
            # return [translate(i, 0, 255, -1, 1) for i in (r, g, b)]
            return [translate(i, 0, 255, -1, 1) for i in (r, g, b, a)]
        case _:
            raise TypeError(f"Invalid return type given. Options are `html`, `rgb`, `rgba`, `opengl`")

def darken(amt, *args) -> Tuple['r', 'g', 'b']:
    """ Returns the given color, but darkened. Make amount negative to lighten
        NOTE: If you pass alpha to this function it will still work, but it
            won't return it.
        NOTE: If you pass OpenGL colors to this, it will work, but `amt` still
            has to be within 0-255
    """
    return tuple(i - amt for i in parse_color(*args))

def darken(amt, *args) -> Tuple['r', 'g', 'b']:
    """ Returns the given color, but lightened. Make amount negative to darken
        NOTE: If you pass alpha to this function it will still work, but it
            won't return it.
        NOTE: If you pass OpenGL colors to this, it will work, but `amt` still
            has to be within 0-255
    """
    return tuple(i + amt for i in parse_color(*args))

def invert_color(*args, **kwargs) -> Tuple['r', 'g', 'b']:
    """ Inverts a color.
        NOTE: If you pass alpha to this function it will still work, but it
            won't return it.
    """
    return tuple(255 - i for i in parse_color(*args, rtn, **kwargs))
