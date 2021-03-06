# Draw Module
# Unified Graphics Engne - Computer Graphics
# Misha (Mikhail Kotlik)

# This module calculates lines, curves, and 3d shapes

from display import *
from matrix import *
from draw import *
from matrixOps import *
import random


# +++++++++++++++++ #
# POLYGON FUNCTIONS #
# +++++++++++++++++ #

def add_polygon(points, point1, point2, point3):
    """
    ======== void add_polygon() ==========
    Inputs: surfaces matrix, 3 vertices
    Result: Adds the vertices (x0, y0, z0), (x1, y1, z1)
    and (x2, y2, z2) to the polygon matrix. They
    define a single triangle surface.
    ====================
    """
    # Copy & add scale factor to each point (required for transformations)
    # If scale factor is added to argument points, results in duplicate cells
    sPoint1 = point1[:]
    sPoint1.append(1)
    sPoint2 = point2[:]
    sPoint2.append(1)
    sPoint3 = point3[:]
    sPoint3.append(1)
    # Append points to polygon matrix
    points.append(sPoint1)
    points.append(sPoint2)
    points.append(sPoint3)


def draw_polygons(points, screen, color):
    """
    ======== void draw_polygons() ==========
    Inputs: polygons matrix, screen, color
    Result: Goes through polygons 3 points at a time, drawing
    lines connecting each points to create bounding
    triangles
    ====================
    """
    if len(points) < 3:
        raise ValueError(
            'draw.draw_polygons() needs at least three points in matrix')
    i = 0
    # Implement backface culling now
    numShowed = 0
    while i < len(points) - 2:
        if should_show(points[i], points[i + 1], points[i + 2]):
            # From 0th to 1st
            draw_line(points[i][0], points[i][1], points[
                      i + 1][0], points[i + 1][1], screen, color)
            # From 1st to 2nd
            draw_line(points[i + 1][0], points[i + 1][1],
                      points[i + 2][0], points[i + 2][1], screen, color)
            # From 2nd to 0th
            draw_line(points[i + 2][0], points[i + 2]
                      [1], points[i][0], points[i][1], screen, color)
            # numShowed += 1
            # Generate a random color for the polygon
            p_color = generate_random_color()
            fill_polygon(points[i], points[i+1], points[i+2], screen, p_color)
            print "Filled a polygon"
        i += 3
    # print "Showed: " + str(numShowed) + "; Culled: " + str((len(points) / 3
    # - numShowed))


def should_show(point0, point1, point2):
    Ax = point1[0] - point0[0]  # x1 - x0
    Ay = point1[1] - point0[1]  # y1 - y0
    Bx = point2[0] - point0[0]  # x2 - x0
    By = point2[1] - point0[1]  # y2 - y0
    Nz = Ax * By - Ay * Bx
    return Nz > 0


def fill_polygon(point0, point1, point2, screen, color):
    """Fills the specified polygon using scanline conversion.
    Draws horizontal lines (incrementing the y-value by 1) from bottom to top.
    """
    print "polygon filling"
    def getY(point):
        return point[1]
    orderedPoints = sorted([point0, point1, point2], key=getY)
    print orderedPoints
    # print point0
    top = orderedPoints[2]
    mid = orderedPoints[1]
    bot = orderedPoints[0]
    # Slopes of the polygon sides as (x/y)
    # Check if dy is 0, in which case slope is automatically 0
    if (top[1] - bot[1]) == 0:
        dBtoT = 0
    else:
        dBtoT = int((top[0] - bot[0]) / (top[1] - bot[1]))
    if (mid[1] - bot[1]) == 0:
        dBtoM = 0
    else:
        dBtoM = int((mid[0] - bot[0]) / (mid[1] - bot[1]))
    if (top[1] - mid[1]) == 0:
        dMtoT = 0
    else:
        dMtoT = int((top[0] - mid[0]) / (top[1] - mid[1]))
    # For y values from the bottom to the midpoint
    print "should go thru a for loop here: " + str(int(mid[1] - bot[1]))
    for ycnt in range(0, int(mid[1] - bot[1])):
        # In x = b + my form
        x0 = bot[0] + dBtoT * ycnt
        y0 = bot[1] + ycnt
        x1 = bot[0] + dBtoM * ycnt
        y1 = bot[1] + ycnt
        draw_line(x0, y0, x1, y1, screen, color)
        print "drew a scanline"
    # print x0
    # mid_x0 = x0  # If this works
    for ycnt in range(0, int(top[1] - mid[1])):
        # x0 = mid_x0 + dBtoT * ycnt
        # In x = b + my form
        x0 = bot[0] + dBtoT * (ycnt + mid[1] - bot[1])
        y0 = mid[1] + ycnt
        x1 = mid[0] + dMtoT * ycnt
        y1 = mid[1] + ycnt
        draw_line(x0, y0, x1, y1, screen, color)


def generate_random_color():
    """Returns a color list containing random values for R, G, and B"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return [red, green, blue]


# ++++++++++++++++++ #
# 3D SHAPE FUNCTIONS #
# ++++++++++++++++++ #

# Adds the polyogons for a box surface to a polyogon matrx
def add_box(matrix, x, y, z, width, height, depth):
    """ Draws a rectangular prism with a polygon surface
    Inputs: Upper-left corner (x, y, z), width, height, and depth
    Result: Calculates the surface polygons, adds to given polygon matrix
    """
    # IMPORTANT, DO NOT MIX UP A POLYGON MATRIX AND AN EDGE MATRIX
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    # Front Face
    add_polygon(matrix, [x, y, z], [x1, y1, z], [x1, y, z])
    add_polygon(matrix, [x, y, z], [x, y1, z], [x1, y1, z])

    # Back Face
    add_polygon(matrix, [x1, y, z1], [x, y1, z1], [x, y, z1])
    add_polygon(matrix, [x1, y, z1], [x1, y1, z1], [x, y1, z1])

    # Left Face
    add_polygon(matrix, [x, y, z1], [x, y1, z], [x, y, z])
    add_polygon(matrix, [x, y, z1], [x, y1, z1], [x, y1, z])

    # Right Face
    add_polygon(matrix, [x1, y, z], [x1, y1, z1], [x1, y, z1])
    add_polygon(matrix, [x1, y, z], [x1, y1, z], [x1, y1, z1])

    # Top Face
    add_polygon(matrix, [x1, y, z], [x1, y, z1], [x, y, z1])
    add_polygon(matrix, [x1, y, z], [x, y, z1], [x, y, z])

    # Bottom Face
    add_polygon(matrix, [x, y1, z], [x1, y1, z1], [x1, y1, z])
    add_polygon(matrix, [x, y1, z], [x, y1, z1], [x1, y1, z1])


def add_box_edges(matrix, x, y, z, width, height, depth):
    """ Draws the 12 edges of a rectangular prism
    Inputs: Upper-left corner (x, y, z), width, height, and depth
    Result: Calculates the edges of the prism, adds to given edge matrix
    """

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
    # return matrix  # ?


def add_sphere(matrix, cx, cy, cz, r, steps):
    # Draws polygons on sphere surface
    points = generate_sphere(matrix, cx, cy, cz, r, steps)
    i = 0
    while i < len(points) - steps - 1:
        add_polygon(matrix, points[i], points[i + steps + 1], points[i + 1])
        add_polygon(matrix, points[i], points[
                    i + steps], points[i + steps + 1])
        i += 1
    # return matrix  # ?
    # SAVE THESE MODES FOR DEBUGGING
    """
    # Plots points alone
    for point in generate_sphere(matrix, cx, cy, cz, r, steps):
        add_edge(matrix, [point[0], point[1], point[
                 2]], [point[0], point[1], point[2]])
    """

    """
    # Connects the points with lines
    cirPoints = generate_sphere(matrix, cx, cy, cz, r, steps)
    i = 0
    while i < len(cirPoints) - 1:
        add_edge(matrix, cirPoints[i], cirPoints[i+1])
        i += 1
    """


def generate_sphere(matrix, cx, cy, cz, r, steps):
    step = 1.0 / steps
    points = []
    rot = 0
    while rot <= 1 + step:
        circ = 0
        while circ <= 1 + step:
            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2 * math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2 * math.pi * rot) + cz
            points.append([x, y, z])
            circ += step
        rot += step
    return points


def add_torus(matrix, cx, cy, cz, r0, r1, steps):
    # Draws polygons on torus surface
    points = generate_torus(matrix, cx, cy, cz, r0, r1, steps)
    i = 0
    while i < len(points) - steps - 1:
        add_polygon(matrix, points[i], points[i + steps + 1], points[i + 1])
        add_polygon(matrix, points[i], points[
                    i + steps], points[i + steps + 1])
        i += 1


def generate_torus(matrix, cx, cy, cz, r0, r1, steps):
    step = 1.0 / steps
    points = []
    rot = 0
    while rot <= 1 + step:
        circ = 0
        while circ <= 1 + step:
            x = (r0 * math.cos(2 * math.pi * circ) + r1) * \
                math.cos(2 * math.pi * rot) + cx
            y = r0 * math.sin(2 * math.pi * circ) + cy
            z = (r0 * math.cos(2 * math.pi * circ) + r1) * - \
                1 * math.sin(2 * math.pi * rot) + cz
            points.append([x, y, z])
            circ += step
        rot += step
    return points


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
    # I'm not sure if im using this correctly...
    hermite_mat = [[2, -3, 0, 1], [-2, 3, 0, 0], [1, -2, 1, 0], [1, -1, 0, 0]]
    x_base = [[x0, x1, mX0, mX1]]
    y_base = [[y0, y1, mY0, mY1]]
    return add_general_curve(matrix, hermite_mat, x_base, y_base, steps)


def add_bezier(matrix, x0, y0, x1, y1, x2, y2, x3, y3, steps):
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
