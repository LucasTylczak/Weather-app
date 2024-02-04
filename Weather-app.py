import requests
from googletrans import Translator
from datetime import datetime, timedelta

import requests
from googletrans import Translator
from datetime import datetime, timedelta

def translate_text(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='fr').text
    return translated_text

def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Erreur lors de la récupération des données. Code d'erreur: {response.status_code}")
        return None

def display_weather_forecast(weather_data):
    banner = """
 ___       __   _______   ________  _________  ___  ___  _______   ________          ________  ________  ________   
|\\  \\     |\\  \\|\\  ___ \\ |\\   __  \\|\\___   ___\\  \\|\\  \\|\\  ___ \\ |\\   __  \\        |\\   __  \\|\\   __  \\|\\   __  \\  
\\ \\  \\    \\ \\  \\ \\   __/|\\ \\  \\|\\  \\|___ \\  \\_\\ \\  \\\\\  \\ \\   __/|\\ \\  \\|\\  \\       \\ \\  \\|\\  \\ \\  \|\  \\ \\  \|\  \\ 
 \\ \\  \\  __\\ \\  \\ \\  \\_|/_\\ \\   __  \\   \\ \\  \\ \\ \\   __  \\ \\  \\_|/_\\ \\   _  _\\       \\ \\   __  \\ \\   ____\\ \\   ____\\
  \\ \\  \\|\\__\\_\\  \\ \\  \\_|\ \\ \\  \\ \\  \\   \\ \\  \\ \\ \\  \\ \  \\ \\  \\_|\ \\ \\  \\\\  \\|       \\ \\  \\ \\  \\ \\  \___|\\ \\  \___|
   \\ \\____________\\ \\_______\\ \\__\\ \\__\\   \\ \\__\\ \\ \\__\\ \__\\ \\_______\\ \\__\\|__|        \\ \\__\\ \\__\\ \\__\\    \\ \\__\\   
    \\|____________|\\|_______|\\|__|\\|__|    \\|__|  \\|__|\\|__|\\|_______|\\|__|\\|__|         \\|__|\\|__|\\|__|     \\|__|   
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
╔═══════════════════════╦══════════════════════════╦═══════════════════════╗
║  Dev : LucasTylczak   ║  Info  : Weather app     ║  Programm  : Python   ║
╚═══════════════════════╩══════════════════════════╩═══════════════════════╝
                                                                                                                                                                                                                     
                                                                                                 """

    if weather_data:
        forecast_list = weather_data['list']

        for day_offset in [0, 1, 2]:  # Aujourd'hui, Demain, Après-demain
            forecast = forecast_list[day_offset * 8]  # Une prévision toutes les 8 heures

            date = datetime.utcfromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')
            main_info = forecast['weather'][0]['main']
            description = forecast['weather'][0]['description']
            temperature = forecast['main']['temp']
            humidity = forecast['main']['humidity']

            # Traduire les termes météorologiques en français
            main_info_fr = translate_text(main_info)
            description_fr = translate_text(description)

            print(f"\n{banner}\nJour {day_offset + 1} - {date}")
            print(f"Conditions météorologiques: {main_info_fr} - {description_fr}")
            print(f"Température: {temperature} °C")
            print(f"Humidité: {humidity}%")
    else:
        print("Aucune donnée météorologique disponible.")

if __name__ == "__main__":
    api_key = "d73e8ffd405111cdef135110d1cea124"
    city = input("Entrez le nom de la ville: ")

    weather_data = get_weather_forecast(api_key, city)

    display_weather_forecast(weather_data)

