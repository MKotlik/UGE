import mdl
from display import *
from matrix import *
from draw import *
from matrixOps import *
from transformOps import *
import time

# NOTE: Apparently curves are unsupported in MDL?


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

    # Constants/variables will be saved in a dict

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
                break
            tMat = scale(blank, float(
                command[1]), float(command[2]), float(command[3]))
            tStack[-1] = multiply(tStack[-1], tMat)

        elif command[0] == "move":
            if len(tStack) == 0:
                print "UGE Error: move command can't be applied to empty stack"
                print "\t Failing command: " + " ".join(command)
                break
            tMat = translate(blank, float(
                command[1]), float(command[2]), float(command[3]))
            tStack[-1] = multiply(tStack[-1], tMat)

        elif command[0] == "rotate":
            if len(tStack) == 0:
                print "UGE Error: rotate command can't be applied to empty stack"
                print "\t Failing command: " + " ".join(command)
                break
            tMat = rotate(blank, command[1], float(command[2]))
            tStack[-1] = multiply(tStack[-1], tMat)

        # -- 2D SHAPE COMMANDS -- #

        elif command[0] == "line":
            points = []
            """
            # Version for constants
            add_edge(points, [int(command[2]), int(command[3]), int(command[
                     4])], [int(command[6]), int(command[7]), int(command[8])])
            """
            add_edge(points, [int(command[1]), int(command[2]), int(command[
                     3])], [int(command[4]), int(command[5]), int(command[6])])
            points = multiply(tStack[-1], points)
            draw_lines(points, screen, color)

        # -- 3D SHAPE COMMANDS -- #

        elif command[0] == "box":
            polygons = []
            """
            # Version for constants
            add_box(polygons, int(command[2]), int(command[3]),
                    int(command[4]), int(command[5]), int(command[6]),
                    int(command[7]))
            """
            add_box(polygons, int(command[1]), int(command[2]),
                    int(command[3]), int(command[4]), int(command[5]),
                    int(command[6]))
            polygons = multiply(tStack[-1], polygons)
            draw_polygons(polygons, screen, color)

        elif command[0] == "sphere":
            polygons = []
            """
            # Version for constants
            add_sphere(polygons, int(command[2]), int(command[3]),
                       int(command[4]), int(command[5]), 20)  # adjust steps
            """
            add_sphere(polygons, int(command[1]), int(command[2]),
                       int(command[3]), int(command[4]), 20)  # adjust steps
            polygons = multiply(tStack[-1], polygons)
            draw_polygons(polygons, screen, color)

        elif command[0] == "torus":
            polygons = []
            """
            # Version for constants
            add_torus(polygons, int(command[2]), int(command[3]),
                      int(command[4]), int(command[5]), int(command[6]), 20)
            """
            add_torus(polygons, int(command[1]), int(command[2]),
                      int(command[3]), int(command[4]), int(command[5]), 20)
            polygons = multiply(tStack[-1], polygons)
            draw_polygons(polygons, screen, color)

        # -- IMAGE COMMANDS -- #

        elif command[0] == "display":
            display(screen)
            time.sleep(0.5)

        elif command[0] == "save":
            print "UGE: saving image with as " + command[1]
            save_extension(screen, command[1])
