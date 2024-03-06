from sudoku import sudokuGen
from connectDB import retrieveData
import sqlite3
from solver import backtrackSolver
import pandas as pd
lim = 55

#for i in range(10,lim,5):
 #   print(f"running funciton for i = {i}")
  #  for k in range(1,50):
   #     sudokuGen(i)
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
