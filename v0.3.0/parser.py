from display import *
from matrix import *
from draw import *
from transformOps import *
from matrixOps import *
import time


"""
Goes through the file named filename and performs all of the actions
    listed in that file.

The file follows the following format:
    Every command is a single word that takes up a line
    Any command that requires arguments must have those arguments
        in the 2nd line, separated by spaces.

The commands are as follows:
    scale: create a scale matrix,
        then applies the transformation to the top of the transform stack
        - takes 3 args (sx, sy, sz)
    move: create a translation matrix,
        then applies the transformation to the top of the transform stack
        - takes 3 args (tx, ty, tz)
    rotate: create a rotation matrix,
        then applies the transformation to the top of the transform stack
        - takes 2 args (axis, theta); axis should be x, y or z

    push: pushes a copy of the matrix currently topping the stack,
        onto the stack
    pop: removes the matrix currently topping the transform stack

    line: calcs points for a line, transforms by the top of the stack,
        and draws it to the screen
        - takes 6 args (x0, y0, z0, x1, y1, z1)

    circle: calcs points for a circle, transforms by the top of the stack,
        and draws it to the screen
        - takes 4 args (cx, cy, cz, r)
    bezier: calcs points for a bezier, transforms by the top of the stack,
        and draws it to the screen
        - takes 8 args (x0, y0, x1, y1, x2, y2, x3, y3)
    hermite: calcs points for a hermite, transforms by the top of the stack,
        and draws it to the screen
        - takes 8 args (x0, y0, x1, y1, rx0, ry0, rx1, ry1)

    box: calc polygons for a box, transforms by the top of the stack,
        and draws it to the screen
        - takes 6 args (x, y, z, width, height, depth)
    sphere: calc polygons for a sphere, transforms by the top of the stack,
        and draws it to the screen
        - takes 4 args (x, y, z, radius)
    torus: calc polygons for a torus, transforms by the top of the stack,
        and draws it to the screen
        - takes 5 args (x, y, z, radius1, radius2)

    display: displays the screen with Image Magick
    save: saves the screen to a file -
        - takes 1 argument (filename)
    quit: ends parsing
    #: comment

Deprecated Calls (since stack version):
    ident
    apply

See the file script for an example of the file format
"""

# NOTE: tStack is now created internally, points & polygons are now temp


def parse_file(fname, screen, color):
    with open(fname, 'r') as script:
        keepReading = True

        tStack = [createIdentity(4)]
        # blank is used as a starting point for transformations
        blank = createIdentity(4)

        while keepReading:
            line = script.readline()
            cLine = line.strip("\n").lower()

            # --- TRANSFORMATIONS --- #

            if cLine == "scale":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError(
                        "scale call must be followed by 3 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = scale(blank, float(
                        args[0]), float(args[1]), float(args[2]))
                    tStack[-1] = multiply(tStack[-1], tMat)

            elif cLine == "move":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError("move call must be followed by 3 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = translate(blank, float(
                        args[0]), float(args[1]), float(args[2]))
                    tStack[-1] = multiply(tStack[-1], tMat)

            elif cLine == "rotate":
                args = script.readline().split(" ")
                if len(args) != 2:
                    raise ValueError("rotate call must be followed by 2 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = rotate(blank, args[0], float(args[1]))
                    tStack[-1] = multiply(tStack[-1], tMat)

            # --- TRANFORMATION STACK --- #

            elif cLine == "push":
                # Shouldn't be followed by any args
                topCopy = tStack[-1][:]
                tStack.append(topCopy)

            elif cLine == "pop":
                # Shouldn't be followed by any args
                tStack.pop()
                if len(tStack) == 0:
                    print "Parser Warning: stack is empty"

            # --- LINE --- #

            elif cLine == "line":
                args = script.readline().split(" ")
                if len(args) != 6:
                    raise ValueError("line call must be followed by 6 args")
                else:
                    points = []
                    add_edge(points, [int(args[0]), int(args[1]), int(args[
                             2])], [int(args[3]), int(args[4]), int(args[5])])
                    points = multiply(tStack[-1], points)
                    draw_lines(points, screen, color)

            # --- CURVES --- #

            elif cLine == "circle":
                args = script.readline().split(" ")
                if len(args) != 4:
                    raise ValueError("circle call must be followed by 4 args")
                else:
                    points = []
                    add_circle(points, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), 1000)
                    points = multiply(tStack[-1], points)
                    draw_points(points, screen, color)

            elif cLine == "bezier":
                args = script.readline().split(" ")
                if len(args) != 8:
                    raise ValueError("bezier call must be followed by 8 args")
                else:
                    points = []
                    add_bezier(points, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), int(args[4]),
                               int(args[5]), int(args[6]), int(args[7]), 1000)
                    points = multiply(tStack[-1], points)
                    draw_points(points, screen, color)

            elif cLine == "hermite":
                args = script.readline().split(" ")
                if len(args) != 8:
                    raise ValueError("hermite call must be followed by 8 args")
                else:
                    points = []
                    add_hermite(points, int(args[0]), int(args[1]),
                                int(args[2]), int(args[3]), int(args[4]),
                                int(args[5]), int(args[6]), int(args[7]), 1000)
                    points = multiply(tStack[-1], points)
                    draw_points(points, screen, color)

            # --- 3D SHAPES --- #

            elif cLine == "box":
                args = script.readline().split(" ")
                if len(args) != 6:
                    raise ValueError("box call must be followed by 6 args")
                else:
                    polygons = []
                    add_box(polygons, int(args[0]), int(args[1]),
                            int(args[2]), int(args[3]), int(args[4]),
                            int(args[5]))
                    polygons = multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

            elif cLine == "sphere":
                args = script.readline().split(" ")
                if len(args) != 4:
                    raise ValueError("sphere call must be followed by 4 args")
                else:
                    polygons = []
                    add_sphere(polygons, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), 20)  # adjust steps
                    polygons = multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

            elif cLine == "torus":
                args = script.readline().split(" ")
                if len(args) != 5:
                    raise ValueError("torus call must be followed by 5 args")
                else:
                    polygons = []
                    add_torus(polygons, int(args[0]), int(args[1]),
                              int(args[2]), int(args[3]), int(args[4]), 20)
                    polygons = multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

            # --- COLOR CMDS --- #

            elif cLine == "color":
                # WARNING: this call is likely UNSUPPORTED by other programs
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError("color call must be followed by 3 args")
                else:
                    color = [args[0], args[1], args[2]]

            # --- IMAGE CMDS --- #

            elif cLine == "display":
                # drawing in "display" call has been deprecated with stack use
                display(screen)
                time.sleep(0.5)

            elif cLine == "clear":
                # resetting matrices in "clear" call deprecated with stack use
                clear_screen(screen)

            elif cLine == "save":
                args = script.readline().split(" ")
                if len(args) != 1:
                    raise ValueError("save call must be followed by 1 arg")
                else:
                    # drawing in "save" call has been deprecated with stack use
                    save_extension(screen, args[0])

            elif cLine.startswith("#"):
                # This is a comment
                pass

            elif cLine == "quit":
                keepReading = False
            elif line == "\n":  # Blank line
                pass
            elif line == "":  # End of file
                keepReading = False
            else:
                raise TypeError("Script command unrecognized: " + cLine)
