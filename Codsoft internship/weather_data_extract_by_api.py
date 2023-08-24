import requests
import json

my_api_key = "8733f05cb1f845fcc31cff434f208084"
weather_api_url = "https://api.openweathermap.org/data/2.5/weather?"
city = input("Enter City Name ")
concatenate_url = weather_api_url + "q=" + city + "&appid=" + my_api_key
response = requests.get(concatenate_url)




if response.status_code == 200:
    data = response.json()
    main = data['main']
    temprature = main['temp']
    temp_feels_like = main['feels_like']
    humidity = main['humidity']
    pressure = main['pressure']
    wind = data['wind']
    weather = data['weather']

    print(f"{city:-^35}")
    print(f"Temprature: {temprature}")
    print(f"Feel like: {temp_feels_like}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather report: {weather[0]['description']}")
    print(f"Wind speed: {wind['speed']}")
    print(f"Timezone: {data['timezone']}")
else:
    print("Api or url not loaded try again!")

