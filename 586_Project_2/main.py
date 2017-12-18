import numpy as np
import pandas as pd

data = pd.read_csv("/Users/thai/Documents/Study/586/Project2/586_Project_2/Tree Species Data.csv", header = 0)
# Response
ash = data['Ash']
oak = data['Whiteoak']
pine = data['Whitepine']
# Predictors
lidar = data.ix[:,14:20]
hyperspectral = data.ix[:,20:-1]
