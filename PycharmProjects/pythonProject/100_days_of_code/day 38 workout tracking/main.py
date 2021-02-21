import pandas as pd
import json
import requests
from datetime import datetime
import os

with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
    api_data = json.load(data_file)


APP_ID = "2d66d9b0"
API_KEY = "809807221c8ccffbe9cf5d2fcc9762f0"
TOKEN = "rgertyjhgwwyfunyjenbuhgbuyrebgrtybh"
GENDER = "Man"
WEIGHT_KG = 81
HEIGHT_CM = 24
AGE = 51


exercise_endpoint = api_data["Nutritionix"]["endpoint"]
sheet_endpoint = api_data["Sheety"]["endpoint"]

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

    sheet_response = requests.post(f"{sheet_endpoint}/workoutTracking/workout", json=sheet_inputs, headers=bearer_headers)

    print(sheet_response)
    print(sheet_response.text)
