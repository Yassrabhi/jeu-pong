
import turtle as t
class Ball:
    def __init__(self):
        ball = t.Turtle()
        ball.speed(0)
        ball.shape('circle')
        ball.color('yellow')
        ball.penup()
        ball.goto(0, 0)
        ball_dx = 1.5
        ball_dy = 1.5