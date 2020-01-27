import numpy as np
import itertools
import math

np.set_printoptions(suppress=True)

# Makes sure that the user chooses either E or D
conditionToEncode = input("Would you like to encrypt(enter an E) or decrypt(enter a D) a message? ")
while conditionToEncode.lower() != "e" and conditionToEncode.lower() != "d":
    conditionToEncode = input("Please enter either a letter E or D: ")
messageSplit = int(input("How many rows does the square encoding matrix have?: "))

# Makes the values of the matrix equal to the user input
encodingValues = input("Enter the values of the encoding matrix in one line: ")
encodingMatrix = np.asarray(encodingValues.split(" "), dtype='int').reshape(messageSplit, messageSplit)

if conditionToEncode.lower() == "d":
    # Defines the message matrix
    messageSize = int(input("How many numbers are in the message?: "))
    messageSizeExtra = messageSize
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
            messageNumbers[i] = 0
        # Otherwise, make the number the corresponding value of the alphabet(a = 1, b = 2, c = 3...)
        else:
            messageNumbers[i] = ((ord(char) - 96) + (encodingMatrix[0][0] % 26))
    rowNumMessage = int(messageSize / messageSplit)
    messageMatrix = messageNumbers.reshape(rowNumMessage, messageSplit)


def factor(matrix):
    meanMatrix = np.round(np.mean(matrix))
    if meanMatrix % 2 == 0:
        return 2
    else:
        return 3


# Actual code for encrypting and decrypting
encodedMessage = None

if conditionToEncode.lower() == "e":
    if factor(encodingMatrix) == 2:
        encodedMessage = np.matmul(messageMatrix, np.linalg.matrix_power(encodingMatrix, 2)).reshape(messageSize)
    else:
        encodedMessage = np.matmul(messageMatrix, np.linalg.matrix_power(encodingMatrix, 3)).reshape(messageSize)
    print("The encoded numbers of the message are")
    print(encodedMessage)

decodedMessage = None
invEncodingMatrix = None

if conditionToEncode.lower() == "d":
    if factor(encodingMatrix) == 2:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 2))
        decodedMessage = np.around(np.matmul(messageMatrix, invEncodingMatrix).reshape(messageSize))
    else:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 3))
        decodedMessage = np.around(np.matmul(messageMatrix, invEncodingMatrix).reshape(messageSize))
    print("The decoded numbers of the message are")
    decodedMessage = decodedMessage.astype(int)
    for i in range(messageSize):
        if decodedMessage[i] != 0:
            decodedMessage[i] = decodedMessage[i] - (encodingMatrix[0][0] % 26)

    print(decodedMessage)
    print("The message says: ")
    for number in decodedMessage:
        if number != 0:
            print(chr(number + 96), end='')
        if number <= 0:
            print(" ", end='')
