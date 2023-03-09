
#import talib as ta

import streamlit as st
import yfinance as yf 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.write("""
# Apple stock price 

Historical data for the last 13 years (one day resolution) with volumes 
""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-07-01', end = '2023-07-01')
#tickerDf['120SMA'] = ta.SMA(tickerDf.Close, 120)


fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Candlestick(x=tickerDf.index, open=tickerDf.Open, high=tickerDf.High,
                low=tickerDf.Low, close=tickerDf.Close, name="AAPL"), secondary_y=True)

fig.add_trace(go.Bar(x=tickerDf.index, y=tickerDf.Volume, opacity = 0.4, showlegend=False, name = 'Volume'),
               secondary_y=False)

#ema_trace = go.Scatter(x=tickerDf.index, y=tickerDf['120SMA'], mode='lines',
#                        name='120-day SMA')
#fig.add_trace(ema_trace, secondary_y=True)


fig.update(layout_xaxis_rangeslider_visible=False)
fig.update_layout(hovermode="x unified", width=800, height=600)
fig.layout.yaxis2.showgrid=False

st.plotly_chart(fig)
