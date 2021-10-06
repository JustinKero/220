import turtle

from graphics import *
def main():
    win = GraphWin("Greeting", 700, 500)
    message = Text(Point(350, 150), "Happy Valentines Day!")
    message.draw(win)

    # points for the shapes
    pointA = Point(400, 175)
    pointB = Point(300, 175)
    pointC = Point(255, 200)
    pointD = Point(445,200)
    pointF = Point(350, 300)
    pointG = Point (350, 200)
    point1 = Point (-200, 450)
    point2 = Point (-500, 375)
    pointend = Point (500, 175)

    # Applying points to draw shapes
    circleA = Circle(pointA, 50)
    circleB = Circle(pointB, 50)
    circleC = Circle(pointG, 25)
    triangle = Polygon(pointC, pointD, pointF)


    # Fill and outline Color
    triangle.setFill("red")
    triangle.setOutline("")
    circleA.setFill("red")
    circleA.setOutline("")
    circleB.setFill("red")
    circleB.setOutline("")
    circleC.setFill("red")
    circleC.setOutline("")

    # draw the shapes to the program
    circleA.draw(win)
    circleB.draw(win)
    circleC.draw(win)
    triangle.draw(win)
    for i in range():
        arrow = Line(point1, point2)
        arrow.draw(win)
        print("")

if __name__ == '__main__':
    main()