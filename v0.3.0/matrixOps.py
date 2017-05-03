# MatrixOps Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

from pprint import pprint

"""
Matrices look like:
matrixA[col (index of sublist), row (index within sublist)]
in terms of the edge matrix: matrixA[position][point]

We are not modifying in place; we are returning a new matrix
"""


# Returns string representation of matrix
# Table will be padded and columns separated by pipes
def toString(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return str(matrix)
    else:
        obj_str = ""
        rowList = ["|"] * len(matrix[0])
        for col in matrix:
            # Calculate maxLen for padding
            maxLen = 0
            for rowEl in col:
                curLen = len(str(rowEl))
                if curLen > maxLen:
                    maxLen = curLen
            # Create padding formatting string
            padStr = "{:>" + str(maxLen) + "}"
            # Add each rowEl to respective rowStr, w/ padding
            for rowN in range(len(matrix[0])):
                rowList[rowN] += padStr.format(col[rowN]) + " | "
        for row in rowList:
            obj_str += row[:-1] + "\n"
        return obj_str[:-1]


# Prints the matrix
def printM(matrix):
    print toString(matrix)


# Converts matrix to an int matrix, rounds all floats
def toIntMatrix(matrix):
    intMatrix = []
    for col in matrix:
        intCol = []
        for rowCell in col:
            intCol.append(int(round(rowCell)))
        intMatrix.append(intCol)
    return intMatrix


# ++++++++++++++++++++++++ #
# MULTIPLICATION FUNCTIONS #
# ++++++++++++++++++++++++ #


# General matrix multiplication (determines operands):
def multiply(operandA, matrix):
    if type(operandA) is int:
        return scalarMult(operandA, matrix)
    elif type(operandA) is float:
        return scalarMult(operandA, matrix)
    elif type(operandA) is list:
        return matrixMult(operandA, matrix)
    elif type(operandA) is long:
        return scalarMult(operandA, matrix)
    else:
        raise TypeError("matrixOps.multiply() takes a matrix or number, "
                        "followed by a matrix")


# Scalar Multiplication
def scalarMult(scalar, matrix):
    # Check that matrix isn't empty
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        raise ValueError(
            "matrixOps.multiply() cannot multiply an empty matrix")
    modMatrix = []
    for colEl in matrix:
        newCol = []
        for rowEl in colEl:
            newCol.append(rowEl * scalar)
        modMatrix.append(newCol)
    return modMatrix


# Matrix Multiplication
def matrixMult(matrixA, matrixB):
    # Check that both matrices are not empty
    if (len(matrixA) == 0 or len(matrixA[0]) == 0 or
            len(matrixB) == 0 or len(matrixB[0]) == 0):
        raise ValueError(
            "matrixOps.multiply() cannot multiply an empty matrix")
    # Check that numbers of cols in A matches number of rows in B
    if (len(matrixA) != len(matrixB[0])):
        raise ValueError("matrixOps.multiply() matrix multiplication "
                         "requires that num cols in 1 matrix matches num "
                         "rows in 2nd matrix")
    # Create new matrix, and fill it with multiplication product
    product = []
    # Iterate over dimensions of product matrix (thru each col, thru each cell)
    # Dimensions: num cols in B * num rows in A
    for colN in range(len(matrixB)):
        col = []  # Create new column to fill
        for rowN in range(len(matrixA[0])):
            cellProd = 0
            # Iterate over els to be multiplied, equal to num cols in A
            for elNum in range(len(matrixA)):
                cellProd += matrixA[elNum][rowN] * matrixB[colN][elNum]
            col.append(cellProd)
        product.append(col)
    return product


# ++++++++++++++++++ #
# IDENTITY FUNCTIONS #
# ++++++++++++++++++ #


# By default, gets left identity matrix
def getIdentity(matrix):
    try:
        return getLeftIdentity(matrix)
    except ValueError:
        raise ValueError("matrixOps.getIdentity() cannot create identity "
                         "for an empty matrix")


# Create the left identity matrix for a given matrix
# Aka the identity matrix that would be the left operand
def getLeftIdentity(matrix):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        raise ValueError("matrixOps.getLeftIdentity() cannot create identity "
                         "for an empty matrix")
    # Left identity needs to match num rows in matrix
    return createIdentity(len(matrix[0]))


# Create the right identity matrix for a given matrix
# Aka the identity matrix that would be the right operand
def getRightIdentity(matrix):
    if (len(matrix) == 0 or len(matrix[0]) == 0):
        raise ValueError("matrixOps.getRightIdentity() cannot create identity "
                         "for an empty matrix")
    # Right identity needs to match num cols in matrix
    return createIdentity(len(matrix))


# Creates identity matrix with given dimension
def createIdentity(numEls):
    identity = []
    for colN in range(numEls):
        col = [0] * numEls
        col[colN] = 1
        identity.append(col)
    return identity
