import simplegui
import random

# Global variables
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_pos = 100
paddle2_pos = 100
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# Constants
BALL_RADIUS = 20
PADDLE_WIDTH = 8
PADDLE_HEIGHT = 80
WIDTH = 600
HEIGHT = 400
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PAD_VELOCITY = 5

# Spawn ball function
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [HALF_WIDTH, HALF_HEIGHT]  # Start in the center of the screen
    
    # Randomize ball velocity
    horizontal_velocity = random.randrange(120, 240)
    vertical_velocity = random.randrange(60, 180)
    
    if direction == "RIGHT":
        ball_vel = [horizontal_velocity, -vertical_velocity]
    elif direction == "LEFT":
        ball_vel = [-horizontal_velocity, -vertical_velocity]

# New game function
def new_game():
    global score1, score2
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")  # Start the ball towards the right

# Draw handler
def draw(canvas):
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2
    
    # Move ball and update its position
    ball_pos[0] += ball_vel[0] // 60
    ball_pos[1] += ball_vel[1] // 60
    
    # Ball collision with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]  # Bounce off the walls
    
    # Ball collision with paddles (left paddle)
    if ball_pos[0] <= BALL_RADIUS + PADDLE_WIDTH and paddle1_pos < ball_pos[1] < paddle1_pos + PADDLE_HEIGHT:
        ball_vel[0] = -ball_vel[0]  # Bounce off left paddle
        ball_vel[0] *= 1.1  # Increase speed by 10%
    
    # Ball collision with paddles (right paddle)
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PADDLE_WIDTH and paddle2_pos < ball_pos[1] < paddle2_pos + PADDLE_HEIGHT:
        ball_vel[0] = -ball_vel[0]  # Bounce off right paddle
        ball_vel[0] *= 1.1  # Increase speed by 10%

    # Ball out of bounds (score)
    if ball_pos[0] <= BALL_RADIUS:
        score2 += 1
        spawn_ball("RIGHT")
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball("LEFT")
    
    # Draw paddles
    canvas.draw_line([PADDLE_WIDTH, paddle1_pos], [PADDLE_WIDTH, paddle1_pos + PADDLE_HEIGHT], PADDLE_WIDTH, "White")
    canvas.draw_line([WIDTH - PADDLE_WIDTH, paddle2_pos], [WIDTH - PADDLE_WIDTH, paddle2_pos + PADDLE_HEIGHT], PADDLE_WIDTH, "White")
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # Draw scores
    canvas.draw_text(str(score1), [WIDTH // 4, 50], 40, "White")
    canvas.draw_text(str(score2), [3 * WIDTH // 4, 50], 40, "White")
    
    # Update paddles' positions
    if 0 <= paddle1_pos + paddle1_vel <= HEIGHT - PADDLE_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= paddle2_pos + paddle2_vel <= HEIGHT - PADDLE_HEIGHT:
        paddle2_pos += paddle2_vel

# Key handlers
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_VELOCITY
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_VELOCITY
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_VELOCITY
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_VELOCITY

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start the game
new_game()
frame.start()
