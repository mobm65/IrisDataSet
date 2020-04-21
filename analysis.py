import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
import scipy as sp

df = pd.read_csv("iris.data")

a = plt.scatter(df["spl"], df["spw"])
fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2, figsize=(0.1,8))
ax1.set_title("Scatter: Variations in Iris Species")
#ax1.scatter(x=a, y=a, marker="o", c = "r", edgecolor="b")
ax1.set_xlabel("Sepal length")
ax1.set_ylabel("Sepal width")


b = plt.scatter(df["ptl"], df["ptw"])
fig, (ax1, ax2)= plt.subplots(nrows=1, ncols=2, figsize=(0.1,8))
#ax1.scatter(x=b, y=b, marker="o", c = "r", edgecolor="b")
ax1.set_title("Scatter: Variations in Iris Species")
ax1.set_xlabel("Petal length")
ax1.set_ylabel("Petal width")

plt.show()






