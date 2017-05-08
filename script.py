import mdl
from display import *
from matrix import *
from draw import *
from matrixOps import *
from transformOps import *


def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]

    print "UGE: Parsing Started"
    p = mdl.parseFile(filename)
    print "UGE: Parsing Completed"

    if p:
        (commands, symbols) = p
    else:
        print "UGE Error: Parsing Failed"
        return

    screen = new_screen()
    tStack = [createIdentity(4)]
    # blank is used as a starting point for transformations
    blank = createIdentity(4)
    # step = 0.1  # Allow setting a global step?

    for command in commands:

        # -- STACK COMMANDS -- #

        if command[0] == "push":
            tStack.append(tStack[-1][:])

        elif command[0] == "pop":
            tStack.pop()
            if len(tStack) == 0:
                print "UGE Warning: Transformation stack is empty"

        # -- TRANSFORMATION COMMANDS -- #

        elif command[0] == "scale":
            if len(tStack) == 0:
                print "UGE Error: scale command can't be applied to empty stack"
                print "\t Failing command: " + " ".join(command)
            tMat = scale(blank, float(
                command[1]), float(command[2]), float(command[3]))
            tStack[-1] = multiply(tStack[-1], tMat)

        elif command[0] == "move":
            if len(tStack) == 0:
                print "UGE Error: move command can't be applied to empty stack"
                print "\t Failing command: " + " ".join(command)
            tMat = translate(blank, float(
                command[1]), float(command[2]), float(command[3]))
            tStack[-1] = multiply(tStack[-1], tMat)

        elif command[0] == "rotate":
            if len(tStack) == 0:
                print "UGE Error: rotate command can't be applied to empty stack"
                print "\t Failing command: " + " ".join(command)
            tMat = scale(blank, float(
                command[1]), float(command[2]))
            tStack[-1] = multiply(tStack[-1], tMat)

        # -- 2D SHAPE COMMANDS -- #

        elif command[0] == "line":
            points = []
            add_edge(points, [int(args[0]), int(args[1]), int(args[
                     2])], [int(args[3]), int(args[4]), int(args[5])])
            points = multiply(tStack[-1], points)
            draw_lines(points, screen, color)

        elif command[0] == "circle":
            points = []
            add_circle(points, int(args[0]), int(args[1]),
                       int(args[2]), int(args[3]), 1000)
            points = multiply(tStack[-1], points)
            draw_points(points, screen, color)

        elif command[0] == "bezier":
            points = []
            add_bezier(points, int(args[0]), int(args[1]),
                       int(args[2]), int(args[3]), int(args[4]),
                       int(args[5]), int(args[6]), int(args[7]), 1000)
            points = multiply(tStack[-1], points)
            draw_points(points, screen, color)

        elif command[0] == "hermite":
            points = []
            add_hermite(points, int(args[0]), int(args[1]),
                        int(args[2]), int(args[3]), int(args[4]),
                        int(args[5]), int(args[6]), int(args[7]), 1000)
            points = multiply(tStack[-1], points)
            draw_points(points, screen, color)

        # -- 3D SHAPE COMMANDS -- #

    elif command[0] == "box":
        polygons = []
        add_box(polygons, int(args[0]), int(args[1]),
                int(args[2]), int(args[3]), int(args[4]),
                int(args[5]))
        polygons = multiply(tStack[-1], polygons)
        draw_polygons(polygons, screen, color)

    elif command[0] == "sphere":
        polygons = []
        add_sphere(polygons, int(args[0]), int(args[1]),
                   int(args[2]), int(args[3]), 20)  # adjust steps
        polygons = multiply(tStack[-1], polygons)
        draw_polygons(polygons, screen, color)

    elif command[0] == "torus":
        polygons = []
        add_torus(polygons, int(args[0]), int(args[1]),
                  int(args[2]), int(args[3]), int(args[4]), 20)
        polygons = multiply(tStack[-1], polygons)
        draw_polygons(polygons, screen, color)
