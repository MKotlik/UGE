# TransformOps Module
# UGE - Computer Graphics
# Misha (Mikhail Kotlik)

import matrixOps

"""
Matrices look like:
matrixA[col (index of sublist), row (index within sublist)]
in terms of the edge matrix: matrixA[position][point]

We are not modifying in place; we are returning a new matrix
"""


def translate(matrix, a, b, c):
    tMat = matrixOps.createIdentity(4)
    tMat[3][0] = a
    tMat[3][1] = b
    tMat[3][2] = c
    return matrixOps.multiply(tMat, matrix)


# CHECK THAT I CAN MULTIPLY BY 4x4 IDENT MATRIX
def scale(matrix, sX, sY, sZ):
    tMat = matrixOps.createIdentity(4)
    tMat[0][0] = a
    tMat[1][1] = b
    tMat[2][2] = c
    return matrixOps.multiply(tMat, matrix)


def rotate(matrix, axis, theta):
    """Based on axis, apply different rotation type"""
    if axis.lower() == "z":
        return rotateZ(matrix, theta)
    elif axis.lower() == "y":
        return rotateY(matrix, theta)
    elif axis.lower() == "x":
        return rotateX(matrix, theta)
    else:
        raise ValueError("transformOps.rotate() accepts X, Y, or Z axes")


def rotateZ(matrix, theta):
    rAngle = theta * math.pi / 180.0
    tMat = matrixOps.createIdentity(4)
    tMat[0][0] = math.cos(rAngle)
    tMat[1][0] = -1 * math.sin(rAngle)
    tMat[0][1] = math.sin(rAngle)
    tMat[1][1] = math.cos(rAngle)
    return matrixOps.multiply(tMat, matrix)


def rotateX(matrix, theta):
    rAngle = theta * math.pi / 180.0
    tMat = matrixOps.createIdentity(4)
    tMat[1][1] = math.cos(rAngle)
    tMat[2][1] = -1 * math.sin(rAngle)
    tMat[1][2] = math.sin(rAngle)
    tMat[2][2] = math.cos(rAngle)
    return matrixOps.multiply(tMat, matrix)


def rotateY(matrix, theta):
    rAngle = theta * math.pi / 180.0
    tMat = matrixOps.createIdentity(4)
    tMat[0][0] = math.cos(rAngle)
    tMat[2][0] = math.sin(rAngle)
    tMat[1][2] = -1 * math.sin(rAngle)
    tMat[2][2] = math.cos(rAngle)
    return matrixOps.multiply(tMat, matrix)
