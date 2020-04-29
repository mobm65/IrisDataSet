import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# A summary of each variable to a text file

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

#################################################################

# a histogram to display the frequency of petal lengths in
# the iris dataset.
plt.hist(iris['ptl'], facecolor='purple', edgecolor='black')
plt.xlabel('Petal length in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Petal length in three species of Iris')
plt.show()

# Following is the command I would have used to save each of
# these histograms to the .png file as requested.  My system will
# not allow me permission and I cannot rectify it.

#plt.savefig("Hist1.png")

# a histogram to display the frequency of petal widths in
# the iris dataset.
plt.hist(iris['ptw'], facecolor='green', edgecolor='black')
plt.xlabel('Petal width in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Petal width in three species of Iris')
plt.show()
#plt.savefig("Hist2.png")


#a histogram to display the frequency of sepal lengths in
# the iris dataset.
plt.hist(iris['spl'], facecolor='orange', edgecolor='black')
plt.xlabel('Sepal length in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Sepal length in three species of Iris')
plt.show()
#plt.savefig("Hist3.png")
# a histogram to display the frequency of sepal widths in
# the iris dataset.
plt.hist(iris['spw'], facecolor='yellow', edgecolor='black')
plt.xlabel('Sepal width in cms')
plt.ylabel('Frequency')
plt.title('Frequency of Sepal width in three species of Iris')
plt.show()
#plt.savefig("Hist4.png")
############################################################################


# A scatter plot comparing the variables

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
