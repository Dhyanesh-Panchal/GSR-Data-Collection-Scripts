from plotly import graph_objects as gobj
import serial
from time import sleep
import pandas as pd

# initialize the plot:
fig = gobj.FigureWidget()
fig.add_scatter()

data = pd.read_csv('./sample-data.csv')
fig
for i in range(len(data)-51):
    sleep(0.5)
    fig.data[0].y = data[i:i+50]

