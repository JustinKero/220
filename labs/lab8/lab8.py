"""
Name: Justin Kerosetz
lab8.py
"""


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "\n")
            i += 1

def hourly_wages(infile, outfile):
    infile = open("hourly_wages.txt", "r")
    outfile = open("hourly_output.txt", "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write(" ".join(new_line) + "\n")

def calc_check_sum(ISBN):
    sum = 0
    ISBN = str(ISBN)
    for i in range(len(ISBN)):
        num = int(ISBN[i]) * (10-i)
        sum += num
    return sum % 11

def send_message(file, friend):
    infile = open(file + "", "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line)

def encode(message, key):
    encryption = ""
    for i in message:
        encryption += chr((ord(i) - 97 + key) % 26 + 97)
    return encryption

def send_safe_message(file, friend, key):
    infile = open(file + "", "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "\n")

def encode_better(sentence, key):
    encryption = ""
    for i in range(len(sentence)):
        s = ord(sentence[i])
        k = ord(key[i % len(key)])
        k = k - 97
        s = s + k
        new_s = chr(s)
        encryption += new_s
    return encryption

def send_untrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    padfile = open(pad, "r")
    for line in infile:
        new_line = encode_better(line, padfile.read())
        outfile.write(new_line + "\n")

def main():
    # number_words("walrus.txt", "new_walrus.txt")
    # hourly_wages("hourly_wages.txt", "hourly_output.txt")
    # print(calc_check_sum(2172946520))
    # send_message("name.txt", "John")
    # send_safe_message("Bob.txt", "john", 3)
    send_untrackable_message("name.txt", "pad", "pad_file.txt")
    pass


main()