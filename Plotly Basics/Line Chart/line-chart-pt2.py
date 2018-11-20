# basic.py
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../SourceData/nst-est2017-alldata.csv')
df2 = df[df['DIVISION'] == '1']
# Filter only for the Northeast States

df2.set_index('NAME', inplace = True)
# Sets the index as the NAME
# inplace ensures the transformation is done
# without forcing a line for reassignmeny

list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
# List Comprehension that only selects the columns that start with Pop

df2 = df2[list_of_pop_col]
# Filtered out based off the list of column names


data = [ go.Scatter(x=df2.columns,
                    y=df2.loc[name], # Grabs the number value @ each name in each column
                    mode='lines',
                    name=name) for name in df2.index]
                    # the name column and name parameter refer to the state name
pyo.plot(data)
