# Date: 2nd of Oct 2025
# Abobaker Ahmed Khidir Hassan
# Course: Matplotlib Liblrary
# Platform: Satr.codes

# Final Project



# 1- Import the lib
from matplotlib import markers
import matplotlib.pyplot as plt


# 1- make a line chart using x, y materxes
x = [1,2,3,4,5,6,7]
y = [1,2,3,5,8,13,20]
# 2- Create a 2 Line Charts with the same values with doing the following:
    # a) put any point with a circle marker
    # b) make the marker size = 10
    # c) use dashed lines
    # d) make the line width = 3
    # e) add lagends named "Normal" for x and "Fast" for y

plt.plot(
    x, # Q1
    y, # Q1
    marker = 'o', # a
    markersize = 10, # b
    linestyle = "-.", # c
    linewidth = 3, # d
)
# e:
plt.xlabel('Normal')
plt.ylabel('Fast')
plt.show()


# Q3: Create Subplot chart of the code with doning the following:
 # a) put all charts in one row
 # b) add a title for each of them
 # c) add a general title named my data visulaization assignment

import numpy as np

#super title = my data visulaization assignment
plt.suptitle('my data visulaization assignment')

#title = First Chart
plt.subplot(1,3,1)
plt.title('Chart Number 1')
x_plot1 = np.array([1, 2, 3, 4, 5, 6, 7])
y_plot1 = np.array([1, 1, 2, 3, 5, 8, 13])
plt.plot(x_plot1, y_plot1)

#title = Second Chart
plt.subplot(1,3,2)
plt.title('Chart Number 2')
x_plot2 = np.array([0, 1, 2, 3, 4, 5, 6])
y_plot2 = np.array([2, 4, 6, 8, 10, 12, 14])
plt.scatter(x_plot2, y_plot2)

#title = Third Chart
plt.subplot(1,3,3)
plt.title('Chart Number 3')
x_plot3 = np.array([0, 1, 3, 4])
y_plot3 = np.array([4, 6, 3, 4])
plt.plot(x_plot3, y_plot3)

plt.show()


