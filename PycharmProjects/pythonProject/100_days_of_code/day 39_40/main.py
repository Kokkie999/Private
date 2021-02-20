#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# APP_ID = "2d66d9b0"
# API_KEY = "a065213639875dfac51e3eb2d418fbfb"
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = os.environ["YOUR_SHEET_ENDPOINT"]
#
#
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }
#
# parameters = {
#     "query": exercise_text,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT_CM,
#     "age": AGE
# }
#
# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)

import requests
from datetime import datetime
import os


GENDER = "Man"
WEIGHT_KG = 81
HEIGHT_CM = 24
AGE = 51

APP_ID = "2d66d9b0"
API_KEY = "809807221c8ccffbe9cf5d2fcc9762f0"
TOKEN = "rgertyjhgwwyfunyjenbuhgbuyrebgrtybh"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/912ff3bb64d3c161c53e9b4cf247006e/workoutTracking/workout"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response)
    print(sheet_response.text)