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
arcade.draw_circle_filled(800, 530, 60, arcade.color.YELLOW)

# Rays for left, right, down, and up
arcade.draw_line(600, 530, 800, 530, arcade.color.YELLOW, 3)
arcade.draw_line(900, 530, 800, 530, arcade.color.YELLOW, 3)
arcade.draw_line(800, 350, 800, 500, arcade.color.YELLOW, 3)
arcade.draw_line(800, 600, 800, 500, arcade.color.YELLOW, 3)

# Diagonal Rays
arcade.draw_line(700, 450, 800, 530, arcade.color.YELLOW, 3)
arcade.draw_line(890, 590, 800, 530, arcade.color.YELLOW, 3)










# Finish drawing

arcade.finish_render()


# Keep the window up until someone closes it.
arcade.run()








