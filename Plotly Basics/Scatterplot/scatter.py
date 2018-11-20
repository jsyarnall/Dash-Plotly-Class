# basic.py

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker=dict(
                        size=12,
                        color='rgb(51,204,153)',
                        symbol='pentagon',
                        line= {'width':2}
                    ))]
# Data Variable is always a list

layout = go.Layout(title='Hello First Plot',
                    xaxis= {'title':'MY X AXIS'},
                    yaxis= dict(title='MY Y AXIS'),
                    hovermode='closest')
# Have to pass in axis titles as dictionaries
# Commonly use dict() instead of {}'s
# Hovermode = 'closest' displays both axis values when cursor is over it

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')
# There is a default filename
