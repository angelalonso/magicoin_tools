import csv
import time, datetime
import plotly
import plotly.offline as py
import plotly.graph_objs as go

#Magicoin data

MagiDate = []
MagiClosed = []
MagiVolume = []
MagiCap = []

with open('magicoin.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rawentry in reader:
        entry = rawentry[0].split(";")
        day = entry[0]
        MagiDate.append(datetime.datetime(int(day[0:4]), int(day[4:6]), int(day[6:8])))
        MagiClosed.append(entry[4])
        MagiVolume.append(entry[5])
        MagiCap.append(entry[6])


MagiTrace1 = go.Scatter(
    x=MagiDate,
    y=MagiVolume,
    name='Magi volume'
)
MagiTrace2 = go.Scatter(
    x=MagiDate,
    y=MagiCap,
    name='Magi cap'
)
MagiTrace3 = go.Scatter(
    x=MagiDate,
    y=MagiClosed,
    name='Magi closed'
)

#Bitcoin data

BitDate = []
BitClosed = []
BitVolume = []
BitCap = []

with open('bitcoin.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rawentry in reader:
        entry = rawentry[0].split(";")
        day = entry[0]
        BitDate.append(datetime.datetime(int(day[0:4]), int(day[4:6]), int(day[6:8])))
        BitClosed.append(entry[4])
        BitVolume.append(entry[5])
        BitCap.append(entry[6])


BitTrace1 = go.Scatter(
    x=BitDate,
    y=BitVolume,
    yaxis='y2',
    name='Bitcoin volume'
)
BitTrace2 = go.Scatter(
    x=BitDate,
    y=BitCap,
    yaxis='y2',
    name='Bitcoin cap'
)
BitTrace3 = go.Scatter(
    x=BitDate,
    y=BitClosed,
    yaxis='y2',
    name='Bitcoin closed'
)

# Volume

# Double Y Axis Layout
voldata = [MagiTrace1, BitTrace1]
vollayout = go.Layout(
    title='Volume Comparison',
    yaxis=dict(
        title='MagiCoin volume'
    ),
    yaxis2=dict(
        title='Bitcoin volume',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
volfig = go.Figure(data=voldata, layout=vollayout)
vol_plot_url = py.plot(volfig, filename='volume_compare')

# Cap

capdata = [MagiTrace2, BitTrace2]
caplayout = go.Layout(
    title='Cap Comparison',
    yaxis=dict(
        title='MagiCoin cap'
    ),
    yaxis2=dict(
        title='Bitcoin cap',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
capfig = go.Figure(data=capdata, layout=caplayout)
cap_plot_url = py.plot(capfig, filename='cap_compare')

# Closed

closeddata = [MagiTrace3, BitTrace3]
closedlayout = go.Layout(
    title='Closed Comparison',
    yaxis=dict(
        title='MagiCoin closed'
    ),
    yaxis2=dict(
        title='Bitcoin closed',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
closedfig = go.Figure(data=closeddata, layout=closedlayout)
closed_plot_url = py.plot(closedfig, filename='closed_compare')

#Example plot - Simple
#data = [MagiTrace1, MagiTrace2, MagiTrace3]
#plot_url = py.plot(data, filename='chart')


