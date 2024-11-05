import os
from requests.auth import HTTPBasicAuth
import requests
from dotenv import load_dotenv
load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/a08309ecbf8036ba1aa39f7cc7bae46e/flightTicketDeals/prices"
class DataManager:
    def __init__(self):
        self._user = os.environ['SHEETY_USERNAME']
        self._password = os.environ['SHEETY_PASSWORD']
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    auth=self._authorization
            )
            print(response.text)
