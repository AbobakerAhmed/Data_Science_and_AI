# Date: 29th of Sep 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# Importing
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
data = pd.read_csv("tmdb_movies_data.csv")


# We need to know the catigories of movies depending on revenue
# group the table depending on the genres column, and sort them, the set the genres as the index
n = 5
top_revenue = data.groupby('genres').sum().sort_values(by = 'revenue', ascending = False)['revenue'][0:n]
# print(top_revenue)

# colors = ['r','g','b','black','gray'] # back to matplotlib colors to show each of them
plt.pie(
    top_revenue.values, # values
    labels= top_revenue.index, # Lables
#    colors = colors, # we don't need to change these colors
    startangle = 180, # the angle where the 1st catigory will be started in
    radius = 1.2, # the size of the circle
    autopct = '%00.2f%%', # showing the percentages of each of catigory and to how many dicimal digits
    explode = [0.2,0,0,0,0], # the dictence between each part and other parts
)
plt.title('Top 5 Catigories Depending on Revenue\n', fontsize = 26, loc = 'center')
plt.show()


