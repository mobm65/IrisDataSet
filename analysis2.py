# a summary of each variable to a text file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import the iris dataset
iris = pd.read_csv("iris.data")
# separate the iris variables for analysis
data = pd.DataFrame(iris, columns=['spl','spw','ptl', 'ptw', 'Species'])
# extract the statistical summary of each variable and print to screen
print(data.describe())

# the code below analyses the data and gives a summary of the
# statistical analysis to a text file
# I have commented the code because it would not give me 
# permission to write to a text file.


#text_file = open("analysis.txt", "w")
#n = text_file.write(data.describe())
#text_file.close()


