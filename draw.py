from display import *


def draw_matrix(edgeMat, screen, color):
    pairNum = 0
    limit = len(edgeMat)
    if len(edgeMat) % 2 != 0:
        limit -= 1
    while pairNum < (limit - 1):
        p1 = edgeMat[pairNum]
        p2 = edgeMat[pairNum + 1]
        draw_line(p1[0], p1[1], p2[0], p2[1], screen, color)
        pairNum += 1
    if len(edgeMat) % 2 != 0:
        lastPt = edgeMat[len(edgeMat) - 1]
        plot(screen, color, lastPt[0], lastPt[1])


def draw_line(x0, y0, x1, y1, screen, color):
    # General draw_line wrapper
    # Decides which octant_helper to call, modifies starting-ending points
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
