from Cope.sympy import *


def test_catagorize():
    assert catagorize(x**2) == ['polynomial', 'rational', 'quadratic', 'power']
    assert catagorize(sqrt(x)) == ['root', 'power']
    assert catagorize(x**3) == ['polynomial', 'rational', 'power']
    assert catagorize(sqrt(3*x + 1)) == []
    assert catagorize(x**3 - 3*x + 2) == ['polynomial', 'rational']
    assert catagorize((x - 1)**2) == ['polynomial', 'rational', 'quadratic']
    assert catagorize((2*x + 3)/(x**2 + 1)) == ['rational']
    assert catagorize(5**x) == ['exponential']
