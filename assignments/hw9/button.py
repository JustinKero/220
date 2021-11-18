from graphics import *

class Button:
    def __init__(self, rect, label):
        self.shape = rect
        self.text = label
        self.pt = Rectangle.getCenter(self.shape)
        self.msg = Text(self.pt, self.text)

    def get_label(self):
        return self.text

    def draw(self, gwin):
        Rectangle.draw(self.shape, gwin)
        self.msg.draw(gwin)

    def undraw(self):
        Rectangle.undraw(self.shape)
        Text.undraw(self.msg)

    def set_label(self, new_label):
        self.text = new_label
        self.msg = Text(self.pt, self.text)

    def is_clicked(self, clickpoint):
        if(self.shape.p1.x < clickpoint.x < self.shape.p2.x) and (self.shape.p1.y > clickpoint.y > self.shape.p2.y):
            return True
        else:
            return False


    def color_button(self, color):
        self.color = color
        Rectangle.setFill(self.shape, self.color)

