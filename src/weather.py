import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1"
    response = requests.get(f"{base_url}/current.json?key={api_key}&q={city}&aqi=no")
    if response.status_code == 400:
        text = "No matching location found."
        is_ephemeral = True
        return text, is_ephemeral
    elif response.status_code == 200:
        json_data = response.json()
        location = json_data["location"]["name"]
        current_temp = json_data["current"]["temp_c"]
        condition = json_data["current"]["condition"]["text"]
        text = f"It is currently {current_temp}c in {location}, and the condition is {condition}"
        is_ephemeral = False
        return text, is_ephemeral
    else:
        text = f"error. received response {response.status_code}"
        is_ephemeral = True
        return text, is_ephemeral