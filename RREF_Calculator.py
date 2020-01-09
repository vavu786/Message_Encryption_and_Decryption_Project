import numpy as np


def rrefMatrix(inputMatrix):
    NUMROWS = len(inputMatrix[:, 0])
    NUMCOLS = len(inputMatrix[0, :])

    # Multiplies a row and a scalar
    def multiplyRow(multiplier, rowNum):
        inputMatrix[rowNum, :] *= multiplier

    # Adds two rows and replaces that sum into the row inputed last
    def addRows(sourceRow, targetRow):
        inputMatrix[targetRow, :] += inputMatrix[sourceRow, :]

    # Makes an input column into RREF
    def RREF(colNum):
        for i in range(NUMCOLS - 1):
            # Makes the diagonal entry 1 in that column
            if inputMatrix[colNum][colNum] != 1.0:
                if (np.count_nonzero(inputMatrix[i, :])) == 0:
                    return 0
                if inputMatrix[colNum][colNum] == 0:
                    for i in range(NUMCOLS - 1):
                        if inputMatrix[i][colNum] != 0:
                            addRows(i, colNum)
                    if inputMatrix[colNum][colNum] == 0:
                        return 2
                # print ("Divide row {} by {}(beginning): ".format(colNum, inputMatrix[colNum][colNum]))
                multiplyRow(1 / inputMatrix[colNum][colNum], colNum)
                # print(inputMatrix)
            # The if statement says that if the [colNum][colNum] is not 1 or any other value is not 0, run the RREF code
            if inputMatrix[i][colNum] != 0:
                # Checks if there is a row of zeros
                if (np.count_nonzero(inputMatrix[i, :])) == 0:
                    return 0
                if inputMatrix[colNum][colNum] == -1:
                    multiplyRow(-1, colNum)
                # Multiplies the row with a 1 by the negative of the entry you are trying to make 0
                # print ("Multiply row {} by {}: ".format(colNum, -inputMatrix[i][colNum]))
                multiplyRow(-inputMatrix[i][colNum], colNum)
                # print (inputMatrix)
                # Adds the two rows, making one entry zero
                # print ("Add row {} and row {} and replace that into row {}: ".format(i, colNum, i))
                addRows(colNum, i)
                # print (inputMatrix)
            # Makes the diagonal entry 1 again
            if inputMatrix[colNum][colNum] != 1.0 and inputMatrix[colNum][colNum] != 0.0:
                if (np.count_nonzero(inputMatrix[i, :])) == 0:
                    return 0
                if np.count_nonzero(inputMatrix[i, :] == 1 and inputMatrix[NUMROWS - 1][NUMCOLS - 1] != 0):
                    return 2
                # print ("Divide row {} by {}(end): ".format(colNum, inputMatrix[colNum][colNum]))
                multiplyRow((1 / inputMatrix[colNum][colNum]), colNum)
                # print(inputMatrix)
            if i == (NUMCOLS - 2):
                return 1

    # print("Your Matrix is: \n{}".format(inputMatrix))
    for i in range(NUMCOLS - 1):
        ret = RREF(i)
        if ret == 0:
            # print("The function needs to be parametrized, since there is a row of all zeros")
            break
        if ret == 2:
            # print("The matrix does not have a RREF, since there is a column of all zeros")
            break
    if ret == 1:
        pass
        return inputMatrix
        # print("RREF of your Matrix is: \n{}".format(inputMatrix))
