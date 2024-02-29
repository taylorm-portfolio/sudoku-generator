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