from button import Button
from graphics import *
from random import randint

def main():
    win = GraphWin("Three Button Game", 500, 400)
    win.setCoords(0, 0, 10, 10)

    door1 = 1
    door2 = 2
    door3 = 3
    random_number = randint(1, 3)

    butrect1 = Rectangle(Point(2.5, 4), Point(3.5, 3))
    butrect2 = Rectangle(Point(4.5, 4), Point(5.5, 3))
    butrect3 = Rectangle(Point(6.5, 4), Point(7.5, 3))

    b1 = Button(butrect1, "Door 1")
    b2 = Button(butrect2, "Door 2")
    b3 = Button(butrect3, "Door 3")



    b1.draw(win)
    b2.draw(win)
    b3.draw(win)

    msg = Text(Point(5, 8), "I have a secret door")
    secret = Text(Point(5, 2), "Click to choose my door")
    winner = Text(Point(5, 8), "You Win!")
    loser = Text(Point(5, 8), "You Lose!")
    door = Text(Point(5, 2), "Door " + str(random_number) + " is my secret door")

    endgame = False
    clicktoclose = False
    msg.draw(win)
    secret.draw(win)
    while(endgame == False):

        clickpoint = win.getMouse()

        if b1.is_clicked(clickpoint):
            msg.undraw()
            secret.undraw()
            if random_number == door1:
                b1.color_button("green")
                winner.draw(win)

            elif random_number == door2:
                b1.color_button("red")
                loser.draw(win)
                door.draw(win)
            elif random_number == door3:
                b1.color_button("red")
                loser.draw(win)
                door.draw(win)
            clicktoclose = True


        elif b2.is_clicked(clickpoint):
            msg.undraw()
            secret.undraw()
            if random_number == door2:
                b2.color_button("green")
                winner.draw(win)
            elif random_number == door1:
                b2.color_button("red")
                loser.draw(win)
                door.draw(win)
            elif random_number == door3:
                b2.color_button("red")
                loser.draw(win)
                door.draw(win)
            clicktoclose = True


        elif b3.is_clicked(clickpoint):
            msg.undraw()
            secret.undraw()
            if random_number == door3:
                b3.color_button("green")
                winner.draw(win)
            elif random_number == door1:
                b3.color_button("red")
                loser.draw(win)
                door.draw(win)
            elif random_number == door2:
                b3.color_button("red")
                loser.draw(win)
                door.draw(win)
            clicktoclose = True

        if clicktoclose == True:
            closemsg = Text(Point(5, 1), "Click to close")
            closemsg.draw(win)
            if win.getMouse():
               endgame = True

    win.close()
if __name__ == '__main__':
    main()