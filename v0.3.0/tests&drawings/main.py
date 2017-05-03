from display import *
from draw import *

screen = new_screen()
color = [0, 255, 0]

"""
# Dank Memes
# M
draw_line(10, 100, 10, 300, screen, color)
draw_line(10, 300, 50, 200, screen, color)
draw_line(50, 200, 90, 300, screen, color)
draw_line(90, 100, 90, 300, screen, color)
# e
draw_line(110, 100, 110, 200, screen, color)
draw_line(110, 100, 190, 100, screen, color)
draw_line(110, 200, 190, 200, screen, color)
draw_line(190, 200, 190, 150, screen, color)
draw_line(190, 150, 110, 150, screen, color)
# m
draw_line(210, 100, 210, 200, screen, color)
draw_line(210, 200, 250, 150, screen, color)
draw_line(250, 150, 290, 200, screen, color)
draw_line(290, 100, 290, 200, screen, color)
# e
draw_line(310, 100, 310, 200, screen, color)
draw_line(310, 100, 390, 100, screen, color)
draw_line(310, 200, 390, 200, screen, color)
draw_line(390, 200, 390, 150, screen, color)
draw_line(390, 150, 310, 150, screen, color)
# s
draw_line(410, 100, 490, 100, screen, color)
draw_line(490, 100, 490, 150, screen, color)
draw_line(490, 150, 410, 150, screen, color)
draw_line(410, 150, 410, 200, screen, color)
draw_line(410, 200, 490, 200, screen, color)
"""


# Demonstration #
# Draw grid lines
color = [255, 255, 255]
draw_line(250, 500, 250, 0, screen, color)
draw_line(0, 250, 500, 250, screen, color)
# Draw octant lines
color = [0, 0, 255]
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)
# Draw demo lines in each octant
color = [255, 0, 255]
draw_line(250, 250, 375, 500, screen, color)  # Octant2
draw_line(250, 250, 500 - 375, 0, screen, color)  # Octant6
color = [255, 255, 0]
draw_line(250, 250, 375, 0, screen, color)  # Octant7
draw_line(250, 250, 500 - 375, 500, screen, color)  # Octant3
color = [0, 255, 255]
draw_line(250, 250, 500, 375, screen, color)  # Octant1
draw_line(250, 250, 0, 500 - 375, screen, color)  # Octant5
color = [0, 255, 0]
draw_line(250, 250, 500, 500 - 375, screen, color)  # Octant8
draw_line(250, 250, 0, 375, screen, color)  # Octant4
plot(screen, [255, 255, 255], 250, 250)


"""
# Test Code #
draw_line_octant1(0, 0, 499, 499, screen, color)
draw_line_octant1(1, 1, 100, 10, screen, color)
draw_line_octant1(1, 1, 500, 1, screen, color)
draw_line_octant1(50, 50, 200, 150, screen, color)
draw_line_octant1(100, 60, 400, 200, screen, color)


# Octant2 Test #
color[RED] = 255
color[GREEN] = 0
draw_line_o2(0, 0, 0, 499, screen, color)
draw_line_o2(0, 0, 10, 250, screen, color)
draw_line_o2(0, 0, 50, 300, screen, color)

# Octant7 Test #
color[GREEN] = 0
color[BLUE] = 255
draw_line_octant7(0,500,200,100, screen, color)

# Octant8 Test #
color[GREEN] = 255
color[BLUE] = 0
draw_line_octant8(0,500,400,400, screen, color)
"""


# display(screen)
save_ppm(screen, "demo.ppm")
# save_extension(screen, 'img.png')
