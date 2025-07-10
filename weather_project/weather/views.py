import datetime
import requests
from django.shortcuts import render


def index(request):
    city = 'Kharagpur'  # default city
    weather_data = {}
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city', 'Kharagpur')

    api_key = '0b5796e5e4690515b7de8cd726c95e88'  # Replace with your valid API key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and 'weather' in data:
        weather_data = {
            'city': city,
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon'],
            'temperature': data['main']['temp'],
            'date': datetime.date.today()
        }
    else:
        error_message = data.get('message', 'City not found or API error.')

    context = {
        'weather': weather_data,
        'error': error_message
    }

    return render(request, 'weather/index.html', context)
