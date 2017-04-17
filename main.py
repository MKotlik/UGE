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
