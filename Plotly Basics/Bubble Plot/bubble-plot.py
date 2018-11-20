import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../Data/mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'], # Text displays what appears when I hover a point
                    mode='markers',
                    marker=dict(size=df['weight']/100, # Affect relevance of size
                                color=df['cylinders'],
                                showscale=True)
                    )]

layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='bubble-plot.html')
