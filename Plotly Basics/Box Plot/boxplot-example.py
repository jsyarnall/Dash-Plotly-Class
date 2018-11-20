import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

# Boxpoints shows all the points in the boxplot
# Can also have the boxpoints only show 'outliers'
data = [go.Box(y=snodgrass, name='Snodgrass' ),
        go.Box(y=twain, name='Twain')]
pyo.plot(data, filename='Snodgrass-vs-Twain.html')
