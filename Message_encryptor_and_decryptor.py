import numpy as np
import itertools
import math


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            # print(i)
            # print("False")
            return False
        elif num == 3:
            # print(i)
            # print("true")
            return True
    return True


# Makes sure that the user choses either E or D
conditionToEncode = input("Would you like to encrypt(enter an E) or decrypt(enter a D) a message? ")
while conditionToEncode.lower() != "e" and conditionToEncode.lower() != "d":
    conditionToEncode = input("Please enter either a letter E or D: ")

if conditionToEncode.lower() == "d":
    # Defines the message matrix
    messageSize = int(input("How many numbers are in the message?: "))
    messageSizeExtra = messageSize
    messageSplit = int(input("How many rows does the square encoding matrix have?: "))
    # This while loop just adds spaces to the end of the message to make the message and the matrix compatible
    while messageSize % messageSplit != 0:
        messageSizeExtra = messageSizeExtra + 1
    # Makes the values of the matrix equal to the user input
    counter = 0
    rowNumMessage = int(messageSize / messageSplit)
    messageMatrix = np.empty([rowNumMessage, messageSplit], dtype='int')
    for i in range(rowNumMessage):
        for j in range(messageSplit):
            counter = counter + 1
            if counter <= messageSize:
                valueM = int(input("Enter value number {} for the message: ".format(counter)))
                messageMatrix[i][j] = valueM
            if counter > messageSize:
                messageMatrix[i][j] = 0
    # End up with a messageMatrix with numbers of the message

if conditionToEncode.lower() == "e":
    # Defines the message matrix (characters)
    message = input("Enter the message to encode: ")
    messageSize = len(message)
    # while isPrime(messageSize) == True:
    # messageSize = int(input("The encoding process cannot be done with a prime number of characters(enter spaces after the message to make the number of characters not prime): "))
    messageSplit = int(input(
        "How many rows does the square encoding matrix have?(it should be a factor of the size of the message): "))
    # This while loop just adds spaces to the end of the message to make the message and the matrix compatible
    while messageSize % messageSplit != 0:
        message = message + " "
        messageSize = len(message)
    # messageNumbers is the array of the characters of the message converted to numbers
    messageNumbers = np.empty([messageSize], dtype='int')
    # i is the indexing variable and char is the python loop variable, enumerate is just fancy syntax for that
    for i, char in enumerate(message):
        # If the character is a space, make the number 0 instead of 32
        if char == " ":
            messageNumbers[i] = (0)
        # Otherwise, make the number the coresponding value of the alphabet(a = 1, b = 2, c = 3...)
        else:
            messageNumbers[i] = (ord(char) - 96)
    # This while loop makes sure that the encoding matrix and the subsets of the message are compatible for multiplication
    while messageSize % messageSplit != 0:
        condOne = input(
            "The encoding process cannot occur since the size of the encoding matrix was not a factor of the message size. Please either change the encoding matrix dimension(enter an E) or change the message matrix dimension(enter an M): ")
        while condOne.lower() != "e" and condOne.lower() != "m":
            cond1 = input("Please enter either an E or an M: ")
        if condOne.lower() == "e":
            messageSplit = int(input(
                "How many rows should the square encoding matrix have?(it should be a factor of the size of the message): "))
        if condOne.lower() == "m":
            messageSize = int(input("How many numbers are in the message?(cannot be prime): "))
            while isPrime(messageSize) == True:
                messageSize = int(input("The encoding process cannot be done with a prime number: "))
    rowNumMessage = int(messageSize / messageSplit)
    messageMatrix = messageNumbers.reshape(rowNumMessage, messageSplit)

# Defines the encoding matrix
dimofEncMatix = messageSplit
encodingMatrix = np.empty([dimofEncMatix, dimofEncMatix], dtype='int')
# Makes the values of the matrix equal to the user input
for i in range(dimofEncMatix):
    for j in range(dimofEncMatix):
        valueE = int(input("Enter the value in row {} and column {} of the encoding matrix: ".format(i, j)))
        encodingMatrix[i][j] = valueE

# Actual code for encrypting and decrypting
if conditionToEncode.lower() == "e":
    print("You will be encrypting the numbers")
    print(messageMatrix.reshape(messageSize))
    encodedMessage = np.dot(messageMatrix, encodingMatrix).reshape(messageSize)
    print("The encoded numbers of the message are")
    print(encodedMessage)
if conditionToEncode.lower() == "d":
    print("You will be decrypting the numbers")
    print(messageMatrix.reshape(messageSize))
    decodedMessage = np.dot(messageMatrix, np.linalg.inv(encodingMatrix)).reshape(messageSize)
    print(np.linalg.inv(encodingMatrix))
    print("The decoded numbers of the message are")
    decodedMessage = decodedMessage.astype(int)
    print(decodedMessage)
    print("The message says: ")
    print()
    for number in decodedMessage:
        if number != 0:
            print(chr(number + 96), end='')
        if number == 0:
            print(" ", end='')
