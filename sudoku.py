
import pandas as pd
import random
from datetime import date
import time
import copy
#import pymysql
from blankGrid import blankGrid
from gridDiary import gridDiary
from indexRef import indexRef
from connectDB import createTable
from connectDB import addRowDB
from connectDB import getLastID
from solver import is_unique
from exportExcel import saveExcel
import os
import sys
def sudokuGen(removeN):
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    # Get date and time Info

    runStartOverall = time.time()
    runDate = date.today()

    # CALL FUNCTIONS

    indexList =indexRef() # Calls function to generate a list of 3 digit indexes representing each of the 81 cells in the sudoku grid
    #options = gridDiary() # Calls function to generate a dictionary with a list of available values for each column, row, and subsquare
    #solutionGrid = blankGrid() # Calls function to generate a list of lists representing an empty 9 x 9 sudoku board (filled with zeros)

    # FILL THE PUZZLE
    runStartSln= time.time()
    gridSum = 0 # used to check that sudoku board has no zeros in it
    triesSln = 0 # used to count number of while loop runs for data analysis purposes
    while gridSum < 405: # When gridSum = 0, the board is filled with digits from 1 to 9, and the program has successfully created a solved board.
        triesSln = triesSln +1 # count runs
        gridSum = 0 # resets gridSum to zero after previous runs
        solutionGrid = blankGrid() # resets the solution grid to empty grid full of zeros 
        options = gridDiary() # resets options dictionary to have all digits (1 - 9) available for each row, column, and subsquare

        for indexx in indexList: # iterates through each of the 81 cells in the grid
            # set variables for ease of reference:

            # variables for cell reference:
            puzzleColIndex = int(indexx[0]) 
            puzzleRowIndex = int(indexx[1])

            # variables for options dictionary reference. With each iteration of current for loop, the option lists for the current row, column, and square are pulled, so that the code can check which values are common between all three lists.
            columnOpt = options["column"+indexx[0]]
            rowOpt = options["row"+indexx[1]]
            squareOpt = options["square"+indexx[2]]

            # Pull randum number from the current column options and compare it with options in the row and square options to find a match. If there's no match, the program will skip this cell, leaving a zero, and the outer while loop will execute again.
            counter = 18 # Set this to limit while loop below. This ensures that all options are tried from the options list.
            
            while counter >0:
                randInt = random.sample(columnOpt,1)[0] # get random value from the available options for current column
                # Check if the random value from the current column options is available in the options for the current row and subsquare
                # Remember, if a value is in the options list for any row, column, or subsquare, that means it is NOT in the current row, column, or subsquare in the actual puzzle grid.
                # this means that if the options list for the current row and subsquare contain randInt, then that is a valid option to place in the square. 

                if randInt in rowOpt and randInt in squareOpt: 
                    # If true, then randInt is valid for the current cell...
                    # so remove randInt from the current option lists
                    columnOpt.remove(randInt) 
                    rowOpt.remove(randInt)
                    squareOpt.remove(randInt)
                    
                    # Place randInt into the puzzle grid:
                    puzzleRow = solutionGrid[puzzleRowIndex]
                    puzzleRow[puzzleColIndex] = randInt
                    solutionGrid[puzzleRowIndex] = puzzleRow
                    gridSum = gridSum + randInt # log that this cell is filled by adding randInt to the gridSum
                    break # no need to continue trying values as the cell is filled.
                counter = counter - 1

    # Capture runtime of solution generator
    runTimeSln = time.time() - runStartSln

    # Now we have a full sudoku grid that satisfies the rules. print this to the terminal and save it as a CSV
    df = pd.DataFrame(solutionGrid)
    print("Solution Grid: ")
    print(df)
    df.to_csv('solution.csv', index=False)
    saveExcel(df,"Sudoku Solution","Solution")

    # Print stats for the while loop that generates the solution grid:
    print("Number of tries to fill solution grid: ",triesSln)

    # This portion of the code runs a function to check if the puzzle has 1 unique solution, and retries generating the puzzle until it finds 1 
    runStartPuzzle = time.time()

    isUnique = 2
    loopcount = 0
    while isUnique > 1:
        puzzleGrid = copy.deepcopy(solutionGrid)
        removeList = random.sample(indexList,removeN)

        for indexx in removeList:
            puzzleColIndex = int(indexx[0])
            puzzleRowIndex = int(indexx[1])
            puzzleGrid[puzzleRowIndex][puzzleColIndex] = ""

        isUnique = is_unique(puzzleGrid)
        loopcount = loopcount +1

    runTimePuzzle = time.time() - runStartPuzzle

    print(f"Puzzle found after {loopcount} runs:")
    df = pd.DataFrame(puzzleGrid)
    print(df)
    df.to_csv('puzzle.csv', index=False)
    saveExcel(df,"Sudoku Puzzle","Puzzle")

    # Now, to introduce a little SQL:

    # I'm pretty certain the above code isn't as efficient as it could be. Instead of improving it (for now),
    # I will send the stats from each run to a SQL database for later analysis.

    # Call a funciton to create a database named :sudokustats.db" and table named "runs" if they do not already exist.
    createTable()

    # Get ID in key column of last run of the code, and increment this to create a new unique ID.
    lastKey = getLastID()
    keyVal = 1 + lastKey

    # Calculate overall code run time.
    runTimeOverall = time.time() - runStartOverall

    # Call funciton to add run stats to the database.
    addRowDB([keyVal,runDate,triesSln,round(runTimeSln,3),loopcount,round(runTimePuzzle,3),round(runTimeOverall,3),removeN])

    sys.stdout = original_stdout
    return df