
import pandas as pd
import random
from datetime import date
import time
from blankGrid import blankGrid
from gridDiary import gridDiary
from indexRef import indexRef
from connectDB import addRowDB
from connectDB import getLastID
from solver import backtrackSolver
from solver import findEmpty
from solver import isValid
from solver import is_unique
from solver import valid
from solver import find_empty

#print(len(gridDiary()))
#
#mylist = list(range(1,10))
#print(mylist)
#print(random.shuffle(list(range(1,10))))

#board = [[7, 8, 5, 0, 3, 4, 1, 9, 2], [2, 6, 0, 5, 1, 7, 3, 4, 8], [4, 1, 3, 8, 2, 9, 5, 6, 7], [9, 4, 6, 2, 5, 1, 8, 7, 0], [3, 2, 8, 9, 7, 6, 4, 5, 1], [5, 7, 1, 3, 4, 8, 0, 2, 9], [6, 9, 4, 1, 8, 2, 7, 3, 5], [1, 5, 2, 7, 6, 3, 9, 8, 4], [8, 3, 7, 4, 9, 5, 2, 1, 6]]


board = [[0, 8, 5, 0, 3, 4, 1, 9, 2], [2, 6, 0, 5, 0, 7,0, 4, 0], [4, 0, 0, 0, 2, 9, 5, 6, 7], [0, 4, 0, 2, 5, 1, 8, 7, 0], [3, 2, 8, 9, 7, 6, 4, 5, 1], [5, 7, 1, 3, 4, 8, 0, 2, 9], [6, 9, 4, 1, 8, 2, 7, 3, 5], [1, 5, 2, 7, 6, 3, 9, 8, 4], [8, 3, 7, 4, 9, 5, 2, 1, 6]]

board = [ # has only 2 soutions 
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

board = [ # has only 1 solution
    [6,9,4,7,0,0,0,0,0],
    [0,3,0,0,6,9,0,0,5],
    [0,0,0,1,3,0,0,0,4],
    [0,1,8,0,0,0,0,4,0],
    [2,0,0,0,0,4,5,0,7],
    [0,4,0,0,0,8,0,0,0],
    [4,0,0,0,0,0,7,5,9],
    [0,2,5,0,0,0,6,0,0],
    [0,0,6,0,0,0,4,0,3]
]

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('sudokustats.db')
c = conn.cursor()

# Add new columns (replace 'column5', 'column6', 'column7' with your column names and 'TYPE' with the data type)
c.execute("ALTER TABLE runs ADD COLUMN removedCells INT")

# Commit the changes and close the connection
conn.commit()
conn.close()