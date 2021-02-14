import requests
# from twilio.rest import Client

STOCK_NAME = "FLOW.AMS"
COMPANY_NAME = "Flow Traders"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY =
NEWS_API_KEY =
# TWILIO_SID =
# TWILIO_AUTH_TOKEN =

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key,value) in stock_data.items()]
yesterday_closing_price = float(stock_data_list[0]["4. close"])

day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

dif_percent = round((difference / yesterday_closing_price) * 100)

if abs(dif_percent) >= 0.5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    three_articles = news_data[:3]

    formated_articles = [f"{STOCK_NAME}: {up_down}{dif_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    # client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    #
    # for article in formated_articles:
    #     message = client.messages.create(
    #         body=article,
    #         from_="+12342353373",
    #         to="+31615633707"
    #     )

    print(yesterday_closing_price)
    print(day_before_yesterday_closing_price)
    print(difference)
    print(dif_percent)
    print(formated_articles)

