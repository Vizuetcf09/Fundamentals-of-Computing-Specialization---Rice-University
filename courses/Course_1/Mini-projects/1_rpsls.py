# Rock-paper-scissors-lizard-Spock
# The key idea of this program is to equate the strings
# "rock" "paper" "scissors" "lizard" and "Spock" to numbers

# as follows:

# 0 - rock
# 1 - paper
# 2 - scissors
# 3 - lizard 
# 4 - Spock

# helper function

def name_to_number(name):
  # convert name to number just using conditionals

  if name == "rock":
    number = 0
    return number
  
  elif name == "paper":
    number = 1
    return number
  
  elif name == "scissors":
    number = 2
    return number
  
  elif name == "lizard":
    number = 3
    return number
  
  elif name == "Spock":
    number = 4
    return number
  
  else:
    return print("Error!!!")
  
  # return the result  
  
  return number
  
def number_to_name(number):
  # convert number to name just using conditionals
  
  if number == 0:
    name = "rock"
    return name
  
  if number == 1:
    name = "paper"
    return name
  
  if number == 2:
    name = "scissors"
    return name
  
  if number == 3:
    name = "lizard"
    return name
  
  if number == 4:
    name = "Spock"
    return name
  
  else:
    return print("Error!!!")
  
  # return the result  
  
  return name

import random

def rpsls(name):
  # print a blanck line to separate consecutive games and print out the message for the player´s choice
  
  print(" ")
  print("Players chooses", name)
    
  # convert the player´s choice to player_number using the function: name_to_number
  
  player_number = name_to_number(name)
  # print(player_number)
  
  #  compute random guess for comp_number using random.randrange()
  comp_number = random.randrange(0, 5)
  # print(comp_number)
  
  # convert the comp_number to comp_choice whith number_to_name and print the message for computer´s choice
  
  comp_choice = number_to_name(comp_number)
  print("Computer chooses", comp_choice) 

  # compute difference of comp_number and player_number modulo five
  comp_and_player_number_dif = (player_number - comp_number) % 5
  
  # use conditionals to determine the winner, and print the winner message
  
  # Player and computer tie!
  if player_number == comp_number:
    print("Player and computer tie!")

  # # Player wins!  
  # # rock wins over scissors and lizard
  elif player_number == 0 and (comp_number == 2 or comp_number == 3):
    return print("Player wins!")
  
  # # paper wins over rock and Spock
  elif player_number == 1 and (comp_number == 0 or comp_number == 4):
    return print("Player wins!")
  # # scissors wins over paper and lizard 
  elif player_number == 2 and (comp_number == 1 or comp_number == 3):
    return print("Player wins!")
  
  # # lizard wins over paper and Spock
  elif player_number == 3 and (comp_number == 1 or comp_number == 4):
    return print("Player wins!")
  
  # # Spock wins over rock and scissors
  elif player_number == 4 and (comp_number == 0 or comp_number == 2):
    return print("Player wins!")
  
  # if comp_and_player_number_dif == 0:
  #   print ("Player and computer tie!")
  # elif comp_and_player_number_dif == 1 or comp_and_player_number_dif == 2:
  #   print ("Player wins!")

  else:
    print ("Computer wins!") 
  
  return 

# personal test

# name_to_number

# print("====================")
# print(" ")
# print(name_to_number("rock"))
# print(name_to_number("paper"))
# print(name_to_number("scissors"))
# print(name_to_number("lizard"))
# print(name_to_number("Spock"))
# print(" ")
# print("====================")

# number_to_name

# print("====================")
# print(" ")
# print(number_to_name(0))
# print(number_to_name(1))
# print(number_to_name(2))
# print(number_to_name(3))
# print(number_to_name(4))
# print(" ")
# print("====================")

# test your code

print("====================")
rpsls("rock")
rpsls("paper")
rpsls("scissors")
rpsls("lizard")
rpsls("Spock")
print(" ")
print("====================")
