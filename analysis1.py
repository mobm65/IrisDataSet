# A scatter plots of each set of variables

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

# read in iris data set to use for statistical analysis
iris = pd.read_csv("iris.data")
iris.info()

# changing iris to int
iris['Species'] = iris['Species'].astype('category')

# plot first variable, sepal length & breath vs species type
ax = iris[iris.Species=='Iris-setosa'].plot.scatter(x='spl', 
y='spw', color='red', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot.scatter(x='spl',
y='spw', color='green', label='versicolor', ax=ax)
iris[iris.Species=='Iris-virginica'].plot.scatter(x='spl', 
y='spw', color='blue', label='virginica', ax=ax)
ax.set_title("Variance in Sepal length & width in Iris Species")

# plot second variable, petal length and breath vs species type
ax = iris[iris.Species=='Iris-setosa'].plot.scatter(x='ptl', 
y='ptw', color='red', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot.scatter(x='ptl',
y='ptw', color='green', label='versicolor', ax=ax)
iris[iris.Species=='Iris-virginica'].plot.scatter(x='ptl', 
y='ptw', color='blue', label='virginica', ax=ax)
ax.set_title("Variance in Petal length & width in Iris Species")

# show the two scatter plots.
plt.show()




