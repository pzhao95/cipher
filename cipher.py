# assignment: programming assignment 4
# author: Peter Wang Zhao
# date: 11/9/2021
# file: cipher.py is a program that (put the description of the program)
# input: (put input description)
# output: (put output description)
# read text from a file and return text as a string
def readfile(filename):
   #write your code here
    message = ""
    f = open(filename, "r")
    message = f.read()
    f.close()
    return message
# write a string (message) to a file
def writefile(message, filename):
    # place a file location
    f = open(filename, "w+")
    f.write(message)
    f.close()

    #write your code here
# make a list (tuple) of letters in the English alphabet
def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   #print (alphabet)
   return alphabet
# encode text letter by letter using a Caesar cipher
# return a list of encoded symbols
def encode(plaintext):
   plaintext = plaintext.upper()
   shift = 3
   ciphertext = []
   alphabet = make_alphabet()
   length = len(alphabet)
   for char in plaintext:
       found = False
       for i in range(length):
           if char == alphabet[i]:
               letter = alphabet[(i + shift) % length]
               ciphertext.append(letter)
               found = True
               break
       if not found:
           ciphertext.append(char)
   return ciphertext
# decode text letter by letter using a Caesar cipher
# return a list of decoded symbols
# check how the function encode() is implemented
# your implementation of the function decode() can be very similar
# to the implementation of the function encode()
def decode(text):
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in text:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext
   #write your code here
# convert a list into a string
# for example, the list ["A", "B", "C"] to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] to the
string = "HOW ARE YOU?"
def to_string(text):
    s = ""
    for val in text:
        s = s + val
    #write your code here
    return s
# main program
try:
    pass
except:
    pass
   #write your code here
while True:
    print("\nWould you like to encode or decode the message?")
    ch = input("Type E to encode, D to decode, or Q to quit:\n")
    if ch == 'E' or ch == 'e':
        filename = input('Please enter a file for reading:\n')
        msg = readfile(filename)
        filename2 = input('Please enter a file for writing:\n')
        print("\nPlaintext:")
        print(msg)
        enc = encode(msg)
        print("\nCiphertext:")
        str = to_string(enc)
        print(str)
        writefile(str, filename2)
    elif ch == 'D' or ch == 'd':
        filename = input('Please enter a file for reading:\n')
        msg = readfile(filename)
        filename2 = input('Please enter a file for writing:\n')
        print("\nCiphertext:")
        print(msg)
        dec = decode(msg)
        print("\nPlaintext:")
        str = to_string(dec)
        print(str)
        writefile(str, filename2)
    elif ch == 'Q' or ch == 'q':
        print("\nGoodbye!")
        quit()
