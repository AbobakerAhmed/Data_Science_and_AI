# Date: 29th of Sep 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# Importing
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
data = pd.read_csv("tmdb_movies_data.csv")


# Display the top 5 revenue movies

# 1- Group the movies depending on title, then sort them by the revenue in deascending order
top_revenue = data.groupby('original_title').sum().sort_values(by='revenue', ascending = False)

# Take a look at the new dataset
# print(top_revenue.info())
# print("\n\n", "_" * 60, "\n\n")
# print(top_revenue.head())

# now, we need only movies titles and revenues, 
    # we sort the data in descending order, so the top row will contain the heigher revenue movies
    # we group the movies by the title, so it is the index right now
n = 5
movies = top_revenue.head(n).index # top n revenue movies
#print(movies)
revenue = top_revenue.head(n).revenue.values
#print(revenue)


# Drow the graph
plt.figure(figsize = (12,10)) # figure size
# colors= ['red','blue'] # make colors of the bars
plt.bar(
    movies, # X-axis
    revenue, # y-axis
    # color=colors # repete the trend in the colors list
)
plt.title(
    f'Top {n} Revenue Movies',
    fontsize = 18
)
plt.xlabel(
    'Movie',
    fontsize = 16
)
plt.ylabel('Revenue',
    fontsize = 16
)

# plt.grid() # display the networks lines +

# dispaly the graph
plt.show()



