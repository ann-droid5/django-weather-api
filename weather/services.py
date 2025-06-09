import requests
from django.conf import settings

def get_current_weather(city):
    api_key = settings.WEATHER_API_KEY
    print("API KEY:", api_key) 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "City not found"}
