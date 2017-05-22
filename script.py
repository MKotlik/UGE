import mdl
from display import *
from matrix import *
from draw import *
from matrixOps import *
from transformOps import *
from pprint import pprint
import time

# NOTE: Apparently curves are unsupported in MDL?

# GLOBAL SETTINGS:
DEBUG = False


def run(filename):
    """
    This function runs an mdl script
    Args: filename (str)
    """
    color = [255, 255, 255]

    print "UGE: Parsing Started"
    parsing_result = mdl.parseFile(filename)
    print "UGE: Parsing Completed"

    if parsing_result:
        (commands, symbols) = parsing_result
    else:
        print "UGE Error: Parsing Failed"
        return

    if DEBUG:
        print commands
        print "================"
        print symbols
        return

    # first_pass, reads through command list and returns number of frames,
    #   basename, and a list of the indices of the vary
    #   cmds within the command list
    (first_status, frames, basename, vary_indices) = first_pass(commands)
    if first_status is False:  # If frames or vary were used improperly, exit
        return

    # second_pass, reads through command list and returns a list of
    # variable dictionaries per frame
    # Checking for vary instead of frame number, b/c could have a static gif
    if len(vary_indices) > 0:
        (second_status, variables) = second_pass(
            commands, frames, vary_indices)
    if second_status is False:  # If vary was used improperly, exit
        return

    # third_pass, iterates over the entire command list and creates each frame
    # pprint(variables)
    third_pass(commands, symbols, frames, variables, basename, color)


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


def first_pass(commands):
    frames = -1  # -1 by default for error checking
    basename = None
    vary_indices = []  # Command list positions of vary cmds

    for i in range(len(commands)):
        command = commands[i]
        if command[0] == "frames":
            frames = command[1]
        elif command[0] == "basename":
            basename = command[1]
        elif command[0] == "vary":
            if frames == -1:
                # TODO: improve error message
                print format_error(command, "UGE Error: number of frames must be set before a vary call")
                return (False, frames, basename, vary_indices)
            vary_indices.append(i)

    if frames != -1 and basename is None:
        basename = "animation"
        print format_error([], 'UGE Notice: user didn\'t set basename, defaulting to "animation"')
    if frames == -1:
        frames = 0
    return (True, frames, basename, vary_indices)


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
  Args: commands (list), num_frames (int), vary_indices (list)
  Returns: (status (str), variables_list (list))
    - commands is a list of the script's MDL commands
    - num_frames is the number of frames set in the sript
    - vary_indices is a list of the positions of vary calls in the command list
    - returns a tuple, where the first element is a boolean status, and the
        second element is the variable list
  ===================="""


def second_pass(commands, num_frames, vary_indices):
    variables = [{} for i in range(num_frames)]  # Optimize by avoiding resizing
    # set first frame to start_val
    # modify subsequent frames by ((end_val - start_val) / (frame diffs))
    for i in vary_indices:
        vary = commands[i]
        # NOTE: vary args might be strings rather than nums

        # ERROR CHECKING
        if vary[3] <= vary[2]:
            print format_error(vary, "UGE Error: last_frame must be greater than first_frame in vary call")
            return (False, variables)

        # set diff of knob btwn frames to:
        #   (end_val - start_val) / float(end_frame - start_frame)
        v_diff = (vary[5] - vary[4]) / float(vary[3] - vary[2])

        # set knob for each frame from start_frame to end_frame, inclusive
        for frameN in range(vary[2], vary[3] + 1):
            frameFactor = frameN - vary[2]

            # set value of knob in dict corresponding to current frame to:
            #   v_diff * cur_frame + start_val
            # vary[1] is the knob name
            variables[frameN][vary[1]] = (v_diff * frameFactor) + vary[4]
        # NOTE: should I leave the frames after end_frame untouched?
    return (True, variables)


def third_pass(commands, symbols, num_frames, variables, basename, color):
    screen = new_screen()
    tStack = [createIdentity(4)]
    # blank is used as a starting point for transformations
    blank = createIdentity(4)
    # step = 0.1
    # NOTE: Allow setting a global step?

    # Constants/variables will be saved in a dict

    # Iterate over frames
    for frame_num in range(num_frames):
        tStack = [createIdentity(4)]
        # print symbols
        # Set up knobs in symbol table (symbols[knob] = value)
        # NOTE: am I supposed to set symbol table w/o set command?
        # NOTE: how am I supposed to access the varibles in the calc funcs?
        for knob_name in variables[frame_num]:
            symbols[knob_name] = variables[frame_num][knob_name]

        for command in commands:

            # -- ANIMATION COMMANDS -- #

            if command[0] == "set":
                # set knobname to value (or creates and fills said knob)
                symbols[command[1]] = command[2]

            elif command[0] == "setknobs":
                # set all knobs to specified value
                for knob in symbols:
                    symbols[knob] = command[1]

            # -- STACK COMMANDS -- #

            elif command[0] == "push":
                tStack.append(tStack[-1][:])

            elif command[0] == "pop":
                tStack.pop()
                if len(tStack) == 0:
                    print format_error(command, "UGE Warning: Transformation stack is empty")

            # -- TRANSFORMATION COMMANDS -- #

            # NOTE: need to test whether adding knob to symbol table,
            # automatically adds it to the command args

            elif command[0] == "scale":
                if len(tStack) == 0:
                    print format_error(command, "UGE Error: scale command can't be applied to empty stack")
                    break
                # If knob given in command, use value from symbol table
                if command[4] is not None:
                    if command[4] in symbols:
                        knob = symbols[command[4]]
                    else:
                        print format_error(command, "UGE Error: reference to an undefined knob")
                        break
                else:
                    # Scale by 1 if no knob given
                    knob = 1
                tMat = scale(blank, float(
                    command[1]) * knob, float(command[2]) * knob,
                    float(command[3]) * knob)
                tStack[-1] = multiply(tStack[-1], tMat)

            elif command[0] == "move":
                if len(tStack) == 0:
                    print format_error(command, "UGE Error: move command can't be applied to empty stack")
                    break
                # If knob given in command, use value from symbol table
                if command[4] is not None:
                    if command[4] in symbols:
                        knob = symbols[command[4]]
                    else:
                        print format_error(command, "UGE Error: reference to an undefined knob")
                        break
                else:
                    # Scale by 1 if no knob given
                    knob = 1
                tMat = translate(blank, float(
                    command[1]) * knob, float(command[2]) * knob,
                    float(command[3]) * knob)
                # tStack[-1]
                # print tMat
                tStack[-1] = multiply(tStack[-1], tMat)

            elif command[0] == "rotate":
                if len(tStack) == 0:
                    print format_error(command, "UGE Error: rotate command can't be applied to empty stack")
                    break
                # If knob given in command, use value from symbol table
                if command[3] is not None:
                    if command[3] in symbols:
                        knob = symbols[command[3]]
                    else:
                        print format_error(command, "UGE Error: reference to an undefined knob")
                        break
                else:
                    # Scale by 1 if no knob given
                    knob = 1
                tMat = rotate(blank, command[1], float(command[2]) * knob)
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
                # pprint(tStack[-1])
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
                print "UGE: saving image as " + command[1]
                save_extension(screen, command[1])

            # -- ENDIF (command identification)

        if len(symbols) > 0:  # If variables and vary are used
            # Auto-save at the end of each frame
            dir_name = "anim/"
            # Calculate the num of digits in largest frame number
            num_digits = int(math.floor(math.log10(num_frames))) + 1
            # Create a 0-padded frame identifier
            frm_str = str(frame_num).zfill(num_digits)
            frame_name = dir_name + basename + frm_str + ".png"
            print "UGE: saving image as " + frame_name
            save_extension(screen, frame_name)

            # Clear screen for next frame
            clear_screen(screen)

        # ENDFOR (frame iteration)

    if len(symbols) > 0:  # If variables and vary are used
        # auto-animate at the end of the animation
        make_animation(basename)


def format_error(command, message):
    """Builds an error/warning/notice report string
    Args: command (list), message (str)
    Returns: error (str)
    """
    # TODO: trace error-causing commands back to lines, and report
    error_str = message + "\n"
    if len(command) > 0:
        error_str += "\tAt: " + "".join(command)
    return error_str
