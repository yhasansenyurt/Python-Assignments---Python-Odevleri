#########################################################################################
# QUESTION IV
# Description: This program operates matrices in different ways and analyzes maximum
# value of matrix.
#########################################################################################
print("SOLUTION OF QUESTION IV:")
print("\n")

import random
import sys
def readMatrix(numberOfRows , numberOfColumns, file):
    matrix = [] # Create an empty list
    for row in range(numberOfRows):
        matrix.append([]) # Add an empty new row
        line = file.readline()
        rowdata = [int(x) for x in line.split(' ')]
        for column in range(numberOfColumns):
            matrix[row].append(rowdata[column])
    return matrix
def printMatrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(format(matrix[row][column],"5d"), end = " ")
        print() # Print a new line
def fillMatrixRandomly(numberOfRows,numberOfColumns ):
    matrix = [] # Create an empty list
    for row in range(numberOfRows):
        matrix.append([]) # Add an empty new row
        for column in range(numberOfColumns):
            matrix[row].append(random.randint(0, 99))
    return matrix
def generateZeroMatrix(numberOfRows,numberOfColumns):
    matrix = [ [ 0 for i in range(numberOfRows) ] for j in range(numberOfColumns) ]
    return matrix
def addMatrix(A,B):
    C = generateZeroMatrix (len(A),len(A[0]))
    for row in range(len(A)):
        for column in range(len(A[row])):
            C[row][column] = A[row][column] + B[row][column]
    return C
def multiplyMatrix(A,B):
    multiply = generateZeroMatrix(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                multiply[i][j] += A[i][k] * B[k][j]
    return multiply

def transpose(A):
    transpose = generateZeroMatrix(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            transpose[j][i] = A[i][j]
    return transpose

def maxOfElements(A):
    max =-sys.maxsize - 1
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > max:
                max = A[i][j]
    return max

def subtractMatrix(A,B):
    subtract = generateZeroMatrix(len(A), len(A[0]))
    for row in range(len(A)):
        for column in range(len(A[row])):
            subtract[row][column] = A[row][column] - B[row][column]
    return subtract
# Redirect standard output device (console) to output.txt file
# print statements will write into output.txt file
sys.stdout = open('output.txt', 'w')
print("\nReading data from inputs.txt file in current directory\n")
f = open("inputs.txt","r")

# Read Matrix A
line = f.readline()
numberOfRows , numberOfColumns = [int (x) for x in line.split(' ')]
A = readMatrix(numberOfRows , numberOfColumns, f)
print(" **** Matrix A **** ")
printMatrix(A)
# Read Matrix B
line = f.readline()
numberOfRows, numberOfColumns = [int(x) for x in line.split(' ')]
B = readMatrix(numberOfRows, numberOfColumns, f)
print(" **** Matrix B **** ")
printMatrix(B)
# Read Matrix C
line = f.readline()
numberOfRows, numberOfColumns = [int(x) for x in line.split(' ')]
C = readMatrix(numberOfRows, numberOfColumns, f)
print(" **** Matrix C **** ")
printMatrix(C)
# Generate 4x4 matrix from random numbers.
D = fillMatrixRandomly(numberOfRows, numberOfColumns)
print(" **** Matrix D **** ")
printMatrix(D)
# Compute S = (A+B) * Transpose(C) + D - A
print("\n *** Computing S = (A+B) * Transpose(C) + D) - A *** \n")
# T1 = A + B
def main():
    T1 = addMatrix(A, B)
    T2 = transpose(C)
    T3 = multiplyMatrix(T1, T2)
    T4 = addMatrix(T3, D)
    S = subtractMatrix(T4, A)
    print(" **** MatriX T1 = (A+B) ****")
    print()
    printMatrix(T1)
    print()
    print(" **** MatriX T2 = Transpose (C) ****")
    print()
    printMatrix(T2)
    print()
    print(" **** MatriX T3 = (A+B) * Transpose (C) ****")
    print()
    printMatrix(T3)
    print()
    print(" **** MatriX T4 = (A+B) * Transpose (C) + D ****")
    print()
    printMatrix(T4)
    print()
    print(" **** MatriX S = ((A+B) * Transpose (C) + D) - A ****")
    print()
    printMatrix(S)
    print()
    print("Maximum Element in S =", maxOfElements(S))
main()




