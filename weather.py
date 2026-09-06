import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_current_weather(city):
    api_key = os.getenv("API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

    response = requests.get(url, params=params)

    return response.json()