import numpy as np
import RREF_Calculator
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-decnums', action='store', type=int, nargs='+')
    parser.add_argument('-encnums', action='store', type=int, nargs='+')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    #Variable dm = decodedMessage; em = encodedMessage
    dm = args.decnums
    em = args.encnums
    #Calculates an encoding matrix dimension compatible for multipliation with the message
    for i in range(len(dm) ):
        split = i+2
        if len(dm)%(split) == 0:
            break
    #Creates the empty encoding matrix to be filled in with the correct values and the matrix to be solved by RREF_Calculator
    encodingMatrix = np.empty([split, split], dtype = 'float')    
    firstColtoRREF = np.array([[dm[0], dm[1], dm[2], em[0]], [dm[3], dm[4], dm[5], em[split]], [dm[6], dm[7], dm[8], em[split*2]]], dtype = 'float')
    secondColtoRREF = np.array([[dm[0], dm[1], dm[2], em[1]], [dm[3], dm[4], dm[5], em[4]], [dm[6], dm[7], dm[8], em[7]]], dtype = 'float')
    thirdColtoRREF = np.array([[dm[0], dm[1], dm[2], em[2]], [dm[3], dm[4], dm[5], em[5]], [dm[6], dm[7], dm[8], em[8]]], dtype = 'float')
    c1 = RREF_Calculator.rrefMatrix(firstColtoRREF)
    c2 = RREF_Calculator.rrefMatrix(secondColtoRREF)
    c3 = RREF_Calculator.rrefMatrix(thirdColtoRREF)
    numcols = len(c1[0,:])
    numrows = len(c1[:,0])
    for i in range(split):
        encodingMatrix[i][0] = c1[i][numcols-1]
        encodingMatrix[i][1] = c2[i][numcols-1]
        encodingMatrix[i][2] = c3[i][numcols-1]
    print(encodingMatrix)

if __name__ == "__main__":
    main()
