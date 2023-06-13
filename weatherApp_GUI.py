from tkinter import *
import requests
import json
from datetime import datetime

#Initialize the Tkinter window
root = Tk()
root.geometry("400x400") #default window size
root.resizable(0,0) #to make window size fixed
root.title("Weather App by Rishabh") #title of the window

#displaying weather
city_value = StringVar()

def showWeather():
    key = "79313bad8f2548ebb94142827231306" #WeatherAPI API-Key
    city_name = city_value.get()
    weather_url = "http://api.weatherapi.com/v1/current.json?key=" + key + "&q=" + city_name
    response = requests.get(weather_url) #Get response from the URL
    weather_info = response.json()

    tfield.delete("1.0", "end") #clear text field for every new output

    if weather_info['location']:
        name = str(weather_info['location']['name'])
        region = str(weather_info['location']['region'])
        country = str(weather_info['location']['country'])
        temp = int(weather_info['current']['temp_c'])
        feels_like = int(weather_info['current']['feelslike_c'])
        weather = f"\nRegion: {region}\nCountry: {country}\nWeather of: {name}\nTemperature (Celsius): {temp}°\nFeels Like (Celsius): {feels_like}\n"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)


city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()

Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather_now = Label(root, text = "The Weather is: ", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()

root.mainloop()
