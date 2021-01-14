# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import yfinance as yf
import pandas as pd

from controls import PERIODS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

tick = yf.Ticker('IPOF')

df = tick.history(period='max')
df = df.loc[:, 'Close']

fig = px.line(df, x=df.index, y="Close", title="Closing Price Chart", labels={"Close":"Close Price (USD)"})

app.layout = html.Div(children=[
    html.H1(children='Stock Chart Example'),

    dcc.Input(
        id="tick-input",
        placeholder="input ticker symbol"
    ),

    dcc.Dropdown(
        id="period-interval",
        multi=True,
        value=[interval for interval in PERIODS]
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

def create_close_price_df(ticker, period='1y'):
    tick = yf.Ticker(ticker)
    df = tick.history(period=period)
    df = df.loc[:, "Close"]
    return df

# @app.callback(
#     Output("")
# )

if __name__ == '__main__':
    app.run_server(debug=True)