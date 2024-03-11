from sudoku import sudokuGen
from connectDB import retrieveData
import sqlite3
from solver import backtrackSolver
import pandas as pd
lim = 50

#for i in range(10,lim):
#    print(f"running funciton for i = {i}")
#    for k in range(1,150):
#        sudokuGen(i)
#sudokuGen(64)

#mylist = retrieveData('''SELECT removedCells,count(removedCells) FROM runs GROUP BY removedCells''',2)
#print(mylist)
        
board = [
[0,4,6,0,0,0,0,0,5],
[0,8,0,0,4,0,7,3,9],
[0,7,5,0,1,0,0,8,6],
[1,0,4,0,0,0,0,0,0],
[0,9,8,3,5,0,0,0,4],
[0,0,0,2,0,0,0,0,0],
[0,0,0,8,0,9,5,0,0],
[4,0,3,0,6,0,8,0,0],
[0,0,9,4,0,0,0,6,0],

]

#backtrackSolver(board)
#df = pd.DataFrame(board)
#print(df)
#df.to_csv('puzzlesolved.csv', index=False)

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import sqlite3

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df1 = pd.read_sql_query('SELECT removedCells, count(runID), round(avg(runCountSolution),2), round(avg(runCountPuzzle),2), runDate FROM runs WHERE runDate = \'2024-03-11\' GROUP BY removedCells',con)
#df2 = pd.read_sql_query('SELECT removedCells, count(runId)')
df2 = pd.read_sql_query('SELECT runID, runDate, runCountSolution, runTimeSolution, runCountPuzzle, runTimePuzzle, runTimeOverall, removedCells FROM runs WHERE runDate = \'2024-03-11\'',con)
renameDiary = {
    'runID': 'Run ID',
    'runDate': 'Date Generator Run',
    'runCountSolution': 'Runs to Generate Solution',
    'runTimeSolution': 'Time (ms) to Generate Solution',
    'runCountPuzzle': 'Runs to Generate Puzzle',
    'runTimePuzzle': 'Time (ms) to Generate Puzzle',
    'runTimeOverall': 'Time (ms) to Run Entire Generator',
    'removedCells': 'Qty Removed Cells',
    'count(runID)': '# of Runs',
    'round(avg(runCountSolution),2)': 'Avg # of Runs to Generate Solution',
    'round(avg(runCountPuzzle),2)': 'Avg # of Runs to Generate Puzzle',
    
}

dfPivot = pd.pivot_table(df2, index='removedCells', values=['runCountSolution','runCountPuzzle'], aggfunc={'runCountSolution':'mean','runCountPuzzle': 'mean'}).reset_index(drop = False)
print(dfPivot)