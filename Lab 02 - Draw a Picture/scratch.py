"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.SAE)

# Get ready to draw
arcade.start_render()




# Draw a sun
arcade.draw_circle_filled(300, 300, 100, arcade.color.YELLOW)
arcade.draw_circle_outline(300,300,100, arcade.color.CADMIUM_RED)
arcade.draw_circle_outline(301,301,100, arcade.color.AMARANTH_PINK)
arcade.draw_circle_outline(302, 302, 100, arcade.color.BARBIE_PINK)

# Rays to the left, right, up, and down
arcade.draw_line(300, 300, 50, 300, arcade.color.YELLOW, 3)
arcade.draw_line(300, 300, 550, 300, arcade.color.YELLOW, 3)
arcade.draw_line(300, 300, 300, 550, arcade.color.YELLOW, 3)
arcade.draw_line(300, 300, 300, 50, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(300, 350, 500, 400, arcade.color.YELLOW, 3)
arcade.draw_line(300, 350, 100, 400, arcade.color.YELLOW, 3)
# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0

arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.AZURE)


# Draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Sunrise on a Lake",
                 150, 230,
                 arcade.color.BLACK, 24)
# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(50, 300, 20, 60, arcade.csscolor.SIENNA)
# Tree top
arcade.draw_circle_filled(50, 350, 30, arcade.csscolor.DARK_GREEN)
# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

