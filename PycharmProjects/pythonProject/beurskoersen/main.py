import pandas as pd
import requests

STOCK_FLOW_TRADERS = "FLOW.AMS"
COMPANY_NAME_FLOW = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY =

def stock_price(stock_name):
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_name,
        "apikey": STOCK_API_KEY,
    }
    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
    data = pd.DataFrame.from_dict(stock_data)


    return data

df_FLOW = stock_price(stock_name=STOCK_FLOW_TRADERS)

print(df_FLOW)
#stock_data_list = [value for (key,value) in stock_data.items()]
#yesterday_closing_price = float(stock_data_list[0]["4. close"])

#day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])

#print(stock_data)




#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=EPA: AF&apikey=A4CTJMCW193KYCGF