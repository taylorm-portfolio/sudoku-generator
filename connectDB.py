import sqlite3

# consider this linked article for future development, possible to store a database in github. https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/

# Function to add input values as a new row in "runs" table in "sudokustats.db"
def createTable():
    conn = sqlite3.connect("sudokustats.db") #creates, or accesses if already created, a SQL database in the same folder as these files.
    cursor = conn.cursor()

    createTable = '''
    CREATE TABLE IF NOT EXISTS runs (
    runID INT PRIMARY KEY,
    runCount INT,
    runTime  DECIMAL(10,3),
    runDate TEXT
    )
    '''

    cursor.execute(createTable)
    conn.commit()
    conn.close()

# Function to add input values as a new row in "runs" table in "sudokustats.db"
def addRowDB(values):
    conn = sqlite3.connect("sudokustats.db") #creates, or accesses if already created, a SQL database in the same folder as these files.
    cursor = conn.cursor()
    addRow = '''
    INSERT INTO runs (runID,runDate,runCountSolution,runTimeSolution,runCountPuzzle,runTimePuzzle,runTimeOverall,removedCells) VALUES (?,?,?,?,?,?,?,?)
    '''
    cursor.execute(addRow,values)
    conn.commit()
    conn.close()

# Function to retrieve latest run ID from "runs" table in "sudokustats.db"
def getLastID():
    conn = sqlite3.connect("sudokustats.db") #creates, or accesses if already created, a SQL database in the same folder as these files.
    cursor = conn.cursor()
    getID = '''
    SELECT max(runID) FROM runs
    '''
    cursor.execute(getID)
    keyTuple = cursor.fetchone()
    conn.commit()
    conn.close()
    
    if keyTuple[0] is None:
        return 0
    else:
        return keyTuple[0]
    
def runStats():
    pass