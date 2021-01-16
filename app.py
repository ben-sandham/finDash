# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import yfinance as yf
import pandas as pd
from dash.dependencies import Input, Output

from controls import PERIODS

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Financial Analysis Dashboard'),

    dcc.Input(
        id="tick-input",
        placeholder="input ticker symbol",
        value='MSFT',
        debounce=True,
        style={'width': '300px'}

    ),

    dcc.RadioItems(
        id="period-interval",
        options=[{'label': interval, 'value': interval} for interval in PERIODS],
        value='5d',
        labelStyle={'display': 'inline-block'}
    ),

    dcc.Graph(
        id='close-price-graph'
    )
])

# Helper function
def create_df(ticker, interval):

    return df

@app.callback(
    Output('close-price-graph', 'figure'),
    [Input('tick-input', 'value'),
    Input('period-interval', 'value')]
)
def close_price_plot(ticker, interval):
    tick = yf.Ticker(ticker)
    df = tick.history(period=interval)
    df = df.loc[:,'Close']
    fig = px.line(df, 
                x=df.index, 
                y="Close", 
                title="<b>{}   {}</b> <br> Close Price (USD)".format(tick.info['longName'], tick.info['symbol']), 
                labels={"Close":"Close Price (USD)"})
    fig.update_xaxes(tickformat="%m-%d-%Y")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)