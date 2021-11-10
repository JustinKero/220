'Justin Kerosetz'
'lab11.py'
from random import *

wordList = "list.txt"
def getWords(wordList):
    file = open(wordList, "r")
    wlist = []
    for line in file:
        word = line[0:]
        wlist.append(word.strip())
    return wlist

def pickWord(words):
    pos = randint(0, len(words))
    secret_word = words[pos]
    return secret_word

def guessedWord(secret_word, guessed_letters, guessed_word, turn_count, letter):
    check = False
    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False

def wordSpelled(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    return False

def guessedLetter(guessed_letters, turn_count, secret_word, guessed_word):
    letter = input("Enter a letter: ")
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            while letter == ch:
                letter = input("Already used that letter, Pick a different letter: ")
                check = False
    return guessedWord(secret_word, guessed_letters, guessed_word, turn_count, letter)

def printBoard(guessed_word, turn_count, guessed_letters):
    print("----------",)
    print(guessed_word)
    print()
    print("Turn count", turn_count)
    print("Guessed Letters", guessed_letters)

def playGame():
    turn_count = 0
    sw = pickWord(getWords(wordList))
    guessed_word = ["_"] * len(sw)
    guessed_letters = []
    printBoard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordSpelled(guessed_word, sw):
        if guessedLetter(guessed_letters, turn_count, sw, guessed_word) is False:
            turn_count += 1
            printBoard(guessed_word, turn_count, guessed_letters)
        else:
            printBoard(guessed_word, turn_count, guessed_letters)

    if turn_count >= 7:
        print("Game over. You Lose!")
    else:
        print("You Won!")

def main():
    playGame()
    # getWords("list.txt")
main()