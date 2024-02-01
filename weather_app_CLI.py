from configparser import ConfigParser
import requests
import json

#helped by a friend
def _get_api_key():
    config = ConfigParser()
    config.read("D:\Projects\Weather App\secrets.ini")
    return config['weather']["api_key"]

city_name = str(input())
key = _get_api_key()
weather_url = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + city_name
response = requests.get(weather_url)
info = response.json()

if info['location']:
    region = str(info['location']['region'])
    country = str(info['location']['country'])
    temp = int(info['current']['temp_c'])
    feels_like = int(info['current']['feelslike_c'])
    weather = f"City: {city_name}\nRegion: {region}\nCountry: {country}\nTemperature: {temp}\nFeels Like: {feels_like}\n"
    print(weather)
else:
    print("Error! Enter valid location")
