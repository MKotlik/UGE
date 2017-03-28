from display import *
from matrix import *
from draw import *
from transformOps import *
import matrixOps
import time

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""


def parse_file(fname, points, transform, screen, color):
    with open(fname, 'r') as script:
        keepReading = True
        while keepReading:
            line = script.readline()
            cLine = line.strip("\n").lower()

            if cLine == "line":
                args = script.readline().split(" ")
                if len(args) != 6:
                    raise ValueError("line call must be followed by 6 args")
                else:
                    add_edge(points, [int(args[0]), int(args[1]), int(args[
                             2])], [int(args[3]), int(args[4]), int(args[5])])

            elif cLine == "ident":
                transform = matrixOps.createIdentity(4)

            elif cLine == "scale":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError(
                        "scale call must be followed by 3 args")
                else:
                    transform = scale(transform, int(
                        args[0]), int(args[1]), int(args[2]))

            elif cLine == "move":
                args = script.readline().split(" ")
                if len(args) != 3:
                    raise ValueError("move call must be followed by 3 args")
                else:
                    transform = translate(transform, int(
                        args[0]), int(args[1]), int(args[2]))

            elif cLine == "rotate":
                args = script.readline().split(" ")
                if len(args) != 2:
                    raise ValueError("rotate call must be followed by 2 args")
                else:
                    transform = rotate(transform, args[0], int(args[1]))

            elif cLine == "circle":
                args = script.readline().split(" ")
                if len(args) != 4:
                    raise ValueError("circle call must be followed by 4 args")
                else:
                    add_circle(points, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), 1000)

            elif cLine == "bezier":
                args = script.readline().split(" ")
                if len(args) != 8:
                    raise ValueError("bezier call must be followed by 8 args")
                else:
                    add_bezier(points, int(args[0]), int(args[1]),
                               int(args[2]), int(args[3]), int(args[4]),
                               int(args[5]), int(args[6]), int(args[7]), 1000)

            elif cLine == "hermite":
                args = script.readline().split(" ")
                if len(args) != 8:
                    raise ValueError("hermite call must be followed by 8 args")
                else:
                    add_hermite(points, int(args[0]), int(args[1]),
                                int(args[2]), int(args[3]), int(args[4]),
                                int(args[5]), int(args[6]), int(args[7]), 1000)

            elif cLine == "box":
                args = script.readline().split(" ")
                if len(args) != 6:
                    raise ValueError("box call must be followed by 6 args")
                else:
                    add_box(points, int(args[0]), int(args[1]),
                            int(args[2]), int(args[3]), int(args[4]),
                            int(args[5]))

            elif cLine == "apply":
                points = matrixOps.multiply(transform, points)

            elif cLine == "display":
                clear_screen(screen)  # YES? NO? MAYBE SO?
                draw_lines(points, screen, color)
                display(screen)
                time.sleep(0.5)

            elif cLine == "save":
                args = script.readline().split(" ")
                if len(args) != 1:
                    raise ValueError("save call must be followed by 1 arg")
                else:
                    draw_lines(points, screen, color)
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
