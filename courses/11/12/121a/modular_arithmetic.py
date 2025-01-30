# Reminder - modular arithmethic

def divition(dividendo, divisor):
  result = dividendo / divisor
  return result

def integer_divition(dividendo, divisor):
  result = dividendo // divisor
  return result

def reminder(dividendo, divisor):
  result = dividendo % divisor
  return result

# Operators:
# residuo = cociente (quotient = integer divition) = //
# resto = residuo (reminder) = %

# Problem - get the ones digit of a number

# num = 49
# tens = ?
# ones = ?

num = 49
div = divition(num, 10) # output = 4.9
tens = integer_divition(num, 10)  # output = 4
ones =  reminder(num, 10)  # output = 9

print(div)
print(tens, ones)
print(10 * tens + ones, num) 


# Aplications
# 
# 24 hours clock

# If hour = 20
# What time (hours_plus_shift) is before shifts = 8 hours?
#  

hours = 20
shifts = 8  # (shift = turno(laboral))

div = divition((hours + shifts), 24)
rem = integer_divition((hours + shifts), 24)
hours_plus_shift = reminder((hours + shifts), 24)  # output: 4

print(div)
print(rem)
print(hours_plus_shift) 

# Screen wraparound

# Spaceship from week seven

width = 800
position = 2
move = 5
div = divition((position + move), width)
rem = integer_divition((position + move), width)
position = reminder((position + move), width)

print(div)
print(rem)
print(position)

