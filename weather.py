import requests
import os
import time

MY_LAT = "51.507351"
MY_LNG = "-0.127758"

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("API_KEY")

ENDPOINT_PARAMETERS = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "hourly, minutely, daily",
    "appid": API_KEY,
}


class Weather:

    def __init__(self):
        response = requests.get(ENDPOINT, params=ENDPOINT_PARAMETERS)
        response.raise_for_status
        current_data = response.json()['current']

        self.current_weather_code = current_data['weather'][0]['id']
        self.sunset_time = current_data['sunset']
        self.time_now = time.time()

    def is_condition_good(self):
        if self.current_weather_code == 800 and self.time_now >= self.sunset_time:
            return True
