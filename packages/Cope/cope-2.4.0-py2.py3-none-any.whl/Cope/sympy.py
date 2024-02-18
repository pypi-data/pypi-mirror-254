"""
A bunch of functions and classes extending the sympy library
"""
try:
    from sympy import *
except: pass
else:
    def categorize(expr:Expr, unknown:Symbol=Symbol('x')) -> list:
        """ Catagorize `expr` as a function of any of:
                polynomial
                rational
                quadratic
                root
                power
                exponential
            Returns a list of strings of the types it is
            NOTE: `expr` must be a sympy expression, and only have one unknown in it.
            Results for expressions with more than 1 unknown is undefined.
        """
        rtn = []
        # Polynomial
        if expr.is_polynomial():
            rtn.append('polynomial')
        # Rational
        if expr.is_rational_function():
            rtn.append('rational')
        # Quadratic
        if (p := expr.as_poly()) is not None and p.degree() == 2:
            rtn.append('quadratic')
        # Root
        if isinstance(expr, Pow) and isinstance(expr.exp, Rational) and int(expr.exp) != expr.exp and expr.base == unknown:
            rtn.append('root')
        # Power
        parts = expr.as_coeff_Mul()
        if parts[0].is_real and isinstance(parts[1], Pow) and parts[1].base == unknown and parts[1].exp.is_real:
            rtn.append('power')
        # Exponential
        if isinstance(expr, Pow) and isinstance(expr.base, Rational) and expr.exp == unknown:
            rtn.append('exponential')
        return rtn
