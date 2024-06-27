import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USER")
GRAPH_ID = os.getenv("GRAPH_ID")
print(f"{TOKEN}/{USERNAME}/{GRAPH_ID}")
endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{endpoint}/{USERNAME}/graphs"

User_token = {
    "X-USER-TOKEN" : TOKEN
}

graph_params = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji"
}


today = datetime.datetime.now()

formatted_day = today.strftime("%Y%m%d")



quantity = float(input("The distance you traveled today: (in kms)"))

# response = requests.post(url=graph_endpoint, json=graph_params, headers=User_token)
# print(response.text)
graph_update_params = {
    "date" : str(formatted_day),
    "quantity" : str(quantity)
}

response = requests.post(url=f"{endpoint}/{USERNAME}/graphs/{GRAPH_ID}", json=graph_update_params, headers=User_token)
print(response.text)
