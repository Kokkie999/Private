#import pandas as pd
#import requests
import urllib, json

API_KEY = "demo"
LOCATION = "Amsterdam"

endpoint = "http://weerlive.nl/api/json-data-10min.php"

params = {
    "key": API_KEY,
    "locatie": LOCATION,
}

url = f"{endpoint}?q=" + plaats + "&appid=" + key + "&units=metric"
response = urllib.urlopen(url)
data = json.loads(response.read())
temp = data['main']['temp']
print temp

# response = requests.get(url=endpoint, params=params)
# data = response.json()["liveweer"][0]
# df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')
# print (df)

