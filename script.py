import mdl
from display import *
from matrix import *
from draw import *
from matrixOps import *
from transformOps import *
import time

# NOTE: Apparently curves are unsupported in MDL?


"""======== first_pass( commands, symbols ) ==========
  Checks the commands array for any animation commands
  (frames, basename, vary)

  Should set num_frames and basename if the frames
  or basename commands are present
  If vary is found, but frames is not, the entire
  program should exit.
  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.
  jdyrlandweaver
  ==================== """
def first_pass( commands ):
    pass


"""======== second_pass( commands ) ==========
  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).
  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.
  Go through the command array, and when you find vary, go
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value.
  ===================="""
def second_pass( commands, num_frames ):
    pass


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
