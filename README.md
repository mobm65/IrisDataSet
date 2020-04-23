# IrisDataSet
Sources:
Ian McLoughlin, GMIT, PandS, Lecture 1

R.A. Fisher (1936). "The use of multiple measurements in taxonomic* problems". Annals of Eugenics. 7(2):179-188

Real Python. Tutorials on OOP, Matplotlib, Pandas, Numpy and csv files.

Wikipedia - sourced scientific articles on iris data set and machine learning.

Iris dataarchive.ics.uci.edu › machine-learning-databases › iris 

http://gael-varoquaux.info

https://www.kaggle.com/xuhewen/iris-dataset-visualization-and-machine-learning


* taxonomy - classification of something, especially organisms.

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
