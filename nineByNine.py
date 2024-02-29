import pandas as pd
import random

# Print a 9x9 list of unique single-digit integers as a learning experience
optionsList = [1,2,3,4,5,6,7,8,9]
table = [[0,0,0],[0,0,0],[0,0,0]]
j=2
i = 2
while i >= 0:
    templist = table[i]
    j=2
    while j >= 0:
        randInt = random.sample(range(len(optionsList)),1)[0]
        templist[j] = optionsList.pop(randInt)
        j=j-1
    table[i] = templist
    i=i-1

df = pd.DataFrame(table)
print(df)
