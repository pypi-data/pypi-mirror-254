from .decorators import reprise, untested
from .debugging import debug
from .imports import dependsOnPackage, ensureImported
import sympy as sp
from sympy import Matrix, ImmutableMatrix, latex, sympify, pprint, eye, randMatrix, flatten, sqrt, zeros, Integer, Float
import ezregex as er

def matrix(string, rows=None, cols=None, cp=False, np=False, immutable=False, verbose=False):
    # Parse params
    assert rows is None or cols is None
    if np:
        type_ = _np.array
        # Yes, this is a despicable line of code, I know.
        # All this does is makes a function that casts everything in a nested list to a float
        # The one 2 lines down does the same thing, except it sympifies it instead
        _caster = lambda x: list(map(lambda a: list(map(lambda b: float(b), a)), x))
    else:
        type_ = Matrix if not immutable else ImmutableMatrix
        _caster = _caster = lambda x: list(map(lambda a: list(map(lambda b: sympify(b), a)), x))

    if string.startswith('c'):
        cols = True
        string = string[1:]
    elif string.startswith('r'):
        rows = True
        string = string[1:]
    elif rows is None and cols is None:
        rows = True

    num = er.anyOf(er.optional('-')+er.matchMax(er.anyCharExcept(er.space))+er.space, er.optional('-')+er.optional(r'\.')+er.anything).compile()

    if cols:
        _cols = string.split(';')
        _cols = [num.findall(i) for i in _cols]
        _rows = []
        debug(_cols, active=verbose)
        # Rotate them (make the rows columns)
        # EDIT: Apparently this is called a "transpose", and I couldn've just
        # done Matrix.T instead
        # ...but this works, so I'm not gonna touch it
        for c in range(len(_cols[0])):
            _rows.append([])
            for i in _cols:
                _rows[-1].append(i[c])
        ans = type_(_caster(_rows))
    else:
        _rows = string.split(';')
        debug(_rows, active=verbose)
        ans = type_(_caster([num.findall(i) for i in _rows]))

    if cp:
        from clipboard import copy
        copy(latex(ans))

    return ans

# This doesn't quite work yet, I'll make it general purpose later
def combineMatricies(*mats):
    rtn = mats[0]
    index = 1
    for c in mats[1:]:
        # if cols:
        rtn = rtn.col_insert(index, c)
        index += c.cols
        # elif rows:
        #     rtn = rtn.row_insert(index, c)
        #     index += c.rows - 1
    return rtn

class Space(sp.matrices.matrices.MatrixSubspaces):
    def __init__(self, *bases):
        if len(bases) == 1 and isinstance(bases[0], (list, tuple)):
            self.bases = self.basis = bases[0]
        else:
            self.bases = self.basis = ensureIterable(bases)

    def __contains__(self, mat):
        try:
            return any(Matrix.hstack(*self.bases).LUsolve(mat))
        except (ValueError, ShapeError) as err:
            return False

    def __str__(self):
        return prettyMats(self.bases)

    @property
    def orthogonal_basis(self):
        return Matrix.orthogonalize(*self.basis)

    @property
    def orthonormal_basis(self):
        return Matrix.orthogonalize(*self.basis, normalize=True)

    def orthogonalized(self):
        return Space(self.orthogonal_basis)

    def orthonormalized(self):
        return Space(self.orthonormal_basis)

    def projectionMatrix(self):
        U = combineMatricies(*self.orthonormal_basis)
        return U*U.T

# Because Matrix.columnspace doesn't work how my teacher says it does
def columnspace(M):
    return Space([M.col(pivot) for pivot in M.rref()[1]])

def eigenspaces(mat):
    return {i[0]: Space(i[2]) for i in mat.eigenvects()}

def convert2Equs(mat, vars):
    """ Converts a matrix into the list of equations it represents """
    vars = list(vars)
    assert mat.cols == len(vars), f'Must have exactly 1 variable for each column ({mat.cols} columns, {len(vars)} variables)'
    eqs = []
    for i in range(mat.rows):
        eq = 0
        for cnt, e in enumerate(mat.row(i)):
            eq += e*vars[cnt]
        eqs.append(eq)
    return eqs

def isSimilar(*args):
    debug('This is wrong', clr=-1)
    first = args[0].eigenvals()
    return all(i == first for i in args)

# Sympy method
def steadyState(stochastic, accuracy=10000000000000, verbose=False):
    import numpy as np
    if isinstance(stochastic, np.ndarray):
        stochastic = Matrix(stochastic)
        numpy = True
    else:
        numpy = False
    # Make sure it's a square matrix
    assert stochastic.cols == stochastic.rows, "Stochastic matricies must be square"
    P = stochastic-eye(stochastic.cols)
    # Yes, this is terrible.
    #   This multiplies everything by a big number, then casts it to an int
    #   so the stupid float rounding errors will go away.
    #   We actually shouldn't need to cast it back, because rref will
    #   just descale it for us
    #   I definitely *didn't* just spend all afternoon getting this to work
    if verbose:
        print('P:')
        pprint(P)
    P = Matrix(np.array((P*accuracy).tolist(), dtype=int))
    if verbose:
        print('Cast P:')
        pprint(P)
        print('RREF(P):')
        pprint(P.rref()[0])
    # w = ensureNotIterable(P.nullspace())
    w = [m / sum(flatten(m)) for m in P.nullspace()]
    if verbose:
        print('Answers:')
        pprint(w)
    # I could double check, but re-fixing the rounding errors isn't worth it
    # assert stochastic * ans == ans
    return [(matrix2numpy(ans, dtype=float) if numpy else ans) for ans in w]

@dependsOnPackage('sympy', ('randMatrix', 'flatten', 'Matrix'))
def randMarkovState(rows, balanced=True, np=False):
    cast = matrix2numpy if np else lambda a, **_: a
    if balanced:
        r = randMatrix(rows, 1)
        return cast(r / sum(flatten(r.tolist())), dtype=float)
    else:
        tmp = ([1] + ([0]*(rows-1)))
        shuffle(tmp)
        return cast(Matrix([tmp]).T, dtype=float)

@dependsOnPackage('sympy', 'Matrix')
def isOrthogonal(*vects, innerProduct=None):
    if innerProduct is None:
        innerProduct = Matrix.dot
    return not any([innerProduct(v1, v2) for v2 in vects for v1 in vects if v1 != v2])

# a = matrix('c111')
# b = matrix('c5-2-3')
# c = matrix('c1-10')
# # a and c are, a and b are, b and c are not
# assert isOrthogonal(a, b)
# assert not isOrthogonal(a, b, c)

@dependsOnPackage('sympy', 'sqrt')
def vectorLength(v):
    assert v.cols == 1
    return sqrt(sum([i**2 for i in v]))

def EuclideanDist(u, v):
    return vectorLength(u-v)

@untested
def manhattanDist(a, b):
    assert len(a) == len(b)
    return sum(abs(a[i] - b[i]) for i in range(len(a)))

@untested
def minkowskiDist(a, b, p):
    assert len(a) == len(b)
    return sum([abs(a[i] - b[i])**p for i in range(len(a))])**(1/p)

# assert vectorLength(matrix('c111')) == sqrt(3)

# def project(v, onto) -> '(proj(v), w)':
#     projected = (onto.dot(v) / onto.dot(onto)) * onto
#     return projected, v - projected

# u = matrix('c1-10')
# v = matrix('c5-2-3')
# assert sum(project(v, u), start=matrix('c000')) == v
# assert Matrix.orthogonalize(u, v)[1] == project(v, u)[1]

def orthonormalize(orthogonalSet):
    return [v / vectorLength(v) for v in orthogonalSet]

# alignedV, w = project(v, u)
# assert Matrix.orthogonalize(u, w, normalize=True) == orthonormalize((u, w))

def splitVector(y:'Matrix', W:'Space', innerProduct=None) -> list:
    """ Returns vectors in W which can be linearly combined to get y """
    if innerProduct is None:
        innerProduct = Matrix.dot
    return [(innerProduct(y, u) / innerProduct(u, u))*u for u in W.orthogonal_basis]

# assert splitVector(matrix('c9-7'), Space(matrix('c2-3'), matrix('c64'))) == [matrix('c6-9'), matrix('c32')]
# for _ in range(100):
#     rows = randint(2, 10)
#     v = randMatrix(rows, 1)
#     assert sum(splitVector(v, Space([randMatrix(rows, 1) for _ in range(rows)])), start=zeros(rows, 1)) == v

def project(y:'Matrix', W:'Space', innerProduct=None) -> '(vector in W, vector in W⟂)':
    """ W  = a subspace of R^n we want to describe y with (to get proj_y)
        y  = some y in R^n
        proj_y = a vector in W
        z  = a vector in W⟂ (W perp) """
    if innerProduct is None:
        innerProduct = Matrix.dot
    proj_y = sum(splitVector(y, W, innerProduct), start=zeros(y.rows, 1))
    z = y - proj_y
    # While this should be true, rounding errors.
    # assert proj_y + z == y
    return proj_y, z

# assert project(matrix('c123-1'), Space((matrix('c1111'), matrix('c1-11-1')))) == \
#     (Matrix([
#     [  2],
#     [1/2],
#     [  2],
#     [1/2]]),
#     Matrix([
#     [  -1],
#     [ 3/2],
#     [   1],
#     [-3/2]]))

def normalizePercentage(p, error='Percentage is of the wrong type (int or float expected)'):
    if isinstance(p, (int, Integer)):
        return p / 100
    elif isinstance(p, (float, Float)):
        return p
    elif isinstance(p, bool):
        if p is True:
            return 1.
        else:
            return 0.
    else:
        if error is not None:
            raise TypeError(error)

# Eq(matrix('4-17-4;-53-51;7-802;6-807', cols=1)*matrix('x_1 x_2 x_3', cols=1), matrix('6-80-7', cols=1))
# debug(matrix('x_1 x_2 x_3 ', cols=1))
# debug(matrix('1 -2 10 '))
# debug(matrix('c1 -2 10 '))
# debug(matrix('c.1 -2 10 '))
# debug(matrix('c.1 -.2 10 '))
# debug(matrix('20;02' ,verbose=1))
# debug(matrix('c1-3' ,verbose=1))
# debug(matrix('c2-6'))
# debug(matrix('20;02') )
# debug(matrix('cab')  )
#  Matrix([[2*var('a')], [2*var('b')]])
# debug(matrix('4-17-4;-53-51;7-802;6-807', cols=1))
