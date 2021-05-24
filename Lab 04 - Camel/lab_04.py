import random

def main():
    # Opening Statements
    print("Welcome to Camel!")
    print("""You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! 
    Survive your desert trek and out run the natives.""")

    # variables
    miles_traveled = 0
    camel_thirst = 0
    camel_fatigue = 0
    natives_traveled = -20
    canteen = 3
    done = False

    # start main loop
    while not done:
        natives_behind = miles_traveled - natives_traveled
        full_speed = random.randrange(10, 21)
        moderate_speed = random.randrange(5, 13)
        print("""
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.""")
        user_input = input("What is your choice? ")
        if user_input.lower() == "q":
            done = True

        # status
        elif user_input.lower() == "e":
            print("Miles traveled: ", miles_traveled)
            print("Drinks in canteen: ", canteen)
            print("Your camel has ", camel_fatigue, "amount of fatigue.")
            print("The natives are ", natives_behind, "miles behind you.")

        # stop for night
        elif user_input.lower() == "d":
            camel_fatigue *= 0
            print("Your camel feels refreshed and happy his fatigue is now ", camel_fatigue)
            natives_traveled += random.randrange(7, 15)

        # move full speed
        elif user_input.lower() == "c":
            print("You traveled ", full_speed, "miles!")
            miles_traveled += full_speed
            camel_thirst += 1
            camel_fatigue += random.randrange(1, 4)
            natives_traveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)


        # move moderate speed
        elif user_input.lower() == "b":
            print("You traveled ", moderate_speed, "miles!")
            miles_traveled += moderate_speed
            camel_thirst += 1
            camel_fatigue += 1
            natives_traveled += random.randrange(7, 15)
            oasis = random.randrange(1, 21)

        # drink canteen
        elif user_input.lower() == "a":
            if canteen == 0:
                print("You're out of water.")
            else:
                canteen -= 1
                camel_thirst *= 0
                print("You have ", canteen, "drinks left and you are no longer thirsty.")

        # not done check
        if oasis == 20:
            camel_fatigue *= 0
            camel_thirst *= 0
            canteen = 3
            print("You found an oasis! After taking a drink you filled your canteen and the camel is refreshed.")
        if natives_behind <= 15:
            print("The natives are coming closer!")
        if miles_traveled >= 200 and not done:
            print("You made it across the desert, you win!")
            done = True
        if natives_traveled >= miles_traveled:
            print("The natives caught and beheaded you.")
            print("You're dead!")
            done = True
        if camel_thirst > 4 and camel_thirst <= 6 and not done:
            print("You are thirsty")
        if camel_thirst > 6:
            print("You died of dehydration!")
            done = True
        if camel_fatigue > 5 and camel_fatigue <= 8 and not done:
            print("Your camel is getting tired.")
        if camel_fatigue > 8:
            print("Your camel is dead.")
            done = True

# Call main function
main()
