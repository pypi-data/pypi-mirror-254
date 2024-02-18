from os.path import join, dirname; import sys; sys.path.append(join(dirname(__file__), '..'))
from Cope.experimental.colors import *
from PyQt6.QtGui import QColor

def test_parse_color():
    # Test parameters
    # Positional parameters
    assert parse_color(255, 255, 255, 255) == (255, 255, 255)
    assert parse_color(255, 255, 255) == (255, 255, 255)
    # tuple or list
    assert parse_color((255, 255, 255, 255)) == (255, 255, 255)
    assert parse_color((255, 255, 255)) == (255, 255, 255)
    # Keyword parameters/dict
    assert parse_color(r=255, g=255, b=255, a=255) == (255, 255, 255)
    assert parse_color({'r':255, 'g':255, 'b':255, 'a':255}) == (255, 255, 255)
    assert parse_color(red=255, green=255, blue=255, alpha=255) == (255, 255, 255)
    assert parse_color({'red':255, 'green':255, 'blue':255, 'alpha':255}) == (255, 255, 255)
    # OpenGL style colors (between -1 and 1)
    assert parse_color(1., 1., 1.) == (255, 255, 255)
    assert parse_color((1., 1., 1.)) == (255, 255, 255)
    # Hex colors
    assert parse_color('#FFFFFF') == (255, 255, 255)
    assert parse_color('#ffffff') == (255, 255, 255)
    # Named colors
    assert parse_color('white') == (255, 255, 255)
    # "Random" distinct colors
    assert len(parse_color(1)) == 3
    # Anything that has r, g, b attributes or red, green, blue attributes (callable or not)
    assert parse_color(QColor(255, 255, 255)) == (255, 255, 255)

    # 'html'
    assert parse_color(255, 255, 255, rtn='html') == '#FFFFFF'
    # 'rgb'
    assert parse_color(255, 255, 255, rtn='rgb') == (255, 255, 255)
    # 'rgba'
    assert parse_color(255, 255, 255, rtn='rgba') == (255, 255, 255, 255)
    # 'opengl'
    assert parse_color(255, 255, 255, rtn='opengl') == (1., 1., 1., 1.)
    # 'hsv'
    assert parse_color(255, 255, 255, rtn='hsv') == (0., 0., 1.)
    # 'hls'
    assert parse_color(255, 255, 255, rtn='hls') == (0., 1., 0.)
    # 'yiq'
    assert parse_color(255, 255, 255, rtn='yiq') == rgb_to_yiq(1, 1, 1,)

test_parse_color()

# def test_darken():
#     darken()

# def test_lighten():
#     lighten()

# def test_invert_color():
#     invertColor()
