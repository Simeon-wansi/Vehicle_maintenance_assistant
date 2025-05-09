import requests
import os
from langchain_core.tools import tool
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Known aliases for common UAE cities
CITY_ALIASES = {
    "abudhabi": "Abu Dhabi",
    "abudhabi.": "Abu Dhabi",
    "dubai": "Dubai",
    "sharjah": "Sharjah"
}

@tool
def get_current_weather(city: str) -> str:
    """Returns the current weather for a given city using OpenWeatherMap."""
    city_cleaned = city.strip().lower()
    city_normalized = CITY_ALIASES.get(city_cleaned, city)  # Replace alias if matched

    city_encoded = quote_plus(city_normalized)
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city_encoded}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return (
            f"I'm sorry, I couldn't find the weather information for \"{city}\". "
            "Could you please check the spelling or try a different city?"
        )

    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"The current temperature in {city_normalized} is {temp}°C with {desc}, "
        f"and humidity is {humidity}%."
    )










# import requests
# import os
# from langchain_core.tools import tool
# from dotenv import load_dotenv
# from urllib.parse import quote_plus

# load_dotenv()
# OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# @tool
# def get_current_weather(city: str) -> str:
#     """Returns the current weather for a given city using OpenWeatherMap."""
#     city_encoded = quote_plus(city)
#     url = (
#         f"http://api.openweathermap.org/data/2.5/weather?"
#         f"q={city_encoded}&appid={OPENWEATHER_API_KEY}&units=metric"
#     )

#     response = requests.get(url)
#     # if response.status_code != 200:
#     #     return f"I'm sorry, but I was unable to fetch the current weather for {city}. Please make sure the city name is spelled correctly."
#     # if response.status_code != 200:
#     #     return f"[DEBUG] Status: {response.status_code}, Message: {response.text}"
#     if response.status_code != 200:
#         return (
#             f"[DEBUG] Failed to fetch weather.\n"
#             f"Status Code: {response.status_code}\n"
#             f"Response: {response.text}\n"
#             f"City: {city}"
#         )


#     data = response.json()
#     temp = data["main"]["temp"]
#     desc = data["weather"][0]["description"]
#     humidity = data["main"]["humidity"]

#     return f"The current temperature in {city} is {temp}°C with {desc}, and humidity is {humidity}%."
