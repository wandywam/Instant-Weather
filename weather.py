import requests
import os
from dotenv import load_dotenv
from colorama import Fore, Style, init

init(autoreset=True) #if for windows use for colorama

def get_weather_emoji(condition):
    condition = condition.lower()
    if "sun" in condition or "clear" in condition:
        return "☀️"
    elif "cloud" in condition or "overcast" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "snow" in condition:
        return "❄️"
    elif "thunder" in condition:
        return "⛈️"
    elif "fog" in condition or "mist" in condition:
        return "🌫️"
    else:
        return "🌈"


load_dotenv()
key = os.getenv("WEATHER_API_KEY")
url = "http://api.weatherapi.com/v1/current.json"

quitVar = False
while not quitVar:

    location = input("\nEnter a location (e.g Los Angeles, CA): ")

    parameters = {"key": key, "q": location}

    response = requests.get(url, params = parameters)
    data = response.json()

    if response.status_code == 200:

        name = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        
        temp_f = data["current"]["temp_f"]
        condition = data["current"]["condition"]["text"]
        feelslike_f = data["current"]["feelslike_f"]
        humidity = data["current"]["humidity"]
        wind_mph = data["current"]["wind_mph"]

        wemoji = get_weather_emoji(condition)
        
        if country == "United States of America":
            print(f"""
---------------------------------------------------------------------
Conditions in {Fore.CYAN}{name}, {region}, {country}{Style.RESET_ALL} are:
---------------------------------------------------------------------""")
        else:
            print(f"""
---------------------------------------------------------------------
The current weather in {Fore.CYAN}{name}, {country}{Style.RESET_ALL} is:
---------------------------------------------------------------------""")
        print(f"{wemoji}{Fore.YELLOW}  Weather: {condition}")
        print(f"🌡️ {Fore.YELLOW} Temperature: {temp_f}°F (Feels like: {feelslike_f}°F)")
        print(f"💧{Fore.YELLOW} Humidity: {humidity}%")
        print(f"💨{Fore.YELLOW} Wind: {wind_mph}mph\n")

    else:
        print(f"{Fore.RED}There was an error fetching the weather.\n")

    cont = input("""
Enter Y to view new location.
Enter any key to quit.
""")

    if cont == "Y" or cont == "y":
        continue
    else:
        quitVar = True
    
#print(response.json())

