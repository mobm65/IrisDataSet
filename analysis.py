import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
import scipy as sp
from sklearn import datasets

df = pd.read_csv("iris.data")

plt.scatter(df['spl'], df['class'])
plt.show()


