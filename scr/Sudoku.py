from numpy import *
import random

"Przesuniecie w Lewo"


def ShiftLeftMatrix(matrixIN):
    matrixOUT = matrixIN
    for i in range(0, 3):
        for j in range(0, 2):
            help = matrixOUT[i][j]
            matrixOUT[i][j] = matrixOUT[i][j + 1]
            matrixOUT[i][j + 1] = help

    return matrixOUT


def ShiftUpMatrix(matrixIN):
    matrixOUT = matrixIN
    for j in range(0, 3):
        for i in range(0, 2):
            help = matrixOUT[i][j]
            matrixOUT[i][j] = matrixOUT[i + 1][j]
            matrixOUT[i + 1][j] = help

    return matrixOUT


tabIntegers = []
for i in range(1, 10):
    tabIntegers.append(i)

"Tworzenie macierzy"
matrix = zeros((3, 3), int)

for i in range(0, 3):
    for j in range(0, 3):
        generator = random.choice(tabIntegers)
        tabIntegers.remove(generator)
        matrix[i][j] = generator

"Tworzenie Sudoku"
sudoku = zeros((9, 9), int)
for k in range(0, 3):
    matrix = ShiftUpMatrix(matrix)
    for i in range(0, 3):
        for j in range(0, 3):
            sudoku[i][j + 3 * k] = matrix[i][j]
    matrix1 = ShiftLeftMatrix(matrix)
    for i in range(0, 3):
        for j in range(0, 3):
            sudoku[i + 3][j + 3 * k] = matrix1[i][j]
    matrix2 = ShiftLeftMatrix(matrix1)
    for i in range(0, 3):
        for j in range(0, 3):
            sudoku[i + 6][j + 3 * k] = matrix2[i][j]
matrix = ShiftUpMatrix(matrix)
print(sudoku)