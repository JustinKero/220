
from random import randint
import math
from graphics import *
import time, random
import keyboard

X_Res = 100
Y_Res = 100

def distance(p1, p2):
    cx1 = p1.getX()
    cy1 = p1.getY()
    cx2 = p2.getX()
    cy2 = p2.getY()
    dist = math.sqrt((cy1 - cy2) ** 2 + (cx1 - cx2) ** 2)
    dist = int(dist)
    return dist

def did_collide(C1, C2):
    center1 = C1.getCenter()
    center2 = C2.getCenter()
    radius1 = C1.getRadius()
    radius2 = C2.getRadius()
    collide_dist = distance(center1, center2)

    if collide_dist <= (radius1 + radius2):
        return True
    else:
        return False


def hit_vertical(ball, win):
    if (ball.getCenter().getY() - ball.getRadius()) <= 0 or (ball.getCenter().getY() + ball.getRadius()) >= Y_Res:
        return True
    else:
        return False

def hit_horizontal(ball, win):
    if (ball.getCenter().getX() - ball.getRadius()) <= 0 or (ball.getCenter().getX() + ball.getRadius()) >= X_Res:
        return True
    else:
        return False

def get_random(move_amount):
    small_move = -move_amount
    big_move = +move_amount
    return randint(small_move, big_move)

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return color_rgb(red, green, blue)


def bounce_main():
    win_Width = 400
    win_Height = 400

    win = GraphWin("Bumper", win_Width, win_Height)
    win.setCoords(0, 0, X_Res, Y_Res)


    # Circle 1
    point1 = Point(40, 40)
    circle1 = Circle(point1, 5)
    circle1.draw(win)

    # Circle 2
    point2 = Point(15, 15)
    circle2 = Circle(point2, 5)
    circle2.draw(win)

    delay = .03
    d1x = get_random(4)
    d1y = get_random(4)
    d2x = get_random(4)
    d2y = get_random(4)

    circle1.setFill(get_random_color())
    circle2.setFill(get_random_color())

    n = 0
    while n < 1:

        collide_vert1 = hit_vertical(circle1, win)
        if collide_vert1 == True:
            d1y = -d1y

        collide_horiz1 = hit_horizontal(circle1, win)
        if collide_horiz1 == True:
            d1x = -d1x

        collide_vert2 = hit_vertical(circle2, win)
        if collide_vert2 == True:
            d2y = -d2y

        collide_horiz2 = hit_horizontal(circle2, win)
        if collide_horiz2 == True:
            d2x = -d2x

        collide_balls = did_collide(circle1, circle2)
        if collide_balls == True:
            d1x = -d1x
            d1y = -d1y
            d2x = -d2x
            d2y = -d2y


        circle1.move(d1x, d1y)
        circle2.move(d2x, d2y)

        if keyboard.is_pressed("q"):
            win.close()

        time.sleep(delay)

def main():
    bounce_main()

if __name__ == '__main__':
    main()
