import Common
import json
import requests
import time
import pyotp
import os
import requests
from urllib.parse import parse_qs,urlparse
import sys
from fyers_api import fyersModel
from fyers_api import accessToken
import streamlit as st

import warnings
warnings.filterwarnings('ignore')
import pandas_ta as ta
from fyers_api import fyersModel, accessToken
from datetime import datetime, timedelta
import time
import os
import datetime
import pandas as pd

import json
import requests
import time
import pyotp
import os
import requests
from urllib.parse import parse_qs,urlparse
import sys
from fyers_api import fyersModel
from fyers_api import accessToken

from datetime import datetime, timedelta
import datetime

from fyers_apiv3 import fyersModel

redirect_uri = "http://127.0.0.1:5000/login"
client_id='JKRFLKWBAI-100'
secret_key = 'IMOJFE3DVX'
FY_ID = "XM11096"  # Your fyers ID
TOTP_KEY = "KN4BIMFJARM4YCX6UVHUI6FGKP4MUIXZ"  # TOTP secret is generated when we enable 2Factor TOTP from myaccount portal
PIN = "4663"  # User pin for fyers account

from fyers_apiv3 import fyersModel


"""
In order to get started with Fyers API we would like you to do the following things first.
1. Checkout our API docs :   https://myapi.fyers.in/docsv3
2. Create an APP using our API dashboard :   https://myapi.fyers.in/dashboard/

Once you have created an APP you can start using the below SDK 
"""

#### Generate an authcode and then make a request to generate an accessToken (Login Flow)

                         ## app_secret key which you got after creating the app
grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
response_type = "code"                             ## The response_type always has to be "code"
state = "sample"                                   ##  The state field here acts as a session manager. you will be sent with the state field after successfull generation of auth_code


### Connect to the sessionModel object here with the required input parameters
appSession = fyersModel.SessionModel(client_id = client_id, redirect_uri = redirect_uri,response_type=response_type,state=state,secret_key=secret_key,grant_type=grant_type)

# ## Make  a request to generate_authcode object this will return a login url which you need to open in your browser from where you can get the generated auth_code
generateTokenUrl = appSession.generate_authcode()
#generateTokenUrl

from datetime import datetime, timedelta, date
from time import sleep
import os
import pyotp
import requests
import json
import math
import pytz
from urllib.parse import parse_qs, urlparse
import warnings
import pandas as pd

pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')
import base64


def getEncodedString(string):
    string = str(string)
    base64_bytes = base64.b64encode(string.encode("ascii"))
    return base64_bytes.decode("ascii")


URL_SEND_LOGIN_OTP = "https://api-t2.fyers.in/vagator/v2/send_login_otp_v2"
res = requests.post(url=URL_SEND_LOGIN_OTP, json={"fy_id": getEncodedString(FY_ID), "app_id": "2"}).json()
#print(res)

if datetime.now().second % 30 > 27: sleep(5)
URL_VERIFY_OTP = "https://api-t2.fyers.in/vagator/v2/verify_otp"
res2 = requests.post(url=URL_VERIFY_OTP,
                     json={"request_key": res["request_key"], "otp": pyotp.TOTP(TOTP_KEY).now()}).json()
#print(res2)

ses = requests.Session()
URL_VERIFY_OTP2 = "https://api-t2.fyers.in/vagator/v2/verify_pin_v2"
payload2 = {"request_key": res2["request_key"], "identity_type": "pin", "identifier": getEncodedString(PIN)}
res3 = ses.post(url=URL_VERIFY_OTP2, json=payload2).json()
#print(res3)

ses.headers.update({
    'authorization': f"Bearer {res3['data']['access_token']}"
})

TOKENURL = "https://api-t1.fyers.in/api/v3/token"
payload3 = {"fyers_id": FY_ID,
            "app_id": client_id[:-4],
            "redirect_uri": redirect_uri,
            "appType": "100", "code_challenge": "",
            "state": "None", "scope": "", "nonce": "", "response_type": "code", "create_cookie": True}

res3 = ses.post(url=TOKENURL, json=payload3).json()
#print(res3)

url = res3['Url']
#print(url)
parsed = urlparse(url)
auth_code = parse_qs(parsed.query)['auth_code'][0]
auth_code

grant_type = "authorization_code"

response_type = "code"

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

session.set_token(auth_code)
response = session.generate_token()
access_token = response['access_token']

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path=os.getcwd())

#fyers.get_profile()

print("Login Sucessful in Fyers Account.....!")

Start_Date =Common.Start_Date
End_Date = Common.End_Date

#st.title("BANKNIFTY Algo Based Trading")
st.subheader("BANKNIFTY Expiry Day PE Buy Strategy....")
ticker = st.sidebar.text_input("Ticker",value ="BANKNIFTY")
Gap = st.sidebar.text_input("Gap-OTM",value =f"{Common.PE_Gap}")
Start_Date = st.sidebar.date_input("Start-Date")
End_Date = st.sidebar.date_input("End-Date")

#COMMON DECLEARATION NEED FOR TRADE
qty = Common.qty
interval = 10
Gap = Common.PE_Gap

TRADED_SYMBOL = []
stoploss = 100
#StockSymbol =  Common.StockSymbol
StockSymbol = "NSE:NIFTYBANK-INDEX"
Common_String = Common.Common_String
localtime = time.localtime()

Profit_per_Trade = 5000

Start_Date = Common.Start_Date
End_Date = Common.End_Date
orderPlaceTime = Common.orderPlaceTime

Text1 = text_placeholder = st.empty()
Text2 = text_placeholder = st.empty()
Text3 = text_placeholder = st.empty()
Text9= text_placeholder = st.empty()
Text4= text_placeholder = st.empty()
Text7= text_placeholder = st.empty()
Text8= text_placeholder = st.empty()


Text6= text_placeholder = st.empty()
Data1 = df_placeholder = st.empty()

Text5= text_placeholder = st.empty()
Data2 = df_placeholder = st.empty()


def getTime():
    return datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
localtime = time.localtime()



def check_Signal():
    #CHECK BANKNIFTY SPOT VALUE & TARGET VALUE
    data = {"symbol": StockSymbol, "ohlcv_flag": "1"}
    Msg = Fyers.fyers.depth(data)['d']
    df = pd.DataFrame(Msg)
    df = df.T
    LTP = df['ltp'].iloc[0]
    #LTP

    ltp = LTP
    SPOT_VALUE = (int(ltp / 100) * 100)
    StrikePrice = (int(ltp / 100) * 100) - Gap

    #Negetive Sign as it ITM
    SpotValue_PE = f'{Common_String}{StrikePrice}PE'

    Text2.markdown(f'BANKNIFTY-FUTURE LTP is = {LTP}')
    Text3.markdown(f'SPOT PRICE Is= {SPOT_VALUE}')
    Text9.markdown(f'TARGET PRICE-GAP Is= {Gap}')
    Text4.markdown(f'TARGET StrikePrice Is= {StrikePrice}')

    # print(f'TARGET StrikePrice CODE Is= {SpotValue_PE}')
    Text7.text(f'Check {SpotValue_PE} for Trade Signal')
    Check_Option_PE_Trade_Signal(StockSymbol,SpotValue_PE)

def Check_Option_PE_Trade_Signal(StockSymbol,SpotValue_PE):
        #CHECK FOR TRADE SIGNAL
        data = {"symbol": SpotValue_PE, "ohlcv_flag": "1"}
        Msg = Fyers.fyers.depth(data)['d']
        df = pd.DataFrame(Msg)
        df = df.T
        PE_LTP = df['ltp'].iloc[0]
        ltp = PE_LTP


        ltp = PE_LTP
        Text8.text(f'BANKNIFTY OPTX PRICE {SpotValue_PE} LTP iS = {PE_LTP}')

        data = {"symbol": SpotValue_PE, "resolution": "5", "date_format": "1",
                "range_from": Start_Date.strftime('%Y-%m-%d'),
                "range_to": End_Date.strftime('%Y-%m-%d'), "cont_flag": "1"}

        historicaldata = Fyers.fyers.history(data)
        res_json = historicaldata
        try:
            hist_data = Fyers.fyers.history(data)
        except Exception as e:
            raise e
        df = pd.DataFrame(hist_data['candles'], columns=['date', 'Open', 'High', 'Low', 'Close', 'Volume'])

        df['date'] = pd.to_datetime(df['date'], unit="s", utc=True)
        df['date'] = df['date'].dt.tz_convert('Asia/Kolkata')
        df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
        df['SMA_14'] = ta.sma(df.Close, length=20)
        df['Stdv'] = df.Close.rolling(window=20).std()
        df['Up_BB'] = df.SMA_14 + 2 * df.Stdv
        df['Lo_BB'] = df.SMA_14 - 2 * df.Stdv

        df["PP"] = (df["High"] + df["Low"] + df["Close"]) / 3
        df["R1"] = df["PP"] * 2 - df["Low"]
        df["S1"] = df["PP"] * 2 - df["High"]

        df["PP"] = df["PP"].shift(1)
        df["R1"] = df["R1"].shift(1)
        df.dropna(inplace=True)

        df['RSI'] = ta.rsi(df.Close, length=14)
        df = df.round(decimals=2)

        #df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)

        df['Buy'] = 0
        df = df.round(decimals=2)
        df = df[['Close', 'Up_BB', 'RSI', 'PP','R1', 'Buy', ]]

        n = 14
        for i in range(n, len(df)):
            if df['Close'][i - 1] < df['Up_BB'][i - 1] and df['Close'][i] > df['Up_BB'][i] and df['Close'][i - 1] < df['R1'][i - 1] and df['Close'][i] > df['R1'][i] and df['RSI'][i] >65:
                df['Buy'][i] = 1

        time.sleep(2)
       
        df2 = df[(df['Buy'] > 0)]
        Text5.markdown(f'<u><b>Last Trade Signals</b></u>',unsafe_allow_html=True)
        Data2.write(df2.tail(4))      
        

        time.sleep(2)
        Text6.markdown(f'<u><b>Current Historical Signals</b></u>',unsafe_allow_html=True)
        Data1.write(df.tail(3))
   
    

        time.sleep(2)
        df1 = df.iloc[-1]
        # print(df1)
        if df1['Buy'] == 1:
            data = {"symbol": SpotValue_PE, "qty": qty, "type": 2, "side": 1, "productType": "INTRADAY",
                    "limitPrice": 0, "stopPrice": 0, "validity": "DAY", "disclosedQty": 0, "offlineOrder": "False",
                    "stopLoss": 0, "takeProfit": 0}
            print(Fyers.fyers.place_order(data))

            TRADED_SYMBOL.append(StockSymbol)
        return df

def main():
    global fyers
    timeNow = (datetime.datetime.now().hour*60 + datetime.datetime.now().minute)
    Hour = orderPlaceTime // 60
    Min = orderPlaceTime % 60
    print(f'Trade Will Be Started From {Hour}:{Min} AM, Present Time {getTime()} ')


    while timeNow < Common.orderPlaceTime:
        time.sleep(0.2)
        timeNow = (datetime.datetime.now().hour*60 + datetime.datetime.now().minute)
    print(f'Ready for Trading, Present Time {getTime()}/ Trade Close Time = {Common.closingTime//60}:{Common.closingTime%60} PM')


    while timeNow < Common.closingTime:
        result = datetime.datetime.now().strftime("%I:%M:%S %p")        
        Text1.markdown(f"<u>Code will run after Every {interval} sec Interval , Current Time is-{result}</u>",unsafe_allow_html=True)
        #st.write('*****************************************************************************************************')
        #st.write(f"Code will run after {interval} sec                                  Current Time-{result}")
        #st.write('------------------------------------------------------------------------------------------------------')
        time.sleep(interval)
        #check_PL()
        check_Signal()



if __name__ == '__main__':
    main()
