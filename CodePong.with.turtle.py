

import turtle as t
import os

# Score

player_a_score = 0
player_b_score = 0

win = t.Screen()  # creation window.
win.title("Ping-Pong Game")  # donner le nom du jeu.
win.bgcolor('black')  # couleur du HomeScreen
win.setup(width=900, height=600)  # dimension du game.
win.tracer(0)  # which speed up's the game.

# creation du Padel gauche.

paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# creation du Padel droite.

paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.color('green')
paddle_right.penup()
paddle_right.goto(350, 0)

# creation de la ball.

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball_dx = 1.5  #Configuration des pixels pour le mouvement de la balle.
ball_dy = 1.5

# Creation du Score .

pen = t.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0                    Player B: 0 ", align="center", font=('Monaco', 24, "normal"))


# Déplacement de la palette gauche à l'aide du clavier.

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)


# Deplacer le Padel gauche en bas

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)


# deplacer le Padel droite vers le haut

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)


# Deplacer le Padel droite vers le bas.

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)


# Keyboard binding

win.listen()
win.onkeypress(paddle_left_up, "z")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")

# Boucle de jeu principale

while True:
    win.update()  #Cette méthode est obligatoire pour exécuter n'importe quel jeu

    # deplacer la balle
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # mise en place de la frontière

    if ball.ycor() > 290:  #Bordure supérieure droite
        ball.sety(290)
        ball_dy = ball_dy * -1

    if ball.ycor() < -290:  #Bordure supérieure gauche
        ball.sety(-290)
        ball_dy = ball_dy * -1

    if ball.xcor() > 390:  # bordure droite
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if (ball.xcor()) < -390:  # Bordure gauche
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Gérer les collisions avec les padels.

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")