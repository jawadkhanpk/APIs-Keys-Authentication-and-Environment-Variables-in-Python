# API Reference = "https://openweathermap.org/current"

import requests
OpenWeather_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "YOUR_API_KEY_HERE"

weather_params ={
    "lat":  33.6995,
    "lon": 73.0363,
    "appid":api_key
}

responce = requests.get(OpenWeather_Endpoint,params=weather_params)
responce.raise_for_status()

print(responce.status_code)
print(responce.json())
