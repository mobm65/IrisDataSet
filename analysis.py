import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
import scipy as sp
from sklearn import datasets

#df = pd.read_csv("iris.csv")

iris = datasets.load_iris() 

X = iris.data[:, :2]
y = iris.target 
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8,6))
plt.clf() 
plt.show()
