import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT = 60.5
HEIGHT = 185
AGE = 21

APP_ID = "aafdc08b"
APP_KEY = "e7954ea5be3ae8e1171bb23c451f1db2"

BASIC_TOKEN = "c2hpdGlrYW50aGE6U2hpdGlrYW50aGFAMTE"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me the exercise you did? : ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workout"
SHEET_ENDPOINT = "https://api.sheety.co/1b18138c7e7fdeda7a23fc1835a8d2bd/shitikanthaWorkouts/workouts"

for exercises in result["exercises"]:
    sheet_params = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": today_time,
            "exercise": exercises["name"].title(),
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_params, auth=("shitikantha","Shitikantha@11",))
