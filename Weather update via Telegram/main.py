import requests
lat = 0.00
lon = 0.00

api_key = ""

bot_token = ""
bot_chat_id = ""

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True

if will_rain:
    bot_message = "It's going to rain today. Remember to bring an ☔"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    response1 = requests.get(send_text)

    