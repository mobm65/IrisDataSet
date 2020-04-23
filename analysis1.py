
# write data in a text file
#File_object = open(r"iris.data",)
#setosa = open(iris.data, "setosa")
#versicolor = open(iris.data, "versicolor")
#virginica = open(iris.data, "virginica"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from sklearn import preprocessing
from Cython.Shadow import inline



iris = pd.read_csv("iris.data")
iris.info()

iris['Species'] = iris['Species'].astype('category')
iris['target'] = pd.Categorical.from_array(iris)['Species'].codes
iris['target'].value_counts()

ax = iris[iris.Species=='Iris-setosa'].plot.scatter(x='SepalLengthCm', 
y='SepalWidthCm', color='red', label='setosa')
iris[iris.Species=='Iris-versicolor'].plot.scatter(x='SepalLengthCm',
y='SepalWidthCm', color='green', label='versicolor', ax=ax)
iris[iris.Species=='Iris-virginica'].plot.scatter(x='SepalLengthCm', 
y='SepalWidthCm', color='blue', label='virginica', ax=ax)
ax.set_title("Variance in petal & sepal length & width in Iris Species")




