# Date: 10th of Oct 2025
# Abobaker Ahmed Khidir Hassan
# Course: Seaborn Library
# Padform: satr.codes
# Introduction


# Importing 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import kagglehub
path = kagglehub.dataset_download("gauravsharma99/car-mpg")

# open the file
df = pd.read_csv("mpg_raw.csv")

# take a look at the data
print("\n", "_" * 60, "\n")
print("Info:\n", df.info())
print("\n", "_" * 60, "\n")
print("Shape: ", df.shape)
print("\n", "_" * 60, "\n")
print("Describtion:\n",df.describe(include = "all")) # to show numerical and non-numerical fields
print("\n", "_" * 60, "\n")
print("Null Values:\n", df.isnull().sum())
print("\n", "_" * 60, "\n")
print("Head:\n", df.head())

