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


def rotate(theta, axis):
    """Based on axis, apply different rotation type"""
    pass


def rotationMatrix(horD, verD, forwardD):
    """Apply changes to the appropriate point pos.s representing directions"""
    pass
