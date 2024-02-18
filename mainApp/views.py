from django.shortcuts import render
import requests

# Create your views here.
def homePage(Request):
    city = Request.GET.get('city','delhi')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=fc0b8aa02188cc731fe9155c714a4a32'
    data = requests.get(url).json()
    load = {'city':data['name'],
            'weather':data['weather'][0]['main'], 
            'icon':data['weather'][0]['icon'], 
            'kelvin_temperature':data['main']['temp'], 
            'celcius_temperature':int(data['main']['temp']-273), 
            'pressure':data['main']['pressure'], 
            'humidity':data['main']['humidity'],
            'description':data['weather'][0]['main'],
            }
    context = {'data': load}
    return render(Request,"index.html",context)
