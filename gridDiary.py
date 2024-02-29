# Function to generate a dictionary (diary) with a list of available values for each column, row, and subsquare

def gridDiary():
    names = ["row","column","square"] # dictionary names that form basis of key names
    listsDiary = {} 
    for i in range(3): # iterates through each of the three main categories in this dictionary: rows, columns, and squares
        keyName = names[i] # gets basis of key name
        for j in range(9):
            listsDiary[keyName+str(j)] = [1,2,3,4,5,6,7,8,9] # applies row, column, or square number to key name basis, and assigns the full range of possible values. Example: row1: [1,2,3,4,5,6,7,8,9]

    return listsDiary #returns dictionary of available values for each row, column, and square