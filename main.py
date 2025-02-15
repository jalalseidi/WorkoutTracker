import requests
from datetime import datetime

# User Data
GENDER = "Male"
WEIGHT_KG = 90
HEIGHT_CM = 180
AGE = 30

# API Credentials
BEARER_TOKEN = "AAAAABBBBBEEEEE12345RRRRRTTTTT56789JA"
SHEETY_URL = "https://api.sheety.co/a1776bed53430a67045c94021b85d79f/myWorkouts/workouts"
BASE_URL = "https://trackapi.nutritionix.com/"
ENDPOINT = "v2/natural/exercise"
APP_ID = "4eaf312c"
API_KEY = "62ebc28c2c1f3c81755d2d830a2f8c66"

# Date and Time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Headers for Nutritionix API
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

# Get user input
exercise_text = input("Tell me which exercises you did: ")

# Payload for Nutritionix API
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Making the POST request to Nutritionix
response = requests.post(f"{BASE_URL}{ENDPOINT}", json=parameters, headers=nutritionix_headers)
result = response.json()

# Headers for Sheety API
sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

# Send data to Sheety
for exercise in result.get("exercises", []):  # Using `.get()` to avoid KeyError
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # POST request to Sheety
    sheety_response = requests.post(SHEETY_URL, json=sheet_inputs, headers=sheety_headers)

    # Print Sheety API response
    print(sheety_response.json())
