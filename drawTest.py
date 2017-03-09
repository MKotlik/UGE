from display import *
from draw import *
from matrix import *
from transformOps import *
import matrixOps

screen = new_screen()
bColor = [0, 0, 255]

matrix1 = new_matrix()
add_edge(matrix1, 50, 50, 0, 150, 50, 0)
add_edge(matrix1, 50, 150, 0, 150, 150, 0)
add_edge(matrix1, 50, 50, 0, 50, 150, 0)
add_edge(matrix1, 150, 50, 0, 150, 150, 0)
print_matrix(matrix1)

print "Drawing matrix1"
draw_lines(matrix1, screen, bColor)
display(screen)
print "--------------------"

print "creating transformation matrix"
transformer = matrixOps.createIdentity(4)
transformer = rotateZ(transformer, 30)
# transformer = scale(transformer, 2, 2, 2)
transformer = translate(transformer, 150, 150, 0)
print_matrix(transformer)

print "tranforming matrix1 using transformation matrix"
shiftedMat = matrixOps.multiply(transformer, matrix1)
shiftedInts = matrixOps.toIntMatrix(shiftedMat)
matrixOps.printM(shiftedInts)

print "drawing the shifted matrix"
gColor = [0, 255, 0]
draw_lines(shiftedInts, screen, gColor)
display(screen)
print "--------------------"
