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

https://medium.com/gft-engineering/start-to-learn-machine-learning-with-the-iris-flower-classification-challenge-4859a920e5e3



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

Machine based learning is pervasive in our everyday lives.  The algorithms produced based on inputs and outputs manipulated by algorithms influence our everyday lives.  Anyone logging onto the internet can see that the advertisements are targetted based on your previous inputs and outputs.  If you read about learning music or taking a music class, you will suddenly notice ads for goods and services related to your searches.  Michel Kosinski delveloped a psychographic model which was very successful in classifying people as to ethnic background, politics, sexuality etc. Based on their responses to a My personality app on Facebook he could estimate classifications.  Now with so many more data points available to data brokers, our information is used to target people directly with adverts or information designed to influence our feelings and behaviours.  This is the evolution of machine learning in sociology; if you can classify people you can target them.

Gael Varoquaux has done much work in the field of machine learning and has many online publications of his work on the Iris Dataset.  He did a 2 dimensional scatter plot to illustrate the features of the dataset, he supplied the code for his plot.  He also did a more complicated 3 dimensional plot importing; numpy, matplotlib.pyplot, matplotlib toolkits and sklearn to plot the 3 species based on sepal length and width, and petal length and width.  He did further analysis of the set mapping differences between versicolor and virginica, the two species with closest petal and sepal attributes.  He supplied code for all of his plots.

Kaggle published a Python notebook doing exploratory data analysis from the iris dataset. Kaggle, a Google subsidiary, is an online community of data scientists and machine learning practictioners.  I learned that each row represents one flower which is called an observation or sample/example/instance.  Each column, the sepal length and width; the petal length and width, is a feature or predictor/attribute/independent variable/input regressor/covariate.  The table is a 2 dimensional grid of data: the rows are individual elements of the dataset and the columns represent quantities related to each of these elements.  The iris dataset is four dimensional there are four features for each sample.  This site gave many examples of code and plots some of which were a bit beyond me but the simpler scatter plots explored the relationship between sepal length and width; and petal length and width within species.  This model predicts the statistical likelihood of an iris flower belonging to a particular species based on its attributes.  

Hari Mittapalli was very useful to me to help with my own coding, I found his approach very simple and helpful.  He is a data engineer and explored the data in a simple way, which suits me well.  I found the motto of the Medium site very encouraging "Getting smarter about what matters to you."   The results of his coding included a table outlining the mean, standard deviation, 25th percentile, median, 75th percentile, minimum and maximum values which I think could be very useful in writing a summary of each variable to be output to a text file. 



MY PLAN

I found it too difficult to contemplate all this problem as one task in one file so I divided it up.  After messing around and trying a few options I created 4 files in Visual Studio Code.  I used the above sources liberally to help me to formulate my code and plan this assignment.  Revision from my lecture notes formed the basis of my understanding of the relevance of this study and how classification helps assign a sample to a group and predict where samples belong.  Machine learning tells us about extracting information from data we have collected.  In this case we are exploring predictive analytics.  Machine based learning produces algorithms which can predict classification based on a series of inputs and outputs.  I want to find out how close the three classes in the iris species are related to each other.  I will do this by statistical analysis.  Secondly I will produce histograms which further illustrate the four variables; petal length, petal width, sepal length and sepal width within the three classes of the iris species.  The final scatter grams can be best used to predict to which class future samples of irish can be assigned.

Analysis2.py currently has a file plotting each of the four features against each other which I don't think is quite what the task requires so I'm working on that.  My biggest task is to join thise files together and have them output the way the assignment outlines.

Analysis.py currently has 4 histograms showing the frequency of petal lengths in the iris flowers, the frequency of petal widths in the iris flowers, the frequency of sepal lengths in the iris flowers, the frequency of sepal widths in the iris flowers.  I have to figure out how to save the histograms to a png file. I also have to find a way to display each plot without having to exit out of the current one.

Analysis1.py currently has 2 scatter plots showing the difference in petal lengths and widths; and sepal lengths and widths between the 3 species.  I need to display each plot without having to exit out of the current one.

Analysis2.py currently has a file plotting each of the four features against each other which I don't think is quite what the task requires so I'm working on that.  My biggest task is to join thise files together and have them output the way the assignment outlines.

iris.data contains the dataset.

UPDATE - 29/4
I have run into difficulties regarding permissions when trying to output data.  I think this issue is to do with errors I made when installing the software in the early days of this course.  I cannot deal with this issue now so I am submitting my findings as follows.

I have combined the elements of the program into one file called iriscombined.py.  The first part of this file produces the statistical summary of the data. I have saved this summary to a file called analysis.txt which is in this folder.  The code needed to export this as a text file is commented in iriscombined.py.  Looking at analysis.txt we can see that as classes within the species iris, there are some striking variations. The first row is simply a count of the number of samples in the dataset.  The next two rows are the most important in this summary.  The mean represents the sum of the elements (eg petal length) divided by the elements multiplied by the frequence with which they appear.  sum of x/sum of fx.  The standard deviation expresses how each sample differs from the mean for the group.  To be predictive the standard deviation should be less than 1/3 of the mean.  We can see when it comes to the petal length and petal width are within this ratio and could be useful to classify these flowers as part of a species.  The sepal length and widths would not allow for this classification to occur as they are well outside the ratio.  The minimum and maximum values show us where the outliers are, the samples which are at the edge of the class.  The median (50%) and interquartile range show us where the greatest number of the samples are plotted.  The analysis of these four variables does not produce a model which can allow us to classify iris samples.

The second element of the file iriscombined.py is four histograms plotting the information gained in the previous section.  Again I could not get permission to output these to a .png file but I have shown the code I would have used to do this.  I also include the .png files which I saved to my documents and dragged into the IRISDATASET folder.  
The first histogram shows that a petal length of 1 cm occurs most frequently in the dataset and a petal length of 3cm occurs least frequently.  The majority of the samples fall within 4 - 6 cms in petal lenght.
Hist2.png shows that the petal width of 1mm to 3mm occurs most frequently in this sample, while a width of 6mm to 8mm occurs least frequently.  Data in this set is spread out and tells us that the three species must be very different as regards this variable.
Hist3.py seems almost like a bell curve skewing to the left.  A normal distribution like this is used to predict if a sample belongs within a certain class.  This histogram showing approximately 71% of samples having sepal lengths between 4.6cm and 6.8cms would be useful in classification.  
Hist4 again resembles a bell curve.  In this plot we can see that 76% of the samples fall within 2.5cms and 3.5cms.  Sepal widths are therfore most alike in these three classes of iris.  The sepal width is the most suitable to predict classification.

The last section of iriscombined.py produces two scatter plots.  The first plot plots each of the three species based on their sepal length and breadth.  This plot shows us that the setosa is quite distinct as regards these two variables, the versicolor and virginica show some areas of crossover.
The second plot shows that the setosa is separate from the others as regards petal lenght and width. The versicolor and virginica are closer together but the crossover points are far fewer.
Plotting the data in this way allows us to better classify and predict.  Examining each variety of iris and correlating it with the four variables allows us to identify to which class an unidentified flower would belong.  Even the two species which are most alike, versicolor and virginica, show enough differences on the petal length and width scatter plot for effective prediction.
