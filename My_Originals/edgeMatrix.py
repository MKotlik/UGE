# EdgeMatrix Module
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

import matrixOps


class EdgeMatrix:
    '''Class for representing and modifying an edge matrix'''

    # Point position enums
    X, Y, Z, SCALE = 0, 1, 2, 3

    # Constructor
    def __init__(self, initMatrix=None, prevObj=None):
        if initMatrix is not None:
            if type(initMatrix) is not list:
                raise TypeError(
                    "initMatrix arg of EdgeMatrix constructor must be 2d list")
            elif len(initMatrix) > 0 and len(initMatrix[0]) != 4:
                raise ValueError(
                    "initMatrix of EdgeMatrix constructor must have 4 rows")
            else:
                self.matrixStore = initMatrix[:][:]
        elif prevObj is not None:
            prevMatrix = prevObj.getMatrix()
            self.matrixStore = prevMatrix[:][:]
        else:
            self.matrixStore = []

    def getMatrix(self):
        return self.matrixStore

    def getIntMatrix(self):
        intMatrix = []
        for col in self.matrixStore:
            intCol = []
            for rowCell in col:
                intCol.append(int(round(rowCell)))
            intMatrix.append(intCol)
        return intMatrix

    def setMatrix(self, new2dList):
        if type(new2dList) is not list:
            raise TypeError(
                "initMatrix arg of EdgeMatrix constructor must be 2d list")
        elif len(new2dList) > 0 and len(new2dList[0]) != 4:
            raise ValueError(
                "initMatrix of EdgeMatrix constructor must have 4 rows")
        else:
            self.matrixStore = new2dList[:][:]

    def addPoint(self, point):
        if type(point) is not list:
            raise TypeError(
                "addPoint method of edgeMatrix takes a 4-element list")
        elif len(point) != 4:
            raise ValueError(
                "addPoint method of edgeMatrix takes a 4-element list")
        else:
            self.matrixStore.append(point)

    def addEdge(self, point1, point2):
        try:
            self.addPoint(point1)
            self.addPoint(point2)
        except TypeError:
            raise TypeError(
                "TE: addEdge method of edgeMatrix takes two 4-element lists")
        except ValueError:
            raise ValueError(
                "VE: addEdge method of edgeMatrix takes two 4-element lists")

    def multiply(self, operand):
        try:
            product = matrixOps.multiply(operand, self.getMatrix())
            self.setMatrix(product)
        except TypeError:
            raise TypeError("multiply method of edgeMatrix takes a matrix"
                            "or a number")
        except ValueError as e:
            if str(e) == "matrixOps.multiply() cannot multiply an empty matrix":
                raise ValueError(
                    "multiply method of edgeMatrix cannot multiply "
                    "an empty matrix")
            elif (str(e) == "matrixOps.multiply() matrix multiplication "
                  "requires that num cols in 1 matrix matches num rows "
                  "in 2nd matrix"):
                raise ValueError("matrix multiplication of edgeMatrix "
                                 "requires that num cols in 1 matrix matches "
                                 "num rows in 2nd matrix")
            else:
                raise ValueError("unknown ValueError")

    def __str__(self):
        if len(self.matrixStore) == 0:
            return "[]"
        else:
            obj_str = ""
            rowList = ["|"] * 4
            for point in self.matrixStore:
                # Calculate maxLen for padding
                maxLen = 0
                for coord in point:
                    curLen = len(str(coord))
                    if curLen > maxLen:
                        maxLen = curLen
                # Create padding formatting string
                padStr = "{:>" + str(maxLen) + "}"
                # Add each coord to respective rowStr, w/ padding
                rowList[0] += padStr.format(point[0]) + " | "
                rowList[1] += padStr.format(point[1]) + " | "
                rowList[2] += padStr.format(point[2]) + " | "
                rowList[3] += padStr.format(point[3]) + " | "
            for row in rowList:
                obj_str += row[:-1] + "\n"
            return obj_str[:-1]

    # __multiply__ goes here

    # __add__ goes here
