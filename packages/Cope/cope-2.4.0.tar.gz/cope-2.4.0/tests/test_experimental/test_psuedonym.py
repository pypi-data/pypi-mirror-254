from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.experimental.Psuedonym import *

def test_Psuedonum():
    return
    yes = Psuedonym('yes', 'ye', 'si', 'indeed')
    debug(yes == 'yes')
    debug(yes == 'ye')
    debug(yes == 'yea')

    no = Psuedonym('no', 'nein', 'NOT', caseSensitive=True)
    debug(no == 'no')
    debug(no == 'Nein')
    debug(no == 'nein')
    debug(no == 'not')

    debug(no)
