import requests
import os
from dotenv import load_dotenv
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

bot_id = os.getenv("BOT_ID")
bot_token = os.getenv("BOT_TOKEN")

stock_key = os.getenv("STOCK_KEY")

Stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : stock_key
}
news_key = os.getenv("NEWS_KEY")

news_params = {
    "q" : "Tesla",
    "apiKey" : news_key 
}

stock_response = requests.get(STOCK_ENDPOINT, params=Stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday = list(stock_data["Time Series (Daily)"].keys())[0]
previous = list(stock_data["Time Series (Daily)"].keys())[1]
yesterday_close = round(float(stock_data["Time Series (Daily)"][yesterday]["4. close"]))
previous_close = round(float(stock_data["Time Series (Daily)"][previous]["4. close"]))

stock_difference = yesterday_close - previous_close
percentage_difference = round(stock_difference/previous_close*100)
if percentage_difference >=5 or percentage_difference<=-5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    news = [each_news for each_news in news_data["articles"][:3]]
    news_body = ""
    for msg in news:
        news_body+="".join(f"Headline: {msg["title"]}\nBrief: {msg["description"]}\n\n")
    if stock_difference > 0:
        text = f"{STOCK_NAME}: 🔺{abs(stock_difference)}%\n{news_body}"
        send_text =  'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_id + '&parse_mode=Markdown&text=' + text
        response = requests.get(send_text)
    elif stock_difference < 0:
        text = f"{STOCK_NAME}: 🔻{abs(stock_difference)}%\n{news_body}"
        send_text =  'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_id + '&parse_mode=Markdown&text=' + text
        response = requests.get(send_text)
    else: 
        print("No Major Changes")

