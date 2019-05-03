#!/usr/bin/env bash 
# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the 
# `target` and the `guess`), and prints out an appropriate message based on 
# how close the guess is to the target:

# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low

import random
target = random.randint(1, 50)

def print_hot_or_cold(target, guess):
    """Prints approximate distance between guess and target.  Target will be selected at random.
    User will input a guess."""
    if (guess == target):
        print("got it!")
    elif(target-1 < guess < target) or (target < guess < target+1):
        print("scalding hot")
        if target<guess<target+1:
            print("guess is high")
        else:
            print("guess is low")
    elif(target-3 < guess < target) or (target < guess < target+3):
        print("very warm")
        if target<guess<target+3:
            print("guess is high")
        else:
            print("guess is low")        
    elif(target-5 < guess < target) or (target < guess < target+5):
        print("warm")
        if target<guess<target+5:
            print("guess is high")
        else:
            print("guess is low")        
    elif(target-8 < guess < target) or (target < guess < target+8):
        print("cold")
        if target<guess<target+8:
            print("guess is high")
        else:
            print("guess is low")
    elif(target-13 < guess < target) or (target < guess < target+13):
        print("very cold")
        if target<guess<target+13:
            print("guess is high")
        else:
            print("guess is low")
    else:
        print("icy freezing and miserably cold")
        if guess>target+13:
            print("guess is high")
        else:
            print("guess is low")        


# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is to that target (use your previous 
# function!). Note that you will need to convert the input into a number.

# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next chapter)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. The later is an example of **recursion**.

def guess_number(target):
    """Prompts user for a guess and passes the guess to hot_or_cold.  
    Will prompt user again if guess is not the target."""
    guess = int(input("Pick a number from 1 to 50: "))
    print(print_hot_or_cold(target, guess))
    if guess != target:
        guess_number(target)


# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# user of the range of numbers before asking them for a guess.
