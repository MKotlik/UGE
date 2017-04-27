from display import *
from matrix import *
from draw import *
from transformOps import *
import matrixOps
import time

# TODO: Update the command list

"""
Goes through the file named filename and performs all of the actions
    listed in that file.

The file follows the following format:
    Every command is a single character that takes up a line
    Any command that requires arguments must have those arguments
        in the 2nd line.

The commands are as follows:
    line: add a line to the edge matrix -
        takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
    scale: create a scale matrix,
        then multiply the transform matrix by the scale matrix -
        takes 3 arguments (sx, sy, sz)
    move: create a translation matrix,
        then multiply the transform matrix by the translation matrix -
        takes 3 arguments (tx, ty, tz)
    rotate: create a rotation matrix,
        then multiply the transform matrix by the rotation matrix -
        takes 2 arguments (axis, theta) axis should be x, y or z
    display: displays the screen with Image Magick
    save: saves the screen to a file -
        takes 1 argument (file name)
    quit: end parsing

Deprecated Calls (since stack version):
    ident
    apply

See the file script for an example of the file format
"""

# NOTE: tStack is now created internally, points & polygons are now temp


def parse_file(fname, screen, color):
    with open(fname, 'r') as script:
        keepReading = True

        tStack = [matrixOps.createIdentity(4)]
        # blank is used as a starting point for transformations
        blank = matrixOps.createIdentity(4)

        while keepReading:
            line = script.readline()
            cLine = line.strip("\n").lower()

            # --- LINE --- #

            if cLine == "line":
                args = script.readline().split(" ")
                if len(args) != 6:
                    raise ValueError("line call must be followed by 6 args")
                else:
                    points = []
                    add_edge(points, [int(args[0]), int(args[1]), int(args[
                             2])], [int(args[3]), int(args[4]), int(args[5])])
                    points = matrixOps.multiply(tStack[-1], points)
                    draw_lines(points, screen, color)

            # --- TRANSFORMATIONS --- #

            elif cLine == "scale":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError(
                        "scale call must be followed by 3 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = scale(blank, int(
                        args[0]), int(args[1]), int(args[2]))
                    tStack[-1] = matrixOps.multiply(tStack[-1], tMat)

            elif cLine == "move":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError("move call must be followed by 3 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = translate(blank, int(
                        args[0]), int(args[1]), int(args[2]))
                    tStack[-1] = matrixOps.multiply(tStack[-1], tMat)

            elif cLine == "rotate":
                args = script.readline().split(" ")
                if len(args) != 2:
                    raise ValueError("rotate call must be followed by 2 args")
                elif len(tStack) == 0:
                    raise IndexError(
                        "cannot perform operation on empty transform stack"
                    )
                else:
                    tMat = rotate(blank, args[0], int(args[1]))
                    tStack[-1] = matrixOps.multiply(tStack[-1], tMat)

            # --- TRANFORMATION STACK --- #

            elif cLine == "push":
                # Shouldn't be followed by any args
                topCopy = tStack[-1][:]
                tStack.append(topCopy)

            elif cLine == "pop":
                # Shouldn't be followed by any args
                tStack.pop()

            # --- CURVES --- #

            elif cLine == "circle":
                args = script.readline().split(" ")
                if len(args) != 4:
                    raise ValueError("circle call must be followed by 4 args")
                else:
                    points = []
                    add_circle(points, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), 1000)
                    points = matrixOps.multiply(tStack[-1], points)
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
                    points = matrixOps.multiply(tStack[-1], points)
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
                    points = matrixOps.multiply(tStack[-1], points)
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
                    polygons = matrixOps.multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

            elif cLine == "sphere":
                args = script.readline().split(" ")
                if len(args) != 4:
                    raise ValueError("sphere call must be followed by 4 args")
                else:
                    polygons = []
                    add_sphere(polygons, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), 20)  # adjust steps
                    polygons = matrixOps.multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

            elif cLine == "torus":
                args = script.readline().split(" ")
                if len(args) != 5:
                    raise ValueError("sphere call must be followed by 5 args")
                else:
                    polygons = []
                    add_torus(polygons, int(args[0]), int(args[1]),
                              int(args[2]), int(args[3]), int(args[4]), 20)
                    polygons = matrixOps.multiply(tStack[-1], polygons)
                    draw_polygons(polygons, screen, color)

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
