from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_current_weather

class CurrentWeatherView(APIView):
    def get(self, request):
        city = request.GET.get('city')
        if not city:
            return Response({'error': 'City is required'}, status=status.HTTP_400_BAD_REQUEST)
        data = get_current_weather(city)
        return Response(data)
