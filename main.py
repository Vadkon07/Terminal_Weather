import pandas as pd
import requests
import json
import os

#API SETTINGS: You can choose one of two ways to enter your api key. First it's to enter him manually each time when you run this code, and the second way it's to predefine him in 'api_key'. Uncomment one of this methods below:


api_key = input("Please, enter you API key: ")
#api_key = 'ifjaghufhafhaghaghagha' (paste your key here and delete this text)

ask = 'y'

while ask == 'y':
    city = input("Input city name (ex: New York): ")
    os.system("clear")

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    data = response.json()

    os.system("clear")
    city_name = data['name']
    print()
    print("=== WEATHER IN ", city_name, "===")
    print()
    coord_lon = data['coord']['lon']
    coord_lat = data['coord']['lat']
    temp = data['main']['temp'] - 273.15
    temp_print = int(temp)
    temp_feels = data['main']['feels_like'] - 273.15
    temp_feels_print = int(temp_feels)
    info = data["dt"]
    desc = data['weather'][0]['description']
    hum = data['main']['humidity']
    print(f'Temperature: ',temp_print,'C, feels like ',temp_feels_print, 'C')
    print(f'Humidity: {hum}%')
    print(f'Description: {desc}')
    print()
    print(f'*Information was updated on {info}, for coordinates {coord_lat} {coord_lon}')
    print()

    ask = input("Do you want to search again? (y/n): ")
else:
    ask = '0'
