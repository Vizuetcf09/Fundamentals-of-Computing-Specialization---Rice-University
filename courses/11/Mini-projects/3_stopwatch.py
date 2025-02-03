# Stopwatch: The Game

# import simplegui

# define global variables
time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    pass

def stop():
    pass

def reset():
    pass
# define event handler for timer with 0.1 sec interval
def interval01():
    pass

# define draw handler
def timer_draw_handler():
    pass

# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200)

# register event handlers
def start_btn_handler():
    pass

def stop_btn_handler():
    pass

def reset_btn_handler():
    pass

# start frame
start_button = frame.add_button('Start', start_btn_handler, 80)
stopt_button = frame.add_button('Stop', stop_btn_handler, 80)
reset_button = frame.add_button('Reset', reset_btn_handler, 80)

frame.start()

# Please remember to review the grading rubric
