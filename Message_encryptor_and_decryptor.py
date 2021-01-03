"""
input.txt is formatted as follows:
Decryption:
    d or D (char)
    Dimension of encoding matrix (int)
    Values of encoding matrix (space-separated ints)
    Number of letters in message (int)
    Values of the encrypted message (space-separated ints)
Encryption:
    e or E (char)
    Dimension of encoding matrix (int)
    Values of encoding matrix (space-separated ints)
    Message (string)
"""

import numpy as np

np.set_printoptions(suppress=True)


def factor(matrix):
    meanMatrix = np.round(np.mean(matrix))
    if meanMatrix % 2 == 0:
        return 2
    else:
        return 3


def encrypt(originalMessage, encodingMatrix):
    # This while loop just adds spaces to the end of the message to make the message and the matrix compatible
    while len(originalMessage) % len(encodingMatrix) != 0:
        originalMessage = originalMessage + " "

    # originalMessageNumbers is the flat array of the characters of the message converted to numbers
    originalMessageNumbers = np.empty([len(originalMessage)], dtype='int')

    # i is the indexing variable and char is the python loop variable, enumerate is just fancy syntax for that
    for i, char in enumerate(originalMessage):
        # If the character is a space, make the number 0 instead of 32
        if char == " ":
            originalMessageNumbers[i] = 0
        # Otherwise, make the number the corresponding value of the alphabet(a = 1, b = 2, c = 3...)
        else:
            originalMessageNumbers[i] = ((ord(char) - 96) + (encodingMatrix[0][0] % 26))

    # originalMessageMatrix is the shaped matrix of the encoded (right now partially encoded) message numbers
    originalMessageMatrix = originalMessageNumbers.reshape(int(len(originalMessage) / len(encodingMatrix)), len(encodingMatrix))

    # Applies the actual encryption algorithm
    if factor(encodingMatrix) == 2:
        encodedMessage = np.matmul(originalMessageMatrix, np.linalg.matrix_power(encodingMatrix, 2)).reshape(len(originalMessage))
    else:
        encodedMessage = np.matmul(originalMessageMatrix, np.linalg.matrix_power(encodingMatrix, 3)).reshape(len(originalMessage))

    # Converts encrypted numbers into formatted string that decrypt() can take in
    encodedMessageString = ""
    for encryptedNumber in encodedMessage:
        encodedMessageString = encodedMessageString + str(encryptedNumber) + " "
    return encodedMessageString.strip()


def decrypt(messageNumbers, encodingMatrix):
    # Formats messageNumbers to get messageNumbers of type list instead if string
    messageNumbers = messageNumbers.split(" ")

    # encryptedMessageMatrix is a compatible, numpy array of the message numbers
    encryptedMessageMatrix = np.asarray(messageNumbers, dtype='int').reshape(int(len(messageNumbers) / len(encodingMatrix)), len(encodingMatrix))

    # Actual decryption process
    if factor(encodingMatrix) == 2:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 2))
        decodedMessage = np.around(np.matmul(encryptedMessageMatrix, invEncodingMatrix).reshape(len(messageNumbers)))
    else:
        invEncodingMatrix = np.linalg.inv(np.linalg.matrix_power(encodingMatrix, 3))
        decodedMessage = np.around(np.matmul(encryptedMessageMatrix, invEncodingMatrix).reshape(len(messageNumbers)))

    for i in range(len(messageNumbers)):
        if decodedMessage[i] != 0:
            decodedMessage[i] = decodedMessage[i] - (encodingMatrix[0][0] % 26)

    # Converts float array to int array so the numbers can be converted to letters (ex: 6.0 -> 6 -> 'f')
    decodedMessage = decodedMessage.astype(int)

    # Gets printable string of the decrypted message
    decodedMessageString = ""
    for number in decodedMessage:
        if number != 0:
            decodedMessageString = decodedMessageString + chr(number + 96)
        if number == 0:
            decodedMessageString = decodedMessageString + " "

    return decodedMessageString.strip()


def main():
    # User chooses "e" or "d"
    encodeOrDecode = input()

    # Dimension of square encoding matrix
    dimEncodingMatrix = int(input())

    # input() is the values of the encoding matrix in one line
    encodingMatrix = np.asarray(input().split(" "), dtype='int').reshape(dimEncodingMatrix, dimEncodingMatrix)

    # Setup to decode: gets encrypted message and calls decrypt()
    if encodeOrDecode.lower() == "d":
        # Encrypted message numbers, each separated by a space
        messageValues = input()
        decodedMessage = decrypt(messageValues, encodingMatrix)
        print(decodedMessage)

    # Setup to encode: gets original message and calls encrypt()
    if encodeOrDecode.lower() == "e":
        # Message to encode
        message = input()
        encodedMessage = encrypt(message, encodingMatrix)
        print(encodedMessage)


if __name__ == "__main__":
    main()
