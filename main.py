'''Guessing Game
  Logan Woods
Version 1.0.0.4
Guess the random number that has been selected'''

#Importing the required libraries
import random
import os
import time

#Defining variables
list_guess = []
bool_playagain = True
int_lives = 3


#Defining functions
def clear():
    os.system('clear')


def title():
    print("********Logans Guessing Game********")
    print("Lives: {}".format(int_lives))


#Asks users for their name
str_name = str(input("Welcome, What is your name? "))
clear()

#Welcomes user
print("********Logans Guessing Game********")
print("")
print("Hello {}".format(str_name))
print("")

int_level = input(
    "What difficulty level do you wish to play on? 1 - Easy | 2 - Normal | 3 - Hard "
)
clear()

print("********Logans Guessing Game********")
print("")
print("Hello {}".format(str_name))
print("")

if int_level == "1":
    print("Easy mode selected.")
    int_numberrange = 10

elif int_level == "2":
    print("Normal mode selected.")
    int_numberrange = 15

elif int_level == "3":
    print("Hard mode selected.")
    int_numberrange = 20

#Explains game
print("Welcome to Logan's guessing game.")
print(
    "Logan is going to think of a number between 1 and {}, your job is to guess that number."
    .format(int_numberrange))
print("You have 3 lives. Goodluck.")
print("")
input("Press Enter to start...")

#Game begins
while bool_playagain is True:
    clear()

    #Header is printed and player lives and guesses are displayed
    print("********Logans Guessing Game********")
    print("Lives: {}".format(int_lives))
    print("Current Guesses: {}".format(list_guess))

    #Random number is generated
    n = random.randint(1, int_numberrange)

    #Player takes first guess, guess is added to list
    guess = int(input("Guess Your number: "))
    list_guess.append(guess)

    #While the player has more than 0 lives, run the game
    while int_lives > 0:

        #Player takes first guess, guess is added to list

        #If the user guesses right, the loop ends
        if guess == n:

            clear()
            title()

            print("You got it right! Good Job {}.".format(str_name))
            print("")
            print("The number was: {}".format(n))
            print("You Guessed: {}".format(list_guess))
            bool_playagain = False
            break

        #If the users guesses incorrectly, the loop continues
        while guess != n:

            print("")

            #Warn the user if their guess was too low
            if guess < n:
                int_lives = int_lives - 1
                print("Incorrect!")
                print("")
                print("Your Guess is too low.")
                time.sleep(1)

            #Warn the user if their guess was too high
            elif guess > n:
                int_lives = int_lives - 1
                print("Incorrect!")
                print("")
                print("Your Guess is too high.")
                time.sleep(1)

            #If the user runs out of lives, the loop will end
            if int_lives == 0:
                break

            #Promts the user to enter another number
            else:
                clear()
                title()
                print("Current Guesses: {}".format(list_guess))
                print("")
                guess = int(input("Guess Your number: "))
                list_guess.append(guess)

    #End game text if the user runs out of lives
    if int_lives == 0:
        clear()
        print("********Logans Guessing Game********")
        print("Lives: {}".format(int_lives))
        print("")
        print("You lose, Your out of lives!")
        print("")
        print("The number was: {}".format(n))
        print("You Guessed: {}".format(list_guess))

    #Asks user if they wish to play again
    print("")
    bool_user_playagain = str(input("Do you wish to play again? Y/N "))
    bool_user_playagain = bool_user_playagain.strip()
    bool_user_playagain = bool_user_playagain.casefold()

    #Enables the game to run again
    if bool_user_playagain == "y":

        #See if the user wishes to change difficultys
        bool_user_changelevel = str(
            input("Do you wish to change the difficulty? Y/N "))
        bool_user_changelevel = bool_user_changelevel.strip()
        bool_user_changelevel = bool_user_changelevel.casefold()

        if bool_user_changelevel == "y":
            int_level = input(
                "What difficulty level do you wish to play on? 1 - Easy | 2 - Normal | 3 - Hard "
            )

            if int_level == "1":
                print("Easy mode selected.")
                int_numberrange = 10

            elif int_level == "2":
                print("Normal mode selected.")
                int_numberrange = 15

            elif int_level == "3":
                print("Hard mode selected.")
                int_numberrange = 20

        int_lives = 3
        list_guess = []
        bool_playagain = True

    #Stops the game from looping
    elif bool_user_playagain == "n":
        bool_playagain = False
        break

#Displays the end screen
clear()
print("********Logans Guessing Game********")
print("Thank you for playing Logan's guessing game.")
print("Have Great Day!")
'''
  needs 
  clear list if the users replays
  ask if the users wants to play again
  show the user their guesses
  play again option
  verify that inputs are the correct format and account for incorrect formats
  COMMENTING
  '''
