import requests
import json

with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
    api_data = json.load(data_file)

ENDPOINT = f"{api_data['Sheety']['endpoint']}/flightDeals/prices"
HEADERS = {
    "Authorization": f"Bearer {api_data['Sheety']['token']}",
    "Content-Type": "application/json",
}


class DataManager:

    def __init__(self):
        self.destination_data = {}


    def get_destination_data(self):
        response = requests.get(url=ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT}/{city['id']}",
                headers=HEADERS,
                json=new_data
            )
            print(response.text)
