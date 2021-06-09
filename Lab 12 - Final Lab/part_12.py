import arcade

# Open window, set background to black
arcade.open_window(1000, 1000, "Welcome to Fun with Flags!")
arcade.set_background_color(arcade.csscolor.PINK)
arcade.start_render()


def opening_statements():
    # Opening statements to player
    arcade.draw_text("""Let's test your knowledge on the wide world of flags!
The questions get progressivley harder, but you got this!
Answer to the best of your ability.
Let the game begin!""", 300, 900, arcade.color.BLACK, 15)


def german_flag():
    # Draw German flag
    arcade.draw_text("1.", 40, 850, arcade.color.BLACK, 30)
    arcade.draw_lrtb_rectangle_filled(50, 350, 850, 750, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 350, 850, 817, arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(50, 350, 817, 784, arcade.color.RED)
    arcade.draw_lrtb_rectangle_filled(50, 350, 784, 750, arcade.color.YELLOW)

def monaco_flag():
    # Draw Monaco flag
    arcade.draw_text("2.", 50, 700, arcade.color.BLACK, 30)
    arcade.draw_lrtb_rectangle_filled(50, 350, 700, 600, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 350, 700, 650, arcade.color.RED)

def nigeria_flag():
    # Draw Nigerian flag
    arcade.draw_text("3.", 50, 550, arcade.color.BLACK, 30)
    arcade.draw_lrtb_rectangle_filled(50, 350, 550, 450, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 150, 550, 450, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(250, 350, 550, 450, arcade.color.GREEN)

def lithuania_flag():
    # Draw Lithuanian flag
    arcade.draw_text("4.", 50, 400, arcade.color.BLACK, 30)
    arcade.draw_lrtb_rectangle_filled(50, 350, 400, 300, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 350, 400, 367, arcade.color.YELLOW)
    arcade.draw_lrtb_rectangle_filled(50, 350, 367, 334, arcade.color.GREEN)
    arcade.draw_lrtb_rectangle_filled(50, 350, 334, 300, arcade.color.RED)

def luxembourg_flag():
    # Draw Luxembourg flag
    arcade.draw_text("5.", 50, 250, arcade.color.BLACK, 30)
    arcade.draw_lrtb_rectangle_filled(50, 350, 250, 150, arcade.color. WHITE)
    arcade.draw_lrtb_rectangle_filled(50, 350, 250, 217, arcade.color.RED)
    arcade.draw_lrtb_rectangle_filled(50, 350, 184, 150, arcade.color.LIGHT_BLUE)


# Defining players score
def check_players_guess(guess, answer):
    global score
    guessing = True
    attempt = 0
    while guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct")
            score = score + 1/5 * 100
            guessing = False
        else:
            if attempt < 2:
                guess = input("Incorrect, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )

# Call functions
opening_statements()
german_flag()
monaco_flag()
nigeria_flag()
lithuania_flag()
luxembourg_flag()

arcade.finish_render()
arcade.run()


# Variables
score = 0

# Message to player
for i in range(3):
    print("Please,")
print("Answer in full names, not abbreviations.")

# Question 1
guess1 = input("Let's start off easy. What country does flag #1 represent?")
guess1 = guess1.lstrip()
check_players_guess(guess1, "Germany")


# Question 2
guess2 = input("This one is harder. What principality does flag #2 represent?")
guess2 = guess2.lstrip()
check_players_guess(guess2, "Monaco")


# Question 3
guess3 = input("Alright, here comes the challenge. What country does flag #3 represent?")
guess3 = guess3.lstrip()
check_players_guess(guess3, "Nigeria")


# Question 4
guess4 = input("And what country does flag #4 belong to?")
guess4 = guess4.lstrip()
check_players_guess(guess4, "Lithuania")


# Questions 5
guess5 = input("Last but not least, the hardest of them all. What country does flag #5 represent?")
guess5 = guess5.lstrip()
check_players_guess(guess5, "Luxembourg")


# Ending message to player with their score
print("Congratulations, your score is " + str(score))
