import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
import scipy as sp

iris = pd.read_csv("iris.data")
iris.info()

iris['Species'] = iris['Species'].astype('category')