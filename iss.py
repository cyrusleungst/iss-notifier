import requests
import os
from math import cos, asin, sqrt, pi

MY_LAT = 51.507351
MY_LNG = -0.127758

ACCOUNT_SID = "AC5019c909f02cb6ff6b848fde1363fce4"
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ENDPOINT = "http://api.open-notify.org/iss-now.json"


class ISS:

    def __init__(self):
        response = requests.get(ENDPOINT)
        response.raise_for_status()
        data = response.json()

        self.iss_latitude = float(data['iss_position']['latitude'])
        self.iss_longitude = float(data['iss_position']['longitude'])

    def is_iss_overhead(self):
        if MY_LAT-5 <= self.iss_latitude <= MY_LAT+5 and MY_LNG-5 <= self.iss_longitude <= MY_LNG+5:
            return True

    def calculate_distance(self):
        p = pi/180
        a = 0.5 - cos((MY_LAT-self.iss_latitude)*p)/2 + cos(self.iss_latitude*p) * \
            cos(MY_LAT*p) * (1-cos((MY_LNG-self.iss_longitude)*p))/2

        return 12742 * asin(sqrt(a))
