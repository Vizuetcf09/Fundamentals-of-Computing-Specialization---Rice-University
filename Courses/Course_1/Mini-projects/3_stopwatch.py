# Stopwatch: The Game

import simplegui
import random

# define global variables
time = 0
#successful_stops = 0
#total_stops = 0
position = [60, 110]
#score_position = [150, 30]
width = 200
height = 200
interval = 100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time
    global A
    global B
    global C
    global D
    global format_counter
    
    A = (time // 1000) % 10
    B = (time // 100) % 10
    C = (time // 10) % 10
    D = time % 10
    
    if B >= 6:
        B = 0
        A += 1
    
    format_counter = str(A) + ":" + str(B) + str(C) + "." + str(round(D)) 
    return format_counter
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()

#def stop():
#    global total_stops, successful_stops
#    if timer.is_running():
#        timer.stop()
#        total_stops += 1
#        if time % 10 == 0:
#            successful_stops += 1

def reset():
    global time
    time = 0

#def reset():
#    global time, successful_stops, total_stops
#    time = 0
#    successful_stops = 0
#    total_stops = 0

# define draw handler
def timer_draw_handler(canvas):
    canvas.draw_text(format(), position, 24, "White")
    #    canvas.draw_text(f"{successful_stops}/{total_stops}", score_position, 20, "Green")
    
# define handler timer
def tick():
    global time 
    time += 1
    return

# button handlers
def start_btn_handler():
    start()

def stop_btn_handler():
    stop()

def reset_btn_handler():
    reset()

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

# Please remember to review the grading rubric
