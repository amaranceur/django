from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
    api_key='5dcb67ef7c0a17d1a4450d3e055e4001'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, api_key, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, api_key, current_weather_url,
                                                                         forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            'weather_data1': weather_data1,
            'daily_forecasts1': daily_forecasts1,
            'weather_data2': weather_data2,
            'daily_forecasts2': daily_forecasts2,
        }

        return render(request, 'app/home.html', context)
    else:
        return render(request, 'app/home.html')

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    try:
        current_weather_response = requests.get(current_weather_url.format(city, api_key)).json()
        
        # Check if the 'coord' key exists in the response
        if 'coord' in current_weather_response:
            lat, lon = current_weather_response['coord']['lat'], current_weather_response['coord']['lon']
        else:
            # Handle the case where 'coord' is missing
            lat, lon = None, None

        weather_data = {
            'city': city,
            'temperature': round(current_weather_response['main']['temp'] - 273.15, 2),
            'description': current_weather_response['weather'][0]['description'],
            'icon': current_weather_response['weather'][0]['icon'],
        }

        forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

        daily_forecasts = []
        for daily_data in forecast_response.get('daily', [])[:5]:
            daily_forecasts.append({
                'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
                'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
                'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
                'description': daily_data['weather'][0]['description'],
                'icon': daily_data['weather'][0]['icon'],
            })

        return weather_data, daily_forecasts

    except Exception as e:
        # Handle any exceptions that may occur during the API request
        print(f"An error occurred: {str(e)}")
        return None, []

