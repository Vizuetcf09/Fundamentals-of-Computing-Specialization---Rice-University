# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# Add code to the program template that creates a 
# frame with an input field whose handler has the 
# name input_guess. You will use this input field 
# to enter guesses.

# import simplegui
import random
import math


# globals

secret_number = random.randint(0, 100)
attempts = 0

# helper function: new_game()

def new_game():
    global secret_number

# event handlers functions: range100(), range1000() 
# and input_guess()

def range100():
    
    global secret_number
    secret_number = random.randint(0, 100)
    global attempts
    attempts = 7
    
    print "You chose a game in range 0-100"
    print "Chose a number betwen 0-100:"
    print secret_number
    print "attempts: ", attempts
    
def range1000():
    
    global secret_number
    secret_number = random.randint(0, 1000)
    global attempts
    attempts = 10
    
    print "You chose a game in range 0-1000"
    print "Chose a number betwen 0-1000:"
    print secret_number
    print "attempts: ", attempts
    
def attempts_count():
    
    global attempts
    
    if attempts >= 1:
        attempts -= 1
        print "attempts: ", attempts
    elif attempts == 0: 
        print "You loose"
    
def input_guess(guess):
    
    global secret_number 
    guess = int(guess)
    print"Guess was", guess

    if guess < secret_number:
        print "Lower"
    elif guess > secret_number:
        print "Higher"
    else:
        print "Correct"
    
    attempts_count()
            
# create frame

frame = simplegui.create_frame('Gues the number game', 200, 200)

# register event handlers for control

def button_100_handler():
    range100()
    return

def button_1000_handler():
    range1000()
    return

def text_handler(guess):
    input_guess(guess)
    return

# create controls

button100 = frame.add_button("Range: 0-100", 
                           button_100_handler, 120)
button1000 = frame.add_button("Range: 0-1000",
                            button_1000_handler, 120)
input_text = frame.add_input('Chose a number',
                             text_handler, 45)
input_text.set_text(" ")

# start frame
frame.start()