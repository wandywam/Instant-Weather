# Instant Weather

Basic app built with Python that displays current weather information of any city chosen by the user. Utilizes API from [WeatherAPI.com].

# Features

- Worldwide weather data fetched from WeatherAPI
- Emoji and colorful visuals using Colorama
- Flexible location inputs (e.g. 'Los Angeles' == 'Los Angeles, CA')

# Prerequisites

1. Python 3+ installed on system
2. API key from [WeatherAPI.com] (Free!)

# Instructions

1. Clone/download this repo
2. Install necessary dependencies:

  '''bash
  pip install requests python-dotenv colorama

3. Create an .env file with your own API key:

  WEATHER_API_KEY=enter_api_key_here

4. Run the app with:

  python weather.py
   OR
  python3 weather.py
