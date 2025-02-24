# Stopwatch: The Game

import simplegui
import random

# define global variables
time = 1
position = [60, 110]
width = 200
height = 200
interval = 1800

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time
    return str(time)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    return 

def stop():
    pass

def reset():
    pass

# define event handler for timer with 0.1 sec interval
def interval01():
    pass # agregar función para agregar un seundo al intervalo

# define draw handler
def timer_draw_handler(canvas):
    canvas.draw_text(format(), position, 24, "White")
    
# define handler timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y


# button handlers
def start_btn_handler():
    pass

def stop_btn_handler():
    pass

def reset_btn_handler():
    pass

# create frame
frame = simplegui.create_frame('Stopwatch: The Game', width, height)

# hander register
frame.set_draw_handler(timer_draw_handler)
start_button = frame.add_button('Start', start_btn_handler, 80)
stopt_button = frame.add_button('Stop', stop_btn_handler, 80)
reset_button = frame.add_button('Reset', reset_btn_handler, 80)
timer = simplegui.create_timer(interval, tick)

# start frame

frame.start()
timer.start()

# Please remember to review the grading rubric
