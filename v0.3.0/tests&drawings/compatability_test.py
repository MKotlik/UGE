from display import *
from draw import *
from parser import *
from matrix import *
from curveDraw import *
import matrixOps

# TODO: Fix EdgeMatrix implementation & make it simpler
# TODO: Switch to using matrxOps fully instead of matrix.py
# TODO: Switch to using my draw.py instead of DW's

screen = new_screen()
color = [0, 255, 0]
edges = []
transform = new_matrix()

# parse_file('script', edges, transform, screen, color)

"""
add_circle(edges, 250, 250, 0, 200, 1000)
draw_lines(edges, screen, color)
display(screen)
"""

print "Matrix operations comparison"
points = [[1, 1, 0, 1], [24, 36, 0, 1], [24, 36, 0, 1], [40, 100, 0, 1],
          [40, 100, 0, 1], [68, 289, 0, 1], [68, 289, 0, 1], [80, 400, 0, 1]]
print "matrixops print"
matrixOps.printM(points)
print "matrix.py print"
print_matrix(points)
print "=============="

print "basic multiplication test"
multiplicand = [[2, -3, 4, 1], [5, 0, 1, 8], [-12, 12, 0.5, 10], [2, 3, 2, 3]]
product1 = matrixOps.matrixMult(multiplicand, points)
matrixOps.printM(product1)
print "--------------"
product2 = points[:]
matrix_mult(multiplicand, product2)
matrixOps.printM(product2)
print "The products are equal: " + str(product1 == product2)
print "=============="

print "edge and point tests"
empty1 = new_matrix()
matrixOps.printM(empty1)
add_edge(empty1, 1, 2, 3, -1, -2, -3)
add_point(empty1, 4, 5, 6)
add_point(empty1, -4, -5, -6)
matrixOps.printM(empty1)
