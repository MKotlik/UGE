import matrixOps
import transformOps


simpleMatrix = [[1, 1, 1, 1], [2, 2, 2, 1], [3, 2, 3, 1], [5, 6, 7, 1]]
matrixOps.printM(simpleMatrix)
print "---------------------"

scaledMatrix = transformOps.scale(simpleMatrix, 2, 2, 2)
matrixOps.printM(scaledMatrix)
print "---------------------"

scaledMatrix2 = transformOps.scale(simpleMatrix, 3, 0.5, 1)
matrixOps.printM(scaledMatrix2)
print "---------------------"

translatedMatrix = transformOps.translate(simpleMatrix, 10, -1, 2)
matrixOps.printM(translatedMatrix)
print "---------------------"

ZRotatedMatrix = transformOps.rotateZ(simpleMatrix, 90)
matrixOps.printM(ZRotatedMatrix)
print "---------------------"

XRotatedMatrix = transformOps.rotateX(simpleMatrix, 30)
matrixOps.printM(XRotatedMatrix)
print "---------------------"

YRotatedMatrix = transformOps.rotateY(simpleMatrix, 60)
matrixOps.printM(YRotatedMatrix)
print "---------------------"

GenRotatedMatrix = transformOps.rotate(simpleMatrix, "z", 180)
matrixOps.printM(GenRotatedMatrix)
print "---------------------"
