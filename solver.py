import random

# this file contains a function to solve the sudoku challenge
# the functions are based on the article by Seng Kuang Yap at the below link
# https://www.linkedin.com/pulse/creating-sudoku-solver-using-python-backtracking-algorithm-yap-tauof/
# from sudoku import puzzleGenerator
def isValid(board,row,col,num):
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col +j] == num:
                return False
    return True

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None

# Example usage
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Example with two solutions:

board = [
[3,4,8,1,2,5,6,7,9],
[6,9,2,7,8,4,1,5,3],
[5,1,7,9,6,3,2,8,4],
[4,6,1,3,5,9,7,2,8],
[2,7,9,8,1,6,3,4,5],
[8,5,3,4,7,2,9,0,0],
[9,2,5,6,4,1,8,3,7],
[1,8,6,5,3,7,4,9,2],
[7,3,4,2,9,8,5,0,0]
]

def backtrackSolver(board):
    #board = [[7, 8, 5, 0, 3, 4, 1, 9, 2], [2, 6, 0, 5, 1, 7, 3, 4, 8], [4, 1, 3, 8, 2, 9, 5, 6, 7], [9, 4, 6, 2, 5, 1, 8, 7, 0], [3, 2, 8, 9, 7, 6, 4, 5, 1], [5, 7, 1, 3, 4, 8, 0, 2, 9], [6, 9, 4, 1, 8, 2, 7, 3, 5], [1, 5, 2, 7, 6, 3, 9, 8, 4], [8, 3, 7, 4, 9, 5, 2, 1, 6]]
    empty = findEmpty(board)
    if empty is None:
        return True
    for i in range(10):
        if isValid(board,empty[0],empty[1],i) == True:
            board[empty[0]][empty[1]] = i
            if backtrackSolver(board):
                return True
            board[empty[0]][empty[1]] = 0
    return False

# FROM AI:

def is_unique(board):
    find = find_empty(board)
    if not find:
        return 1
    else:
        row, col = find

    count = 0
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            count += is_unique(board)
            board[row][col] = ""

    return count

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "":
                return (i, j)  # row, col

    return None