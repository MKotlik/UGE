from display import *
from draw import *
from parser import *
from matrix import *
import matrixOps
from transformOps import *


screen = new_screen()
color = [0, 255, 0]
edges = []
transform = new_matrix()

# parse_file('script', edges, transform, screen, color)

add_sphere(edges, 250, 250, 0, 200, 30)
draw_polygons(edges, screen, color)
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
