from .imports import dependsOnPackage
from typing import Union

#* My Own Point Classes
@dependsOnPackage('Point', 'Point')
def findClosestXPoint(target, comparatorList, offsetIndex=0):
    """ I've forgotten what *exactly* this does. I think it finds the point in a list of
        points who's x point is closest to the target
    """
    finalDist = 1000000
    result = 0

    # for i in range(len(comparatorList) - offsetIndex):
    for current in comparatorList:
        # current = comparatorList[i + offsetIndex]
        currentDist = abs(target.x - current.x)
        if currentDist < finalDist:
            result = current
            finalDist = currentDist

    return result

@dependsOnPackage('Point', ('Point', 'Pointi', 'Pointf'))
def getPointsAlongLine(p1, p2):
    """ I don't remember what this does. """
    p1 = Pointi(p1)
    p2 = Pointi(p2)

    returnMe = []

    dx = p2.x - p1.x
    dy = p2.y - p1.y

    for x in range(p1.x, p2.x):
        y = p1.y + dy * (x - p1.x) / dx
        returnMe.append(Pointf(x, y))

    return returnMe

@dependsOnPackage('Point', 'Point')
def rotatePoint(p, angle, pivotPoint, radians=False):
    """ This rotates one point around another point a certain amount, and returns it's new position """
    if not radians:
        angle = math.radians(angle)
    # p -= pivotPoint
    # tmp = pygame.math.Vector2(p.data()).normalize().rotate(amount)
    # return Pointf(tmp.x, tmp.y) + pivotPoint

    dx = p.x - pivotPoint.x
    dy = p.y - pivotPoint.y
    newX = dx * math.cos(angle) - dy * math.sin(angle) + pivotPoint.x
    newY = dx * math.sin(angle) + dy * math.cos(angle) + pivotPoint.y

    return Pointf(newX, newY)

@dependsOnPackage('Point', 'Point')
def getMidPoint(p1, p2):
    """ Returns the halfway point between 2 given points """
    assert type(p1) == type(p2)
    # return Pointf((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)
    return p1._initCopy((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

@dependsOnPackage('Point', 'Point')
def findClosestPoint(target, comparatorList):
    """ Finds the closest point in the list to what it's given"""
    finalDist = 1000000

    for i in comparatorList:
        current = getDist(target, i)
        if current < finalDist:
            finalDist = current

    return finalDist

@dependsOnPackage('Point', 'Point')
def collidePoint(topLeft: 'Point', size: Union[tuple, list, 'Size'], target, inclusive=True):
    """ Returns true if target is within the rectangle given by topLeft and size """
    return isBetween(target.x, topLeft.x, size[0], beginInclusive=inclusive, endInclusive=inclusive) and \
           isBetween(target.y, topLeft.y, size[1], beginInclusive=inclusive, endInclusive=inclusive)

@dependsOnPackage('Point', 'Point')
def getPointDist(a: 'Point', b: 'Point'):
    return math.sqrt(((b.x - a.x)**2) + ((b.y - a.y)**2))
