#!/usr/bin/python
#
# Using graph_objects
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('all_data.csv')

fig = go.Figure([go.Bar(x=df['SUM'], y=df['Month']/df['Month'])])
fig.show()
