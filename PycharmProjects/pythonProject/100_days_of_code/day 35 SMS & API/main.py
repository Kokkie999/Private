import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_apiKey = "420b76cf820dd44a2ee56a31fbf24e3f"
#OWM_apiKey = os.environ.get("OWM_API_KEY")
account_sid = "ACded0659b3cf8aeb9efbac4621f742e5d"
auth_token = "afb7ed24d57a0208bf11bf095055797a"

weather_params = {
    # "lat": "52.167137",
    # "lon": "4.634807",
    "lat": "49.542801",
    "lon": "28.036854",
    "appid": OWM_apiKey,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]


will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+12342353373",
        to="+31615633707"
    )

    print(message.status)
