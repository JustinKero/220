"""
Name: Justin Kerosetz
lab6.py
"""
def name_reverse():
    name = str(input("Enter your name First-Last: "))
    fullname = name.split()
    firstname = fullname[0]
    lastname = fullname[1]
    print(lastname + (", ") + firstname)

def company_name():
    website = str(input("Enter the three part website domain name: "))
    websitename = website.split(".")
    company = websitename[1]
    print(company)

def initials():
    initial = eval(input("How many names will there be?: "))
    for i in range(initial):
        firstname = str(input("Enter the first name of " + str(i + 1) + ": " ))
        lastname = str(input("Enter " + str(firstname) + "'s last name: "))
        name = (firstname[0], lastname[0])
        print(str(firstname) + "'s initials are " + str(name))
def names():
    name = str(input("Enter names first and last serperated by commas: "))
    namesplit = name.split(", ")
    print("The initials are: ", end=" ")
    for i in (namesplit):
        names = i.split(" ")
        firstname = names[0]
        lastname = names[1]
        fullname = (firstname[0] + lastname[0])
        print(fullname, end=" ")
    print(" ")

def thirds():
    w = eval(input("Enter how many sentences there will be: "))
    for i in range(w):
        sentence = str(input("Enter the sentence: "))
        length = len(sentence)
        third = sentence[2:length:3]
        print(third)

def word_average():
    w = eval(input("How many sentences will there be: "))
    for i in range(w):
        total = 0
        sentence = str(input("Enter the sentence: "))
        word = sentence.split(" ")
        totalword = len(word)
        for _ in word:
            totalcount = len(_)
            total += totalcount
        average = total / totalword
        print(average)

def pig_latin():
    sentence = input("Enter sentence: ")
    sentencelower = sentence.lower()
    sentencesplit = sentencelower.split(" ")
    for word in sentencesplit:
        code = word[1:] + word[0] + "ay"
        print(code, end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

if __name__ == '__main__':
    main()