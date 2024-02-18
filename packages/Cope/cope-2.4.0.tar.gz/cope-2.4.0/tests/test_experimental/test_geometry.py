from os.path import join, dirname; import sys; sys.path.append(join(dirname( __file__ ), '..'))
from Cope.experimental.geometry import *

# def test_absdeg():
#     absdeg()

# def test_absrad():
#     absrad()

# def test_dist():
#     dist()

# def test_normalize2rad():
#     normalize2rad()

# def test_normalize2deg():
#     normalize2deg()

# def test_constrainToUpperQuadrants():
#     constrainToUpperQuadrants()

# def test_negPow():
#     negPow()

# from sympy import *
# def test_round2():

#     debug(round2(8.3235))
#     debug(round2(8.3235, 2))
#     debug(round2(83498.3235, 2))
#     debug(round2(Integer(432)))
#     debug(round2(Float(432.543534234)))
#     debug(round2(Float(432.543534234), 5))
#     debug(round2(Float(432.543534234), 1))
#     debug(round2(Float(432.543534234), 0))
#     debug(round2(Float(432.543534234), scinot=3))
#     debug(round2(pi))
#     debug(round2(pi, tostr=False))
#     debug(round2(pi, 8))
#     debug(round2(pi, scinot=3))
#     debug(round2(pi, scinot=9))
