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


# Makes sure that the user chooses either E or D
conditionToEncode = input("Would you like to encrypt(enter an E) or decrypt(enter a D) a message? ")
while conditionToEncode.lower() != "e" and conditionToEncode.lower() != "d":
    conditionToEncode = input("Please enter either a letter E or D: ")

if conditionToEncode.lower() == "d":
    # Defines the message matrix
    messageSize = int(input("How many numbers are in the message?: "))
    messageSizeExtra = messageSize
    messageSplit = int(input("How many rows does the square encoding matrix have?: "))
    # This while loop just adds spaces to the end of the message to make the message and the matrix compatible
    while messageSizeExtra % messageSplit != 0:
        messageSizeExtra = messageSizeExtra + 1
    # Makes the values of the matrix equal to the user input
    counter = 0
    rowNumMessage = int(messageSizeExtra / messageSplit)
    # messageMatrix = np.empty([rowNumMessage, messageSplit], dtype='int')
    messageValues = input("Enter the numbers of the message, each separated by a space: ")
    messageMatrix = np.asarray(messageValues.split(" "), dtype='int').reshape(rowNumMessage, messageSplit)
    # End up with a messageMatrix with numbers of the message

if conditionToEncode.lower() == "e":
    # Defines the message matrix (characters)
    message = input("Enter the message to encode: ")
    messageSize = len(message)
    messageSplit = int(input("How many rows does the square encoding matrix have?: "))
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
        # Otherwise, make the number the corresponding value of the alphabet(a = 1, b = 2, c = 3...)
        else:
            messageNumbers[i] = (ord(char) - 96)
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


def factor(matrix):
    meanMatrix = np.round(np.mean(matrix))
    if meanMatrix % 2 == 0:
        return 2
    else:
        return 3


# Actual code for encrypting and decrypting
if conditionToEncode.lower() == "e":
    if factor(encodingMatrix) == 2:
        encodedMessage = np.matmul(messageMatrix, np.linalg.matrix_power(encodingMatrix, 2)).reshape(messageSize)
        print("should be 2")
    else:
        encodedMessage = np.matmul(messageMatrix, np.linalg.matrix_power(encodingMatrix, 3)).reshape(messageSize)
        print("should be 3")

    print("messageMatrix")
    print(messageMatrix)
    print(np.linalg.matrix_power(encodingMatrix, 2))
    print("The encoded numbers of the message are")
    print(encodedMessage)
decodedMessage = None
invEncodingMatrix = None
if conditionToEncode.lower() == "d":
    if factor(encodingMatrix) == 2:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 2))
        decodedMessage = np.matmul(messageMatrix, invEncodingMatrix).reshape(messageSize)
    else:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 3))
        decodedMessage = np.matmul(messageMatrix, invEncodingMatrix).reshape(messageSize)
    print(invEncodingMatrix)
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

# TODO The error could be rounding errors
'''
m1 = np.array([[13, 5, 5], [20, 0, 13], [5, 0, 13], [15, 14, 4], [1, 25, 0]])
m2 = np.array([[5, -6, -12], [1, 0, -11], [-2, 1, 15]])
print(m1)
print(m2)
print(m1 @ m2)
'''