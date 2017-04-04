from display import *
from draw import *
from parser import *
from matrix import *
import matrixOps
from transformOps import *


screen = new_screen()
color = [0, 255, 0]
edges = []  # edge matrix (lines & 2d shapes)
polygons = []  # polygon matrix (3d shapes)
transform = new_matrix()

parse_file('script', edges, polygons, transform, screen, color)


# ++++++++++ #
# TEMP TESTS #
# ++++++++++ #

"""
add_torus(polygons, 250, 250, 0, 25, 100, 50)
polygons = rotate(polygons, "x", 90)
polygons = scale(polygons, 1.5, 1.5, 1.5)
polygons = translate(polygons, -100, 100, 0)
draw_polygons(polygons, screen, color)
display(screen)
"""

"""
add_box_surface(polygons, 0, 0, 0, 200, 100, 400)
polygons = rotate(polygons, "z", 180)
polygons = rotate(polygons, "x", 20)
polygons = rotate(polygons, "y", 20)
polygons = translate(polygons, 450, 200, 0)
draw_polygons(polygons, screen, color)
display(screen)
"""

"""
add_circle(edges, 250, 250, 0, 200, 1000)
draw_lines(edges, screen, color)
display(screen)
"""
