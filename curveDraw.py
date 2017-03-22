# curveDraw Module
# Unified Graphics Engine - Computer Graphics
# Misha (Mikhail Kotlik)
from display import *
from matrix import *
from draw import *
import matrixOps


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
            add_edge(matrix, prevX, prevY, 0, X, Y, 0)
        prevX, prevY = X, Y
        curStep += dStep
    return matrix  # Yes or no?


def add_hermite(matrix, x0, y0, x1, y1, mX0, mY0, mX1, mY1, steps):
    print "hermite"
    # I'm not sure if im using this correctly...
    hermite_mat = [[2, -3, 0, 1], [-2, 3, 0, 0], [1, -2, 1, 0], [1, 1, 0, 0]]
    x_base = [[x0, x1, mX0, mX1]]
    y_base = [[y0, y1, mY0, mY1]]
    return add_general_curve(matrix, hermite_mat, x_base, y_base, steps)


def add_bezier(matrix, x0, y0, x1, y1, x2, y2, x3, y3, steps):
    print "bezier"
    # I'm not sure if im using this correctly...
    bezier_mat = [[-1, 3, -3, 2], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]]
    x_base = [[x0, x1, x2, x3]]
    y_base = [[y0, y1, y2, y3]]
    return add_general_curve(matrix, bezier_mat, x_base, y_base, steps)


def add_general_curve(matrix, inverse_mat, x_base, y_base, steps):
    x_coeff = matrixOps.multiply(inverse_mat, x_base)[0]
    y_coeff = matrixOps.multiply(inverse_mat, y_base)[0]

    t = 0
    dStep = 1.0 / steps
    prevX = x_coeff[3]
    prevY = y_coeff[3]

    while t < 1:
        X = (x_coeff[0] * t**3) + (x_coeff[1] * t**2) + (x_coeff[2] * t) + x_coeff[3]
        print X
        Y = (y_coeff[0] * t**3) + (y_coeff[1] * t**2) + (y_coeff[2] * t) + y_coeff[3]
        add_edge(matrix, prevX, prevY, 0, X, Y, 0)
        prevX = X
        prevY = Y
        t += dStep
    return matrix  # Yes or no?
