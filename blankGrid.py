# Function to generate a list of lists representing an empty 9 x 9 soduko board (filled with zeros)

def blankGrid():
    blnkGrid = []

    for i in range(9):
        blankRow = []
        for j in range(9):
            blankRow.append(0)
        blnkGrid.append(blankRow)

    return blnkGrid