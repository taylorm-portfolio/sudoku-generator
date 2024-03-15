import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pandas
from connectDB import retrieveData

# Example query: SELECT max(runID) FROM runs
mylist = retrieveData('''SELECT runTimeSolution FROM runs ''',1)
df = pandas.DataFrame(mylist)
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(df)  # Plot some data on the axes.
plt.show()
print(df)

#plt.show()