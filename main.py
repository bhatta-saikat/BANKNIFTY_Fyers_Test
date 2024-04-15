import streamlit as st,pandas as pd,numpy as np,yfinance as yf
import plotly.express as px
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import pandas_ta as ta
from datetime import date
from nsepy import get_history
import datetime
import yfinance as yf
import mplfinance as mpf

Start_Date =datetime.datetime.now() - datetime.timedelta(days=600)
End_Date = datetime.datetime.now()

st.title("Stock Market Dashboard")
ticker = st.sidebar.text_input("Ticker",value ="SBIN")
Start_Date = st.sidebar.date_input("Start-Date")
End_Date = st.sidebar.date_input("End-Date")



df = yf.download(f"{ticker}.NS",start=Start_Date,end=End_Date,interval='1d')
df['EMA12'] = df.Close.ewm(span=12).mean()
df['%Changes'] = round(((df['Close']-df['Open'])/df['Open'])*100,3)
df

fig = px.line(df,x=df.index,y=df['Close'],title=f"{ticker}-Graph Analysis")
st.plotly_chart(fig)

