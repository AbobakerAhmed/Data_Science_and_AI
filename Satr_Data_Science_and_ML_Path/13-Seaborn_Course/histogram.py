# Date: 11th of Oct 2025
# Abobaker Ahmed Khidir Hassan
# Course: Seaborn Library
# Padform: satr.codes
# Histogram Plot 

# Importing
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the data
data = pd.read_csv("mpg_raw.csv")

# Display the histogram of MPG column
plt.figure(figsize = (10,5))
sns.histplot(data, x= "mpg" , bins = 15, hue = "origin", multiple = "stack")
plt.title("MPG Distribution")
plt.show()


# Insigits:
# 1- The count of the economic cars in the dataset is low
# 2- After applying the hue depending on the origin, we see that:
    # a) usa cars is not economic (13, 14)
    # b) the best economic cars are in japan and europe













