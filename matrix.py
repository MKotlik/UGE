# Matrix Module
# Unified Graphics Engine - Computer Graphics
# Misha (Mikhail Kotlik)

# This module contains code for adding points and edges to Matrices

import math


def add_point(matrix, point):
    if type(point) is not list:
        raise TypeError(
            "matrix.addPoint() point must be a 3-element list")
    elif len(point) != 3:
        raise ValueError(
            "matrix.addPoint() point must be a 3-element list")
    else:
        fourP = point[:]
        print fourP
        print fourP.append(1)
        matrix.append(fourP)


def add_edge(matrix, point1, point2):
    add_point(matrix, point1)
    add_point(matrix, point2)


def new_matrix(rows=0, cols=0):
    # Functon created by Mr. DW
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m
