import turtle
import random
import pygame
import webbrowser
import math

# Initialize pygame mixer for sound
pygame.mixer.init()

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 2
ball.dy = 2

# Sound mapping using pygame
def play_sound(color):
    sounds = {
        "red": "red.mp3",
        "orange": "orange.mp3",
        "yellow": "yellow.mp3",
        "green": "green.mp3",
        "blue": "blue.mp3"
    }
    if color in sounds:
        pygame.mixer.Sound(sounds[color]).play()

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for row in range(5):
    for col in range(-5, 6):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(col * 70, 200 - row * 30)
        bricks.append(brick)

# Paddle movement
def move_left():
    x = paddle.xcor() - 30  # Decrease by smaller amount for smoother movement
    if x > -350:
        paddle.setx(x)

def move_right():
    x = paddle.xcor() + 30  # Decrease by smaller amount for smoother movement
    if x < 350:
        paddle.setx(x)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Reset the game
def reset_game():
    global ball, bricks, fall_count
    ball.goto(0, -230)
    ball.dx = 2
    ball.dy = 2
    fall_count = 0
    for brick in bricks:
        brick.goto(1000, 1000)
    bricks.clear()
    for row in range(5):
        for col in range(-5, 6):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(colors[row])
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(col * 70, 200 - row * 30)
            bricks.append(brick)

screen.onkeypress(reset_game, "r")

fall_count = 0

# Display fall count and ball speed
info_display = turtle.Turtle()
info_display.hideturtle()
info_display.color("white")
info_display.penup()
info_display.goto(-350, 260)
info_display.write(f"Falls: {fall_count}  Speed: {ball.dx}", align="left", font=("Arial", 16, "normal"))

# Game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Ball collision with paddle
    if (ball.ycor() < -240 and ball.ycor() > -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.dy *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1

    # Ball collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 25:
            play_sound(brick.color()[0])
            brick.goto(1000, 1000)  # Move brick off screen
            bricks.remove(brick)
            ball.dy *= -1
            break

    # Ball falls below screen
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy = 2
        fall_count += 1

    # Update the display text with current fall count and ball speed
    info_display.clear()
    info_display.write(f"Falls: {fall_count}  Speed: {round(ball.dx, 2)}", align="left", font=("Arial", 16, "normal"))

    if not bricks:
        screen.textinput("Game Over", f"You Win! Ball fell {fall_count} times. Press OK to exit.")
        webbrowser.open("https://www.youtube.com/watch?v=HHEOn2Jdyx8")  # Open YouTube link
        break

turtle.done()
