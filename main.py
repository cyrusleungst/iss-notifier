import os
from twilio.rest import Client
from weather import Weather
from iss import ISS

ACCOUNT_SID = "AC5019c909f02cb6ff6b848fde1363fce4"
AUTH_TOKEN = os.environ.get("auth_token")

# checks if the weather is clear so we can get a good view of the ISS
weather = Weather()
iss = ISS()
client = Client(ACCOUNT_SID, AUTH_TOKEN)

if weather.is_condition_good() and iss.is_iss_overhead():
    body_text = "Look up, the ISS is close by!"
else:
    body_text = f"ISS is {iss.calculate_distance()} kilometers away"

message = client.messages \
        .create(
            body=body_text,
            from_='+12058583328',
            to='+447756240526'
        )

print(message.status)
