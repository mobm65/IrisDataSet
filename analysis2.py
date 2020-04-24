# a summary of each variable to a text file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from seaborn import colors

iris = pd.read_csv("iris.data")
data = pd.DataFrame(iris, columns=['spl','spw','ptl', 'ptw', 'Species'])



#print(data.head())

#print(data.describe())

#data.info()

sns.pairplot(data)
plt.show()