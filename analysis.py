# save a histogram of each variable to a png file
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
import scipy as sp
from seaborn import colors
from matplotlib.patches import Patch

iris = pd.read_csv("iris.data")
# iris.info()
# iris['Species'] = iris['Species'].astype('category')

plt.hist(iris['ptl'], facecolor='purple', edgecolor='black')
plt.xlabel('Petal length in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Petal length in three species of Iris')
plt.show()


plt.hist(iris['ptw'], facecolor='green', edgecolor='black')
plt.xlabel('Petal width in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Petal width in three species of Iris')
plt.show()

plt.hist(iris['spl'], facecolor='orange', edgecolor='black')
plt.xlabel('Sepal length in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Sepal length in three species of Iris')
plt.show()

plt.hist(iris['spw'], facecolor='yellow', edgecolor='black')
plt.xlabel('Sepal width in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Sepal width in three species of Iris')
plt.show()

#plt.plot()
#ax = iris[iris.Species=='Iris-setosa'].plot.trend(x='spl', 
#y='spw', color='red', label='setosa')


#plt.show()