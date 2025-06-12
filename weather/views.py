# weather_app/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings  # We'll store the API key in settings.py


class CurrentWeatherView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        city_name = request.query_params.get('city')
        if not city_name:
            return Response({"error": "City parameter is required"}, status=400)

        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                return Response({"error": data.get("message", "Failed to fetch weather")}, status=response.status_code)

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
            }
            return Response(weather)

        except requests.exceptions.RequestException as e:
            return Response({"error": "External API request failed", "details": str(e)}, status=500)
