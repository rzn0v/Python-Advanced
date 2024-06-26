import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
app_id = os.getenv("X_APP_ID")
app_key = os.getenv("X_APP_KEY")
authorization = os.getenv("AUTHORIZATION")

now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H:%M:%S")

domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/b1861502d152549854dad876f1de772d/copyOfMyWorkouts/workouts"

authentication = {
    "x-app-id" : app_id,
    "x-app-key" : app_key
}

sheet_header = {
    "Authorization" : authorization
}

body = {
    "query" : input("Enter your activity: ")
}

response = requests.post(url=f"{domain}{endpoint}", headers=authentication, json=body)
data = response.json()


duration = data["exercises"][0]["duration_min"]
name = data["exercises"][0]["name"].title()
calories = data["exercises"][0]["nf_calories"]

body = {
    "workout" : {
        "date" : formatted_date,
        "time" : formatted_time,
        "exercise" : name,
        "duration" : duration,
        "calories" : calories
    }
}

response1 = requests.post(url=sheety_endpoint, json=body, headers=sheet_header)
