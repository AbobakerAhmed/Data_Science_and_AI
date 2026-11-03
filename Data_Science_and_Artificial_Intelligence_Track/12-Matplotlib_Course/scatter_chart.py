# Date: 29th of Sep 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# Importing
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
data = pd.read_csv("tmdb_movies_data.csv")


# What is the relation between vote_average and revenue?
print(data.info())
# 1- try to drow that first to show the relation
vote_revenue = data.groupby('vote_average').sum().sort_values(by = 'revenue', ascending = False)
# print(vote_revenue) # now the data is ready

plt.scatter(
    vote_revenue.index, # X-axis
    vote_revenue.revenue.values, # Y-axis
    alpha= 0.8, # how points are clear?
    marker = "o" , # points style, look at matplotlib marker
    s = 10, # size of the marker
    label = 'Vote Average'
)
plt.scatter(
    vote_revenue.vote_count.values, # X-axis
    vote_revenue.revenue.values, # Y-axis    
    alpha= 0.2, # how points are clear?
    s = 15,
    label = 'Vote Counts'
)

plt.legend(loc = 0) # to show legends and what is its location

plt.title('What is the Relation Between Vote Count and Aerage with Revenue?\n', fontsize = 18)
plt.xlabel('Vote Average')
plt.ylabel('Revenue')



plt.show()
