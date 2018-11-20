#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../../Data/iris.csv')

# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
trace1 = df[df['class']=='Iris-setosa']['petal_length']
trace2 = df[df['class']=='Iris-versicolor']['petal_length']
trace3 = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
data = [trace1, trace2, trace3]
group_labels = ['Setosa', 'Versicolor', 'Virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data=data,
                            group_labels=group_labels)

pyo.plot(fig, filename='dist-solution.html')
