import json

with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
    api_data = json.load(data_file)

ENDPOINT = api_data['Tequila']['endpoint']
API_KEY = api_data['Tequila']['api_key']

class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code