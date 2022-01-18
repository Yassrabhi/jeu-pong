
import turtle as t
class Joueur1:
    def __init__(self):
        joueur1 = t.Turtle()
        joueur1.speed(0)
        joueur1.shape('square')
        joueur1.color(255,140,55)
        joueur1.shapesize(stretch_wid=5, stretch_len=1)
        joueur1.penup()
        joueur1.goto(-350, 0)