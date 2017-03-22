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

parse_file('script', edges, transform, screen, color)

"""
add_circle(edges, 250, 250, 0, 200, 1000)
draw_lines(edges, screen, color)
display(screen)
"""
