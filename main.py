import requests
import os
from twilio.rest import Client
from weather import Weather
from iss import ISS

# checks if the weather is clear so we can get a good view of the ISS
weather = Weather()
iss = ISS()

print(weather.is_condition_good())
print(iss.is_iss_overhead())
print(iss.calculate_distance())
