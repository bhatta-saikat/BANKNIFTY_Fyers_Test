import warnings
warnings.filterwarnings('ignore')
import time
import os
import datetime
import pandas as pd

Lots = 1
LotSize = 15
Profit_Points = 30
Loss_Points = 10

qty = LotSize*Lots
interval = 30
PE_Gap = 200
CE_Gap = 200

TotalProfit = Profit_Points*qty
TotalLoss = Loss_Points*qty

TRADED_SYMBOL = []
stoploss = 100
StockSymbol = "NSE:BANKNIFTY24APRFUT"

#Common_String = 'NSE:BANKNIFTY24424'
Common_String = 'NSE:BANKNIFTY24APR'

Fin_FNOsymbol = "BANKNIFTY 22SEP23"
localtime = time.localtime()

Profit_per_Trade = 5000

Start_Date =datetime.datetime.now() - datetime.timedelta(days=60)
End_Date = datetime.datetime.now()

closingTime = int(23) * 60 + int(59)
orderPlaceTime = int(0) * 60 + int(3)
