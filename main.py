from display import *
from draw import *
from parser import *
from matrix import *
import matrixOps
from transformOps import *

# TODO: Fix EdgeMatrix implementation & make it simpler
# TODO: Switch to using matrxOps fully instead of matrix.py
# TODO: Switch to using my draw.py instead of DW's

screen = new_screen()
color = [0, 255, 0]
edges = []
transform = new_matrix()

# parse_file('script', edges, transform, screen, color)

generate_sphere(edges, 0, 0, 0, 200, 100)
rotate(edges, "y", 20)
draw_points(edges, screen, color)
display(screen)

"""
add_box(edges, 0, 0, 0, 200, 100, 400)
draw_lines(edges, screen, color)
display(screen)
"""

"""
add_circle(edges, 250, 250, 0, 200, 1000)
draw_lines(edges, screen, color)
display(screen)
"""
