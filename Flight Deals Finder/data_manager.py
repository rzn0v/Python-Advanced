import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

sheety_auth = os.getenv("SHEETY_AUTH")


sheety_endpoint = os.getenv("SHEETY_ENDPOINT")


class DataManager:
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        self.response = requests.get(url=sheety_endpoint)
        self.data = self.response.json()
        self.destination_data = self.data["prices"]

        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city["id"]}", json=new_data)
