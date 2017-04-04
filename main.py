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

"""
add_torus(edges, 250, 250, 0, 25, 100, 50)
edges = rotate(edges, "x", 90)
edges = scale(edges, 1.5, 1.5, 1.5)
edges = translate(edges, -100, 100, 0)
draw_polygons(edges, screen, color)
display(screen)
"""


add_box_surface(edges, 0, 0, 0, 200, 100, 400)
edges = rotate(edges, "z", 180)
edges = rotate(edges, "x", 20)
edges = rotate(edges, "y", 20)
edges = translate(edges, 450, 200, 0)
draw_polygons(edges, screen, color)
display(screen)


"""
add_circle(edges, 250, 250, 0, 200, 1000)
draw_lines(edges, screen, color)
display(screen)
"""
