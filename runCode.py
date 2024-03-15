# This file is for running tests and iterations of my sudokuGen function (or other snippets of code)

from sudoku import sudokuGen
from connectDB import retrieveData
import sqlite3
from solver import backtrackSolver
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

lim = 50

#for i in range(10,lim):
#    print(f"running funciton for i = {i}")
#    for k in range(1,150):
#        sudokuGen(i)
sudokuGen(10)

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

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df = pd.read_sql_query('SELECT runID, runDate, runCountSolution, runTimeSolution, runCountPuzzle, runTimePuzzle, runTimeOverall, removedCells FROM runs WHERE runDate = \'2024-03-11\'',con)
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
#df.close.rolling(5).mean()
dfPivotMA = pd.pivot_table(
    df, index=['removedCells','runID'],
    values=[
        'runCountSolution',
        'runCountPuzzle',
        'runTimePuzzle',
        'runTimeSolution',
        'runTimeOverall'
        ],
    aggfunc={
        'runCountSolution':'mean',
        'runCountPuzzle': 'mean',
        'runTimePuzzle': 'mean',
        'runTimeSolution': 'mean',
        'runTimeOverall': 'mean'
        }
    ).reset_index(drop = False).round({
        'runCountSolution': 2,
        'runCountPuzzle': 2,
        'runTimePuzzle': 6,
        'runTimeSolution': 6,
        'runTimeOverall': 6
    })
print(dfPivotMA)
dfPivotMA['SlnMA5'] = dfPivotMA.runCountSolution.rolling(5).mean()
dfPivotMA['SlnMA15'] = dfPivotMA.runCountSolution.rolling(20).mean()

print(dfPivotMA)