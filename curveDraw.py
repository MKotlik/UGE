# curveDraw Module
# Unified Graphics Engine - Computer Graphics
# Misha (Mikhail Kotlik)
from display import *
from matrix import *
from draw import *


def drawCircle(matrix, cX, cY, r, steps):
    curStep = 0
    prevX = -1
    prevY = -1
    while curStep < steps:
        angle = 2 * math.pi * (curStep / float(steps))
        if prevX == -1:
            prevX = cX + r * math.cos(angle)
            prevY = cY + r * math.sin(angle)
        else:
            curX = cX + r * math.cos(angle)
            curY = cY + r * math.sin(angle)
            add_edge(matrix, prevX, prevY, 0, curX, curY, 0)
            prevX, prevY = curX, curY
        curStep += 1
    return matrix  # Yes or no?
