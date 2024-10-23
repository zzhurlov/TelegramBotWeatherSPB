import requests
from pprint import pprint
from datetime import date

def get_weather_text(token) -> str:
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={token}&q=Saint-Petersburg&aqi=no&lang=ru"
        r = requests.get(url)
        data = r.json()

        d = date.today().isoformat()
        temperature = data["current"]["temp_c"]
        cloud_text = data["current"]["condition"]["text"]
        feelslike = data["current"]["feelslike_c"]
        wind_speed = data["current"]["wind_kph"]
        humidity = data["current"]["humidity"] # влажность
        last_update = data["current"]["last_updated"]

        return f"Дата: {d}\nТемпература: {temperature} °С, {cloud_text}\nОщущается как {feelslike} °С\nСкорость ветра: {wind_speed} км/ч\nВлажность: {humidity}%\nПоследнее обновление: {last_update}\n"


    except Exception:
        return "Ошибка!"
