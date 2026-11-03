# Date: 28th of Sep 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# Importing
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
data = pd.read_csv("tmdb_movies_data.csv")

# take a look at the data
#print(data.info())
#print("\n\n","_" * 80, "\n\n")
#print(data.head())

# Displaying vote_avrage column
bins_number = [0,1,2,3,4,5,6,7,8,9,10]
plt.hist(
        data['vote_average'], # Data
        bins_number, # Bins count
        facecolor = 'blue', # Bins color
        edgecolor = 'black' # Seprator color
    ) 
plt.title('Distribution of Vote Average') # graph title
plt.ylabel("Frequency")    # vertical label
plt.xlabel(f"Vote Average ({data['vote_average'].min()} to {data['vote_average'].max()})") # horizantal label
plt.show() # to show the graph





