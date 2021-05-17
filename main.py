'''Guessing Game
  Logan Woods
Version 2.0.0.2
Guess the random number that has been selected

THIS PROGRAM MUST BE RUN IN A LINUX ENVIROMENT
Python IDLE on Windows 10 does not support the required libraries'''

##################################################################
# SETUP
##################################################################

# Importing the required libraries
import random
import os
import time
import getch

# Defining variables
list_guess = []
bool_playagain = True
int_lives = 3
bool_no_lvl_selected = True


# Defining functions
def clear():
    os.system('clear')


def title():
    print("********Logans Guessing Game********")
    print("Lives: {}".format(int_lives))

##################################################################
# INTRODUCTION
##################################################################

# Asks users for their name
str_name = str(input("Welcome, What is your name? "))
clear()

# Welcomes user
print("********Logans Guessing Game********")
print("")
print("Hello {}".format(str_name))
print("")

# User selects difficulty
while bool_no_lvl_selected is True:
    try:

        print(
            "What difficulty of you wish to play on? Easy 1-10 | Normal 1-15 | Hard 1-20"
        )
        print("")
        int_level = input(
            "Please select your difficulty. 1 - Easy | 2 - Normal | 3 - Hard ")
        if int_level == "1":
            print("Easy mode selected.")
            int_numberrange = 10
            bool_no_lvl_selected = False

        elif int_level == "2":
            print("Normal mode selected.")
            int_numberrange = 15
            bool_no_lvl_selected = False

        elif int_level == "3":
            print("Hard mode selected.")
            int_numberrange = 20
            bool_no_lvl_selected = False

        else:
            print("")
            print("You must select 1, 2 or 3.")
            time.sleep(1)
            clear()
            print("********Logans Guessing Game********")
            print("")
            print("Hello {}".format(str_name))
            print("")
    except:
        print("You must select 1, 2 or 3.")

# Explains game
clear()
print("********Logans Guessing Game********")
print("")
print("Hello {}".format(str_name))
print("")
print("Welcome to Logan's guessing game.")
print(
    "Logan is going to think of a number between 1 and {}, your job is to guess that number."
    .format(int_numberrange))
print("You have 3 lives. Goodluck.")
print("")
time.sleep(2)
print("Press any key to continue...")
char = getch.getch()

##################################################################
# GAME
##################################################################

# Game begins
while bool_playagain is True:
    clear()

    # Header is printed and player lives and guesses are displayed
    title()
    print("Current Guesses: {}".format(list_guess))

    # Random number is generated
    n = random.randint(1, int_numberrange)

    # While the player has more than 0 lives, loop the game
    while int_lives > 0:

        while True:
            try:
                guess = int(input("Guess Your number: "))
                break
            except:
                print("")
                print("You must input a number.")
                time.sleep(2)
                clear()
                title()
                print("Current Guesses: {}".format(list_guess))

        # If the users guesses incorrectly, the loop continues
        while guess != n:

            print("")

            # If the user's input is lower than the minimum
            if guess < 1:
                print("Your answer needs to be more than 1!")
                time.sleep(2)

            # If the user's input is higher than the maximum
            elif guess > int_numberrange:
                print("Your answer cannot be more than {}".format(
                    int_numberrange))
                time.sleep(2)

            else:

                # Warn the user if their guess was too low
                if guess < n:
                    list_guess.append(guess)
                    int_lives = int_lives - 1
                    print("Incorrect!")
                    print("")
                    print("Your Guess is too low.")
                    time.sleep(2)

                # Warn the user if their guess was too high
                elif guess > n:
                    list_guess.append(guess)
                    int_lives = int_lives - 1
                    print("Incorrect!")
                    print("")
                    print("Your Guess is too high.")
                    time.sleep(2)

            # If the user runs out of lives, the loop will end
            if int_lives == 0:
                break

            # Promts the user to enter another number
            else:
                clear()
                title()
                print("Current Guesses: {}".format(list_guess))
                print("")

                # Make sure that the user inputs the correct data type
                while True:
                    try:

                        guess = int(input("Guess Your number: "))
                        break
                        break
                    except:
                        print("")
                        print("You must input a number.")
                        time.sleep(2)
                        clear()
                        title()
                        print("Current Guesses: {}".format(list_guess))

        # If the user guesses right, the loop ends
        if guess == n:

            clear()
            list_guess.append(guess)
            title()

            print("You got it right! Good Job {}.".format(str_name))
            print("")
            print("The number was: {}".format(n))
            print("You Guessed: {}".format(list_guess))
            bool_playagain = False
            break

##################################################################
# END OF GAME
##################################################################

# End game text if the user runs out of lives
    if int_lives == 0:
        clear()
        title()
        print("")
        print("You lose, Your out of lives!")
        print("")
        print("The number was: {}".format(n))
        print("You Guessed: {}".format(list_guess))

    bool_no_ans = True
    while bool_no_ans is True:

        # Asks user if they wish to play again
        print("")
        bool_user_playagain = str(input("Do you wish to play again? Y/N "))
        bool_user_playagain = bool_user_playagain.strip()
        bool_user_playagain = bool_user_playagain.casefold()

        # Enables the game to run again
        if bool_user_playagain == "y":
            bool_no_ans = False

            bool_no_ans2 = True
            while bool_no_ans2 is True:

                # See if the user wishes to change difficultys
                bool_user_changelevel = str(
                    input("Do you wish to change the difficulty? Y/N "))
                bool_user_changelevel = bool_user_changelevel.strip()
                bool_user_changelevel = bool_user_changelevel.casefold()

                if bool_user_changelevel == "y":
                    bool_no_ans2 = False

                    # User selects difficulty
                    while True:
                        try:

                            print(
                                "What difficulty of you wish to play on? Easy 1-10 | Normal 1-15 | Hard 1-20"
                            )
                            print("")
                            int_level = input(
                                "Please select your difficulty. 1 - Easy | 2 - Normal | 3 - Hard "
                            )
                            if int_level == "1":
                                print("Easy mode selected.")
                                int_numberrange = 10
                                bool_no_lvl_selected = False
                                break

                            elif int_level == "2":
                                print("Normal mode selected.")
                                int_numberrange = 15
                                bool_no_lvl_selected = False
                                break

                            elif int_level == "3":
                                print("Hard mode selected.")
                                int_numberrange = 20
                                bool_no_lvl_selected = False
                                break

                            else:
                                print("")
                                print("You must select 1, 2 or 3.")
                                time.sleep(1)
                                clear()
                                print("")

                        except:
                            print("You must select 1, 2 or 3.")
                    int_lives = 3
                    list_guess = []
                    bool_playagain = True

                # If the user doesnt wish to change difficulty
                elif bool_user_changelevel == "n":
                    int_lives = 3
                    list_guess = []
                    bool_playagain = True
                    bool_no_ans2 = False

                else:
                    print("")
                    print("You must select Y or N.")
                    print("")

        # Stops the game from looping
        elif bool_user_playagain == "n":
            bool_playagain = False
            bool_no_ans = False
            break

        else:
            print("")
            print("You must select Y or N.")
            print("")

##################################################################
# END SCREEN
##################################################################

# Displays the end screen
clear()
print("********Logans Guessing Game********")
print("Thank you for playing Logan's guessing game.")
print("Have Great Day!")
time.sleep(3)
clear()
'''
  needs 
  clear list if the users replays
  ask if the users wants to play again
  show the user their guesses
  play again option
  verify that inputs are the correct format and account for incorrect formats
  COMMENTING
  '''
