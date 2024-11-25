# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: edeeb
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
        baseText = input("What message do you want to encode?")
        cipherQuestion = int(input("What number do you want to cipher the text by?"))
        finalEncode = ""
        for x in range(len(baseText)):
            letter = alphabet.find(baseText[x])
            if letter == -1:
                letter = alphabet2.find(baseText[x])
            encodedLetter = (letter + cipherQuestion) % 26
            finalEncode += alphabet[encodedLetter]
        print(finalEncode)
        pass

# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    fileQuestion = input("What file do you want to encode?")
    file = open(fileQuestion, 'r')
    fileStr = file.read()
    cipherQuestion = int(input("What number do you want to cipher the text by?"))
    finalEncode = ""
    for x in range(len(fileStr)):
        letter = alphabet.find(fileStr[x])
        if letter == -1:
            letter = alphabet2.find(fileStr[x])
        encodedLetter = (letter + cipherQuestion) % 26
        finalEncode += alphabet[encodedLetter]
    print(finalEncode)
    file.close()
    pass

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    decodemenu = input("Is the key [1] known or [2] unknown?")
    if decodemenu == "1":
        fileQuestion = input("What file do you want to decode?")
        file = open(fileQuestion, 'r')
        fileStr = file.read()
        cipherQuestion = int(input("What is the key?"))
        finalEncode = ""
        for x in range(len(fileStr)):
            letter = alphabet.find(fileStr[x])
            if letter == -1:
                letter = alphabet2.find(fileStr[x])
            encodedLetter = (letter + cipherQuestion) % 26
            finalEncode += alphabet[encodedLetter]
        print(finalEncode)
        file.close()
    if decodemenu == "2":
        decode_unknown_key()
    pass

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
        fileQuestion = input("What file do you want to decode?")
        file = open(fileQuestion, 'r')
        fileStr = file.read()
        for key in range(0, 25):
            finalEncode = ""
            for x in range(len(fileStr)):
                letter = alphabet.find(fileStr[x])
                if letter == -1:
                    letter = alphabet2.find(fileStr[x])
                encodedLetter = (letter + key) % 26
                finalEncode += alphabet[encodedLetter]
            print(finalEncode)
            print(f"Key: {key}")
        file.close()


# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()

