# Function to generate a list of 3 digit indexes representing each of the 81 cells in the soduko grid

def indexRef():

    indexOutput = []
    # create 81 values referencing 1 of 9 subsquares that each of the 81 cells in the soduko board occupy:
    subSquareList = (3*(3*"0,"+3*"1,"+3*"2,")+3*(3*"3,"+3*"4,"+3*"5,")+3*(3*"6,"+3*"7,"+3*"8,")).split(",")
    # Remove empty last value:
    subSquareList.remove("")

    counter = 0
    # Loop through all 81 cells in the soduko board applying the row nunber, column number, and subsquare number to a string that is appended to the indexes list.
    for i in range (9): # row numbers
        for j in range (9): # column numbers
            squareIndex = subSquareList[counter]
            indexOutput.append(str(i)+str(j)+squareIndex)
            counter = counter + 1 # update counter to get next value from subSquareList

    return indexOutput # return list of 3-character strings representing row, column, and subsquare index

# Function to generate a list of lists representing an empty 9 x 9 soduko board (filled with zeros)

def blankGrid():
    blnkGrid = []

    for i in range(9):
        blankRow = []
        for j in range(9):
            blankRow.append(0)
        blnkGrid.append(blankRow)

    return blnkGrid

# Function to generate a dictionary (diary) with a list of available values for each column, row, and subsquare

def gridDiary():
    names = ["row","column","square"] # dictionary names that form basis of key names
    listsDiary = {} 
    for i in range(3): # iterates through each of the three main categories in this dictionary: rows, columns, and squares
        keyName = names[i] # gets basis of key name
        for j in range(9):
            listsDiary[keyName+str(j)] = [1,2,3,4,5,6,7,8,9] # applies row, column, or square number to key name basis, and assigns the full range of possible values. Example: row1: [1,2,3,4,5,6,7,8,9]

    return listsDiary #returns dictionary of available values for each row, column, and square
