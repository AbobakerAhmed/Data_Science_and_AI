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

# Displaying the count of released movies in each year

# 1- store the count of movies released in each year as a DataFrame
movies_counts = pd.DataFrame(data.release_year.value_counts(ascending = True))
# 2- now, the year is index not a column so reset the index
movies_counts = movies_counts.reset_index()
# 3- Ater that, we should rename colums
movies_counts.columns = ['year','count']
# 4- Finaly, sort years in ascending order
movies_counts = movies_counts.sort_values(by = ['year'])

# create the graph
plt.plot(
    movies_counts['year'], # X-Axis
    movies_counts['count'], # Y-Axis
    c = '0.4', # line color
    linestyle = ':', # how the line will be look like
    linewidth = 2, # the width of the line
    marker = "o", # u can search matplotlib marker
    markersize = 0.5, 
    markerfacecolor = 'grey',
    markeredgecolor = 'b', # see matplotlib color
    markeredgewidth = 5
)
plt.title('Distribution of Releasing Movies') # graph title
plt.ylabel("Movies Count")    # vertical label
plt.xlabel("Release Year") # horizantal label
plt.xlim(movies_counts['year'].min() - 1, movies_counts['year'].max() + 1) # starting and end points
plt.xticks(range(movies_counts['year'].min(), movies_counts['year'].max() + 1, 5)) # divied the x-axis to pariods
plt.legend("count of movies", shadow = True) # the box inside the graph, it's important when graphing multiple lines
plt.show() # to show the graph

