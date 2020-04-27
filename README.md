# IrisDataSet
Sources:
Ian McLoughlin, GMIT, PandS, Lecture 1

R.A. Fisher (1936). "The use of multiple measurements in taxonomic* problems". Annals of Eugenics. 7(2):179-188
* taxonomy - classification of something, especially organisms.

Real Python. Tutorials on OOP, Matplotlib, Pandas, Numpy and csv files.

Wikipedia - sourced scientific articles on iris data set and machine learning.

Iris dataarchive.ics.uci.edu › machine-learning-databases › iris 

http://gael-varoquaux.info

https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning

https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis

https://medium.com/@harimittapalli/exploratory-data-analysis-iris-dataset



RESEARCH

Background

The Iris data set is a multivariate* data set introduced by the statistician and biologist Ronald Fisher. 
His study quantified morphologic* data of Iris flowers of three related species; the Setosa and Versicolour were
gathered in the Gaspe Peninsula near Quebec under the same controls, the third species, the Virginica, comes from an 
unnamed location.  His study first makes statistical analysis between the two from the same site, and compares findings
with the 3rd species.  Based on a combination of features, petal height and width and sepal height and width he developed a 
linear discriminant model to distinguish the species from each other. Although his paper was published in the Annals of 
Eugenics, it assigns no particular value to any species.  

* Multivariate - simultaneous analysis of two or more variables.
* Morphology - shape, form and/or structure.

Significance

This data set became a test case for other statistical classification techniques in machine learning. One of these techniques
is Support Vector Machines (SVM). SVMs are supervised learning models with associated learning algorithms which analyse data
used for classification and regression analysis. Regression analysis is a statistical model which estimates the relationship between a dependent variable and independent variables.  The most common type is linear regression where the researcher finds a line which best connects the data found by plotting the relationships between variables.  This model is used for prediction and its use has a correlation with machine learning.  Fisher's Linear Discriminant Model can only be obtained when the object variables are known, this is supervised learning.

Statistical Analysis

Fisher used a variety of statistical equations to find the means and standard deviations within and between species and produced 
ratios to predict to which distribution each plant object belonged.  His histogram displaying his findings lacks modern bells and whistles but cogently illustrates his findings nonetheless. One of the modern methods used to display the Iris data set is a "metro model." The data points are plotted and they are projected to the nearest node. For each node a pie chart is constructed displaying the colour of the variable(s) it represents, the area of the pie is correlated to the number of points it represents.  If the metro model is correct most pie charts will contain only one colour and therefore represent only one variable.  The nodes are connected like a trunk of a tree with branches.  Matplotlib, Scipy and Seaborn offer a wide range of plots to make our data meaningful and capable of being used to explain findings and predict outcomes.

Gael Varoquaux has done much work in the field of machine learning and has many online publications of his work on the Iris Dataset.  He did a 2 dimensional scatter plot to illustrate the features of the dataset, he supplied the code for his plot.  He also did a more complicated 3 dimensional plot importing; numpy, matplotlib.pyplot, matplotlib toolkits and sklearn to plot the 3 species based on sepal length and width, and petal length and width.  He did further analysis of the set mapping differences between versicolor and virginica, the two species with closest petal and sepal attributes.  He supplied code for all of his plots.

Kaggle published a Python notebook doing exploratory data analysis from the iris dataset. Kaggle, a Google subsidiary, is an online community of data scientists and machine learning practictioners.  I learned that each row represents one flower which is called an observation or sample/example/instance.  Each column, the sepal length and width; the petal length and width, is a feature or predictor/attribute/independent variable/input regressor/covariate.  The table is a 2 dimensional grid of data: the rows are individual elements of the dataset and the columns represent quantities related to each of these elements.  The iris dataset is four dimensional there are four features for each sample.  This site gave many examples of code and plots some of which were a bit beyond me but the simpler scatter plots explored the relationship between sepal length and width; and petal length and width within species.  This model predicts the statistical likelihood of an iris flower belonging to a particular species based on its attributes.  

Hari Mittapalli was very useful to me to help with my own coding, I found his approach very simple and helpful.  He is a data engineer and explored the data in a simple way, which suits me well.  I found the motto of the Medium site very encouraging "Getting smarter about what matters to you."   The results of his coding included a table outlining the mean, standard deviation, 25th percentile, median, 75th percentile, minimum and maximum values which I think could be very useful in writing a summary of each variable to be output to a text file. 

My Plan

I found it too difficult to contemplate all this problem as one task in one file so I divided it up.  After messing around and trying a few options I created 4 files in Visual Studio Code.  

Analysis.py currently has 4 histograms showing the frequency of petal lengths in the iris flowers, the frequency of petal widths in the iris flowers, the frequency of sepal lengths in the iris flowers, the frequency of sepal widths in the iris flowers.  I have to figure out how to save the histograms to a png file. I also have to find a way to display each plot without having to exit out of the current one.

Analysis1.py currently has 2 scatter plots showing the difference in petal lengths and widths; and sepal lengths and widths between the 3 species.  I need to display each plot without having to exit out of the current one.

Analysis2.py currently has a file plotting each of the four features against each other which I don't think is quite what the task requires so I'm working on that.  My biggest task is to join thise files together and have them output the way the assignment outlines.

iris.data contains the dataset.
