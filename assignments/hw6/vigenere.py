from graphics import *

def draw_button(point_1, point_2, button_text, win):
    outline = Rectangle(point_1, point_2)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)

def input(message):
    message = message.upper()
    message = message.replace(" ", "")
    return message

def code(message, keyword):
    msg = input(message)
    word = input(keyword)
    keylist = []
    for i in range(len(msg)):
        s = msg[i]
        k = i % len(word)
        con = ord(s) - 65
        wordcon = ord(word[k]) - 65
        encode = chr(((con + wordcon) % 26) + 65)
        keylist.append(encode)
    text = "".join(keylist)
    return text

def main():
    win = GraphWin("Greeting", 600, 400)
    win.setCoords(0, 0, 9, 9)
    draw_button(Point(4, 5), Point(5, 6), "Encode", win)
    code_message = Text(Point(1.9, 8), "Message to code")
    code_message.draw(win)
    key_message = Text(Point(2, 7.25), "Enter Keyword")
    key_message.draw(win)

    sentence = Entry(Point(5.5, 8), 30)
    sentence.setText("")
    sentence.draw(win)
    sen = str(sentence)

    keyword = Entry(Point(4.15, 7.25), 10)
    keyword.setText("")
    keyword.draw(win)
    key = str(keyword)

    win.getMouse()
    result_message = Text(Point(4, 4), "Resulting Message")
    result_message.draw(win)
    result = Text(Point(3.5, 3), code(sen, key))
    result.draw(win)
    close = Text(Point(4, 1), "Click anywhere to close")
    close.draw(win)
    draw_button(Point(20,20), Point(20,20), "", win)

    win.getMouse()
    win.close()
if __name__ == '__main__':
    main()