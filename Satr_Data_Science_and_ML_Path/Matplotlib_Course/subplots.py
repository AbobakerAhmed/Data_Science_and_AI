# Date: 29th of Sep 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# The Idea is to devied the 


# Importing
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
data = pd.read_csv("tmdb_movies_data.csv")

top_revenue_movies = data.groupby('original_title').sum().sort_values(by = 'revenue', ascending = False)
top_vote_movies = data.groupby('original_title').sum().sort_values(by = 'vote_average', ascending = False)

plt.suptitle('What are Factors Efficte on Revenue?')
# Fig 1: Bar Chart
plt.subplot(2,2,1) # there is tow rows, tow columns, and the nex char will be in index 1
plt.title('What is the Hieghest 5 Movies?')
plt.bar(
    top_revenue_movies.head(5).index,
    top_revenue_movies.head(5).revenue,
)

# Fig 3: Voting effictioncy
plt.subplot(2,2,2)
plt.title('What are the heighest genres revenues?')
plt.pie(
    data.groupby('genres').mean(numeric_only= True).sort_values(by = 'revenue',ascending= False).head().revenue,
    labels = data.groupby('genres').mean(numeric_only= True).sort_values(by = 'revenue', ascending= False).head().index,
    radius = 0.8,
    autopct= '%00.1f%%',
    startangle= 180,
    explode= [0.2, 0,0,0,0]
)


# Fig 3: Year and Revenue
plt.subplot(2,2,3)
plt.xlabel('year')
plt.ylabel('mean revenue')
plt.scatter(
    data.groupby('release_year').mean(numeric_only= True).sort_values(by = 'revenue', ascending= False).index,
    data.groupby('release_year').mean(numeric_only= True).sort_values(by = 'revenue',ascending= False).revenue
)


# Fig 4:
plt.subplot(2,2,4)
plt.xlabel('vote avetage')
plt.ylabel('mean revenue')
plt.plot(
    data.groupby('vote_average').mean(numeric_only= True).sort_values('vote_average', ascending = True).index,
    data.groupby('vote_average').mean(numeric_only= True).sort_values('vote_average', ascending = True).revenue ,
)



plt.savefig('subplots_figure.png', dpi = 300) # Must be before show() fun.

plt.show()


