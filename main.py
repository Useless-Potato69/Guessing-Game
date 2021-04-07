'''Guessing Game
  Logan Woods
Version 0.0.0.1
Guess the random number that has been selected'''

#Importing the required libraries
import random
import os

#Defining variables
list_guess = [ ]
bool_playagain = True
int_lives = 3

#Defining functions
def clear(): os.system('clear') 

#Asks users for their name
str_name = input("Welcome, What is your name? ")
clear()

#Welcomes user
print("********Logans Guessing Game********")
print("")
print("Hello {}".format(str_name))

#Explains game

print("Welcome to Logan's guessing game.")
print("Logan is going to think of a number between 1 and 10, your job is to guess that number.")
print("You have 3 lives. Goodluck.")
print("")
input("Press Enter to start...")

while bool_playagain is True:
  clear()
  print("********Logans Guessing Game********")
  print("Lives: {}".format(int_lives))

  n = random.randint(1, 10)
  print(n)

  guess = int(input("Guess Your number: "))
  list_guess.append(guess)

  int_lives = int_lives - 1
  print(int_lives)
  while int_lives > 0:

    if guess == n:

      print("You got it right!")
      bool_playagain = False
      break
    "elif guess != n"