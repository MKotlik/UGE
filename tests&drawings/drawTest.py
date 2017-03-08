import matrixOps
import transformOps
from edgeMatrix import EdgeMatrix
from draw import *
from display import *

screen = new_screen()

linesList = [[50, 50, 0, 1], [150, 50, 0, 1], [50, 50, 0, 1], [50, 150, 0, 1]]
linesList.extend([[50, 150, 0, 1], [150, 150, 0, 1]])
linesList.extend([[150, 150, 0, 1], [150, 50, 0, 1]])
mainMatrix = EdgeMatrix(initMatrix=linesList)
print mainMatrix
draw_matrix(mainMatrix.getMatrix(), screen, [0, 0, 255])
# display(screen)
save_ppm(screen, "matTest.ppm")
print "---------------------"

transMatrix = matrixOps.createIdentity(4)
transMatrix = transformOps.rotateZ(transMatrix, 45)
transMatrix = transformOps.scale(transMatrix, 2, 2, 2)
transMatrix = transformOps.translate(transMatrix, 100, 100, 0)
mainMatrix = EdgeMatrix(matrixOps.multiply(transMatrix, mainMatrix.getMatrix()))
clear_screen(screen)
draw_matrix(mainMatrix.getMatrix(), screen, [0, 0, 255])
save_ppm(screen, "drawTest.ppm")
print "---------------------"
