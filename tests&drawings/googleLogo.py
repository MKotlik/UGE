# Google Logo using Edge Matrix
# Matrix Assignment - Computer Graphics
# Misha (Mikhail Kotlik)

from draw import draw_matrix
from display import *
from edgeMatrix import EdgeMatrix
import math
import matrixOps


def drawLogo():
    # General properties/setup
    screen = new_screen(500, 500)
    outerRadius = 200
    innerRadius = 120
    backRadius = 220
    redColor = [255, 0, 0]
    yellowColor = [255, 255, 0]
    greenColor = [0, 255, 0]
    blueColor = [0, 0, 255]
    whiteColor = [255, 255, 255]
    curAngle = 50

    # Drawing a solid white background
    background = EdgeMatrix()
    centerPoint = [250, 250, 0, 1]
    for angle in range(361):
        radAngle = angle * math.pi / 180.0
        higherX = round(backRadius * math.cos(radAngle)) + 250
        higherY = round(backRadius * math.sin(radAngle)) + 250
        background.addEdge(centerPoint, [higherX, higherY, 0, 1])
        lowerX = math.floor(backRadius * math.cos(radAngle)) + 250
        lowerY = math.floor(backRadius * math.sin(radAngle)) + 250
        background.addEdge(centerPoint, [lowerX, lowerY, 0, 1])
    draw_matrix(background.getIntMatrix(), screen, whiteColor)

    # Red curve of logo
    redCurve = EdgeMatrix()
    while curAngle <= 160:
        radAngle = curAngle * math.pi / 180.0
        outerX = round(outerRadius * math.cos(radAngle)) + 250
        outerY = round(outerRadius * math.sin(radAngle)) + 250
        innerX = round(innerRadius * math.cos(radAngle)) + 250
        innerY = round(innerRadius * math.sin(radAngle)) + 250
        redCurve.addEdge([innerX, innerY, 0, 1], [outerX, outerY, 0, 1])
        lOuterX = round(outerRadius * math.cos(radAngle)) + 250
        lOuterY = round(outerRadius * math.sin(radAngle)) + 250
        lInnerX = round(innerRadius * math.cos(radAngle)) + 250
        lInnerY = round(innerRadius * math.sin(radAngle)) + 250
        redCurve.addEdge([lInnerX, lInnerY, 0, 1], [lOuterX, lOuterY, 0, 1])
        curAngle += 1
    draw_matrix(redCurve.getIntMatrix(), screen, redColor)

    # Yellow curve of log
    yellowCurve = EdgeMatrix()
    while curAngle <= 200:
        radAngle = curAngle * math.pi / 180.0
        outerX = round(outerRadius * math.cos(radAngle)) + 250
        outerY = round(outerRadius * math.sin(radAngle)) + 250
        innerX = round(innerRadius * math.cos(radAngle)) + 250
        innerY = round(innerRadius * math.sin(radAngle)) + 250
        yellowCurve.addEdge([innerX, innerY, 0, 1], [outerX, outerY, 0, 1])
        lOuterX = round(outerRadius * math.cos(radAngle)) + 250
        lOuterY = round(outerRadius * math.sin(radAngle)) + 250
        lInnerX = round(innerRadius * math.cos(radAngle)) + 250
        lInnerY = round(innerRadius * math.sin(radAngle)) + 250
        yellowCurve.addEdge([lInnerX, lInnerY, 0, 1], [lOuterX, lOuterY, 0, 1])
        curAngle += 1
    draw_matrix(yellowCurve.getIntMatrix(), screen, yellowColor)

    # Green curve of logo
    greenCurve = EdgeMatrix()
    while curAngle <= 300:
        radAngle = curAngle * math.pi / 180.0
        outerX = round(outerRadius * math.cos(radAngle)) + 250
        outerY = round(outerRadius * math.sin(radAngle)) + 250
        innerX = round(innerRadius * math.cos(radAngle)) + 250
        innerY = round(innerRadius * math.sin(radAngle)) + 250
        greenCurve.addEdge([innerX, innerY, 0, 1], [outerX, outerY, 0, 1])
        lOuterX = round(outerRadius * math.cos(radAngle)) + 250
        lOuterY = round(outerRadius * math.sin(radAngle)) + 250
        lInnerX = round(innerRadius * math.cos(radAngle)) + 250
        lInnerY = round(innerRadius * math.sin(radAngle)) + 250
        greenCurve.addEdge([lInnerX, lInnerY, 0, 1], [lOuterX, lOuterY, 0, 1])
        curAngle += 1
    draw_matrix(greenCurve.getIntMatrix(), screen, greenColor)

    # Blue curve of logo
    blueCurve = EdgeMatrix()
    while curAngle <= 350:
        radAngle = curAngle * math.pi / 180.0
        outerX = round(outerRadius * math.cos(radAngle)) + 250
        outerY = round(outerRadius * math.sin(radAngle)) + 250
        innerX = round(innerRadius * math.cos(radAngle)) + 250
        innerY = round(innerRadius * math.sin(radAngle)) + 250
        blueCurve.addEdge([innerX, innerY, 0, 1], [outerX, outerY, 0, 1])
        lOuterX = round(outerRadius * math.cos(radAngle)) + 250
        lOuterY = round(outerRadius * math.sin(radAngle)) + 250
        lInnerX = round(innerRadius * math.cos(radAngle)) + 250
        lInnerY = round(innerRadius * math.sin(radAngle)) + 250
        blueCurve.addEdge([lInnerX, lInnerY, 0, 1], [lOuterX, lOuterY, 0, 1])
        curAngle += 1
    draw_matrix(blueCurve.getIntMatrix(), screen, blueColor)

    # Blue curve of lego
    blueBox = EdgeMatrix()
    rightX = round(outerRadius * math.cos(340 * math.pi / 180.0)) + 250
    leftX = rightX - 170
    startY = round(outerRadius * math.sin(340 * math.pi / 180.0)) + 250
    curY = 0
    while curY < 80:
        if curY % 3 != 0:
            blueBox.addEdge([leftX, startY + curY, 0, 1], [rightX, startY + curY, 0, 1])
        curY += 1
    draw_matrix(blueBox.getIntMatrix(), screen, blueColor)

    # Display
    display(screen)
    save_extension(screen, "empireGlitches.png")
    # save_ppm(screen, "empireGlitches.ppm")

drawLogo()
print "Drew Google logo for demonstration"
