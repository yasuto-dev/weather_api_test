from contextvars import Context
from django.shortcuts import render
from matplotlib.style import context
import requests
from .models import City

def index(request):

    city = request.POST.get("city_name")

    # city = "Tokyo"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=397b3421758bb13b9e90c554ed5ed356'

    cities = City.objects.all() #return all the cities in the database



    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather':weather}
    # print(context)
    return render(request, 'weather/index.html',context) #returns the index.html template

      