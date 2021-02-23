# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(900, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the sun
arcade.draw_circle_filled(800, 530, 60, arcade.color.AUREOLIN)

# Rays for left, right, down, and up
arcade.draw_line(600, 530, 800, 530, arcade.color.AUREOLIN, 3)
arcade.draw_line(900, 530, 800, 530, arcade.color.AUREOLIN, 3)
arcade.draw_line(800, 350, 800, 500, arcade.color.AUREOLIN, 3)
arcade.draw_line(800, 600, 800, 500, arcade.color.AUREOLIN, 3)

# Diagonal Rays
arcade.draw_line(700, 450, 800, 530, arcade.color.AUREOLIN, 3)
arcade.draw_line(890, 590, 800, 530, arcade.color.AUREOLIN, 3)
arcade.draw_line(700, 590, 800, 530, arcade.color.AUREOLIN, 3)
arcade.draw_line(890, 480, 800, 530, arcade.color.AUREOLIN, 3)

# Draw Sidewalk
arcade.draw_lrtb_rectangle_filled(0, 899, 50, 0, arcade.color.BATTLESHIP_GREY)

#  Base of Building
arcade.draw_lrtb_rectangle_filled(0, 200, 400, 0, arcade.color.ARSENIC)

# Top of Building
arcade.draw_lrtb_rectangle_filled(30, 170, 430, 400, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(60, 130, 460, 430, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(90, 95, 520, 460, arcade.color.ARSENIC)

# Another Building
arcade.draw_lrtb_rectangle_filled(250, 450, 500, 0, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(270, 430, 530, 500, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(300, 400, 560, 530, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(345, 350, 600, 560, arcade.color.ARSENIC)

# Another Building
arcade.draw_lrtb_rectangle_filled(500, 800, 300, 0, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(560, 740, 330, 300, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(625, 675, 370, 330, arcade.color.ARSENIC)
arcade.draw_lrtb_rectangle_filled(645, 650, 420, 370, arcade.color.ARSENIC)

# Tree Trunk
arcade.draw_rectangle_filled(225, 50, 30, 90, arcade.csscolor.SADDLE_BROWN)

# Tree Top (circle)
arcade.draw_circle_filled(225, 120, 40, arcade.csscolor.GREEN)

# Another Tree (trunk and arc)
# Arc is centered at (480, 70) with a width of 60 and height of 150.
# The starting angle is 0, and ending angle is 180.
arcade.draw_rectangle_filled(480, 60, 30, 90, arcade.csscolor.SADDLE_BROWN)
arcade.draw_arc_filled(480, 70, 60, 150, arcade.csscolor.GREEN, 0, 180)

# Another Tree (trunk and polygon)
arcade.draw_rectangle_filled(840, 80, 30, 90, arcade.csscolor.SADDLE_BROWN)
arcade.draw_polygon_filled(((840, 200),
                            (790, 150),
                            (810, 90),
                            (870, 90),
                            (890, 150)
                            ),
                           arcade.csscolor.GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()