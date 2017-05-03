# Tester for Edge Matrix updates
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

from draw import draw_matrix
from display import *
from edgeMatrix import EdgeMatrix
import matrixOps

# Basic matrix math tests
print "==============="
print "Running matrixOps Tests:"
print "+++++++++++++++"
print "Printing matrixA:"
matrixA = [[1, 2], [4, 5], [7, 8]]
matrixOps.printM(matrixA)
print "\n---------------"
print "Printing matrixB:"
matrixB = [[9, 1337, 23], [2, 3, 7]]
matrixOps.printM(matrixB)
print "\n---------------"
print "Testing Scalar Multiplication"
print "3 * matrixA -> matrixC:"
matrixC = matrixOps.multiply(3, matrixA)  # Scalar mult
matrixOps.printM(matrixC)
print "\n---------------"
print "Testing Matrix Multiplication"
print "matrixA * matrixB -> matrixD:"
matrixD = matrixOps.multiply(matrixA, matrixB)  # MatrixMult, should work
matrixOps.printM(matrixD)
print "\n---------------"
print "Testing Matrix Multiplication Errors"
print "matrixB * matrixA -> raise ValueError:"
matrixNo = [[5, 5, 5, 5]]
try:
    matrixE = matrixOps.multiply(matrixNo, matrixA)  # MatrixMult,should except
except ValueError as e:
    print "Caught Error: " + str(e)
print "\n---------------"
print "Testing Identity Matrix Creation"
print "identity for matrixB -> identityB:"
identityB = matrixOps.getIdentity(matrixB)
matrixOps.printM(identityB)
print "\n---------------"
print "Testing Identity Matrix Multiplication"
print "identityB * matrixB -> matrixB:"
matrixF = matrixOps.multiply(identityB, matrixB)
matrixOps.printM(matrixF)
print "==============="


# EdgeMatrix tests
print "==============="
print "Running EdgeMatrix Tests:"
print "+++++++++++++++"
print "Creating empty eM1:"
eM1 = EdgeMatrix()
print eM1
print "\n---------------"
print "Creating eM2 from 2d list:"
pointsList = [[1, 2, 0, 1], [3, 4, 0, 1], [5, 6, 0, 1], [7, 8, 0, 1]]
eM2 = EdgeMatrix(initMatrix=pointsList)
print eM2
print "\n---------------"
print "Creating eM3 from eM2:"
eM3 = EdgeMatrix(prevObj=eM2)
print eM3
print "\n---------------"
print "Adding a point to eM1:"
eM1.addPoint([5, 2743, 23, 2])
print eM1
print "\n---------------"
print "Adding an edge to eM2:"
point1 = [55, 123, 0, 1]
point2 = [250, 250, 0, 1]
eM2.addEdge(point1, point2)
print eM2
print "\n---------------"
"""
print "Drawing from an edge matrix:"
drawList = [[20, 20, 0, 1], [320, 20, 0, 1], [170, 420, 0, 1], [20, 20, 0, 1]]
drawMatrix = EdgeMatrix(drawList)
print drawMatrix
screen = new_screen()
draw_matrix(drawMatrix.getMatrix(), screen, [0, 0, 255])
print "Matrix drawn on screen"
save_ppm(screen, "matrixTest.ppm")
print "Windows Mode: matrix drawing saved as 'matrixTest.ppm'"
# display(screen)
# save_extension(screen, "matrixTest.png")
# print "Linux Mode: matrix drawing saved as 'matrixTest.png'"
eM2.addEdge(point1, point2)
# print "\n---------------"
"""
