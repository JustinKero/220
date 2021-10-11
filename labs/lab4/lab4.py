"""
Name: Justin Kerosetz
lab4.py
"""

from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move Square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), (20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        cloneshape = shape.clone()
        cloneshape.move(dx, dy)
        cloneshape.draw(win)
        shape.move(dx, dy)

    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Draw a Square")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, .5), "Click on two points")
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)

    rectangle = Rectangle(p1, p2)
    rectangle.setFill("red")
    rectangle.setOutline("blue")
    rectangle.draw(win)
    message.setText("Click anywhere to exit")
    win.getMouse()
    win.close()

def circle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Circle", win_width, win_height)
    message = Text(Point(350, 450), "Click to find the circumference")
    message.draw(win)
    center = win.getMouse()
    point = win.getMouse()


    dx = point.getX() - center.getX()
    dy = point.getY() - center.getY()

    radpoint = Point(250, 100)
    radius = math.sqrt(dx ** 2 + dy ** 2)
    c = Circle(radius, 30)
    radiustext = Text(radpoint, "The radius is: " + str(radius))
    c.setFill("green")
    c.setOutline("blue")
    c.draw(win)
    radiustext.draw(win)

    message.setText("Click anywhere to exit")
    win.getMouse()
    win.close()

def main():
    squares()
    rectangle()
    circle()



main()
