
import turtle as t
class Ball:
    def __init__(self):
        joueur2 = t.Turtle()
        joueur2.speed(0)
        joueur2.shape('square')
        joueur2.shapesize(stretch_wid=5, stretch_len=1)
        joueur2.color('red')
        joueur2.penup()
        joueur2.goto(350, 0)