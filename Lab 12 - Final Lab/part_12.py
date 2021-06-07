import arcade
arcade.open_window(2000, 2000, "Welcome to Fun with Flags!")
arcade.set_background_color(arcade.csscolor.BLACK)
arcade.start_render()


def opening_statements():
    arcade.draw_text("""Let's test your knowledge on the wide world of flags!
The questions get progressivley harder, but you got this!
Answer to the best of your ability and give full answers.
Let the game begin!""", 500, 1400, arcade.color.WHITE, 15)


def american_flag():
    arcade.draw_lrtb_rectangle_filled(50, 500, 1300, 1100, arcade.color.WHITE)
    for row in range(13):
        for column in range(13):
            x = 1290  # Instead of zero, calculate the proper x location using 'column'
            y = 1280 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_lrtb_rectangle_filled(50, 500, x, y, arcade.color.RED)

def monaco_flag():
    arcade.draw_lrtb_rectangle_filled(50, 500, 1000, 800, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 500, 1000, 900, arcade.color.RED)


# Defining players score
def check_players_guess(guess, answer):
    global score
    guessing = True
    attempt = 0
    while guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct")
            score = score + 1/10 * 100
            guessing = False
        else:
            if attempt < 2:
                guess = input("Incorrect, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )







# Call all functions
opening_statements()
american_flag()
monaco_flag()




arcade.finish_render()
arcade.run()
