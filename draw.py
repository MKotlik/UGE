# Draw Module
# Unified Graphics Engne - Computer Graphics
# Misha (Mikhail Kotlik)

# This module calculates lines, curves, and 3d shapes

from display import *
from matrix import *
from draw import *
from matrixOps import *


# ++++++++++++++++++ #
# 3D SHAPE FUNCTIONS #
# ++++++++++++++++++ #

# Adds a rectangular prism to an edge matricx
def add_box(matrix, x, y, z, width, height, depth):
    """Given the upper-left corner (x, y, z) of a rectangular prism and its
    width, height, and depth, calculates the 12 edges of the prism and adds
    them to the matrix"""

    # FRONT FACE
    # U,L,N to U,R,N
    add_edge(matrix, [x, y, z], [x + width, y, z])
    # U,L,N to D,L,N
    add_edge(matrix, [x, y, z], [x, y - height, z])
    # U,R,N to D,R,N
    add_edge(matrix, [x + width, y, z], [x + width, y - height, z])
    # D,L,N to D,R,N
    add_edge(matrix, [x, y - height, z], [x + width, y - height, z])

    # LATERAL EDGES
    # U,L,N to U,L,F
    add_edge(matrix, [x, y, z], [x, y, z + depth])
    # U,R,N to U,R,F
    add_edge(matrix, [x + width, y, z], [x + width, y, z + depth])
    # D,L,N to D,L,F
    add_edge(matrix, [x, y - height, z], [x, y - height, z + depth])
    # D,R,N to D,R,F
    add_edge(matrix, [x + width, y - height, z],
             [x + width, y - height, z + depth])

    # DISTANT FACE
    # U,L,F to U,R,F
    add_edge(matrix, [x, y, z + depth], [x + width, y, z + depth])
    # U,L,F to D,L,F
    add_edge(matrix, [x, y, z + depth], [x, y - height, z + depth])
    # U,R,F to D,R,F
    add_edge(matrix, [x + width, y, z + depth],
             [x + width, y - height, z + depth])
    # D,L,F to D,R,F
    add_edge(matrix, [x, y - height, z + depth],
             [x + width, y - height, z + depth])
    return matrix


def add_sphere(matrix, cx, cy, cz, r, step):
    
    for point in generate_sphere(matrix, cx, cy, cz, r, step):
        add_edge(matrix, [point[0], point[1], point[
                 2]], [point[0], point[1], point[2]])
    """

    cirPoints = generate_sphere(matrix, cx, cy, cz, r, step)
    i = 0
    while i < len(cirPoints) - 1:
        add_edge(matrix, cirPoints[i], cirPoints[i+1])
        i += 1
    """


def generate_sphere(matrix, cx, cy, cz, r, steps):
    steps = float(steps)
    rot = 0
    cirPoints = []
    while rot <= steps:
        cirStep = 0
        while cirStep <= steps:
            X = r * math.cos(2 * rot / steps * math.pi) * math.cos(cirStep / steps * math.pi) + cx
            Y = r * math.sin(2 * rot / steps * math.pi) + cy
            Z = r * math.cos(2 * rot  / steps * math.pi) * -1 * math.sin(cirStep / steps * math.pi) + cz
            # add_point(matrix, [X, Y, Z])
            cirPoints.append([X, Y, Z])
            cirStep += 1
        rot += 1
    return cirPoints


def add_torus(matrix, cx, cy, cz, r0, r1, steps):
    for point in generate_torus(matrix, cx, cy, cz, r0, r1, steps):
        add_edge(matrix, [point[0], point[1], point[
                 2]], [point[0], point[1], point[2]])


def generate_torus(matrix, cx, cy, cz, r0, r1, steps):
    steps = float(steps)
    rot = 0
    cirPoints = []
    while rot <= steps:
        cirStep = 0
        while cirStep <= steps:
            rotAng = 2 * rot / steps * math.pi
            cirAng = 2 * cirStep / steps * math.pi
            X = (r0 * math.cos(rotAng) + r1) * math.cos(cirAng) + cx
            Y = r0 * math.sin(rotAng) + cy
            Z = (r0 * math.cos(rotAng) + r1) * -1 * math.sin(cirAng) + cz
            # add_point(matrix, [X, Y, Z])
            cirPoints.append([X, Y, Z])
            cirStep += 1
        rot += 1
    return cirPoints


# +++++++++++++++ #
# CURVE FUNCTIONS #
# +++++++++++++++ #


def add_circle(matrix, cX, cY, cZ, r, steps):
    curStep = 0
    dStep = 1.0 / steps
    prevX = -1
    prevY = -1
    while curStep < 1:
        angle = 2 * math.pi * (curStep / 1)
        X = cX + r * math.cos(angle)
        Y = cY + r * math.sin(angle)
        if prevX != -1:
            add_edge(matrix, [prevX, prevY, 0], [X, Y, 0])
        prevX, prevY = X, Y
        curStep += dStep
    return matrix  # Yes or no?


def add_hermite(matrix, x0, y0, x1, y1, mX0, mY0, mX1, mY1, steps):
    print "hermite"
    # I'm not sure if im using this correctly...
    hermite_mat = [[2, -3, 0, 1], [-2, 3, 0, 0], [1, -2, 1, 0], [1, -1, 0, 0]]
    x_base = [[x0, x1, mX0, mX1]]
    y_base = [[y0, y1, mY0, mY1]]
    return add_general_curve(matrix, hermite_mat, x_base, y_base, steps)


def add_bezier(matrix, x0, y0, x1, y1, x2, y2, x3, y3, steps):
    print "bezier"
    # I'm not sure if im using this correctly...
    bezier_mat = [[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]]
    x_base = [[x0, x1, x2, x3]]
    y_base = [[y0, y1, y2, y3]]
    return add_general_curve(matrix, bezier_mat, x_base, y_base, steps)


def add_general_curve(matrix, inverse_mat, x_base, y_base, steps):
    x_coeff = multiply(inverse_mat, x_base)[0]
    y_coeff = multiply(inverse_mat, y_base)[0]

    t = 0
    dStep = 1.0 / steps
    prevX = x_coeff[3]
    prevY = y_coeff[3]

    while t < 1:
        X = (x_coeff[0] * t**3) + (x_coeff[1] * t**2) + \
            (x_coeff[2] * t) + x_coeff[3]
        Y = (y_coeff[0] * t**3) + (y_coeff[1] * t**2) + \
            (y_coeff[2] * t) + y_coeff[3]
        add_edge(matrix, [prevX, prevY, 0], [X, Y, 0])
        prevX = X
        prevY = Y
        t += dStep
    return matrix  # Yes or no?


# ++++++++++++++ #
# LINE FUNCTIONS #
# ++++++++++++++ #


def draw_lines(edgeMat, screen, color):
    if len(edgeMat) < 2:
        raise ValueError(
            'draw.draw_lines() needs at least two points in matrix')
    pairNum = 0
    limit = len(edgeMat)
    if len(edgeMat) % 2 != 0:
        limit -= 1
    while pairNum < (limit - 1):
        p1 = edgeMat[pairNum]
        p2 = edgeMat[pairNum + 1]
        draw_line(p1[0], p1[1], p2[0], p2[1], screen, color)
        pairNum += 2
    if len(edgeMat) % 2 != 0:
        lastPt = edgeMat[len(edgeMat) - 1]
        plot(screen, color, lastPt[0], lastPt[1])


def draw_line(x0, y0, x1, y1, screen, color):
    # General draw_line wrapper
    # Decides which octant_helper to call, modifies starting-ending matrix
    # Rounds x & y, in case they were taken from non-int matrix
    x0 = int(round(x0))
    y0 = int(round(y0))
    x1 = int(round(x1))
    y1 = int(round(y1))

    dX = abs(x1 - x0)
    dY = abs(y1 - y0)
    if (x1 >= x0):  # Quadrants 1 & 2 (Pos-x direction)
        if (y1 >= y0):  # Octants 1 & 2 (Pos-y direction)
            if (dX >= dY):  # Octant 1
                draw_line_octant1(x0, y0, x1, y1, screen, color)
            else:  # Octant 2
                draw_line_octant2(x0, y0, x1, y1, screen, color)
        else:  # Octants 8 & 7 (Neg-y direction)
            if (dX >= dY):  # Octant 8
                draw_line_octant8(x0, y0, x1, y1, screen, color)
            else:  # Octant 7
                draw_line_octant7(x0, y0, x1, y1, screen, color)
    else:  # Quadrants 3 & 4 (Neg-x direction)
        if (y1 >= y0):  # Octants 4 & 3 (Pos-y direction)
            if (dX >= dY):  # Octant 4
                draw_line_octant8(x1, y1, x0, y0, screen, color)
            else:  # Octant 3
                draw_line_octant7(x1, y1, x0, y0, screen, color)
        else:  # Octants 5 & 6 (Neg-y direction)
            if (dX >= dY):  # Octant 5
                draw_line_octant1(x1, y1, x0, y0, screen, color)
            else:  # Octant 6
                draw_line_octant2(x1, y1, x0, y0, screen, color)


def draw_line_octant1(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = 2 * A + B
    while (x <= x1):
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += 2 * B
        x += 1
        d += 2 * A
    plot(screen, color, x1, y1)


def draw_line_octant2(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = A + 2 * B
    while (y <= y1):
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B
    plot(screen, color, x1, y1)


def draw_line_octant7(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = A - 2 * B
    while (y >= y1):
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2 * A
        y -= 1
        d -= 2 * B
    plot(screen, color, x1, y1)


def draw_line_octant8(x0, y0, x1, y1, screen, color):
    # Set initial coords & calculate line constants
    x = x0
    y = y0
    A = y1 - y0
    B = x0 - x1  # -(x1 - x0)
    d = 2 * A - B
    while (x <= x1):
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2 * B
        x += 1
        d += 2 * A
    plot(screen, color, x1, y1)


def draw_points(points, screen, color):
    if len(points) < 1:
        raise ValueError(
            'draw.draw_points() needs at least one point in matrix')
    for point in points:
        plot(screen, color, int(point[0]), int(point[1]))
