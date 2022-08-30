import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



API_KEY = os.environ.get("KEY")
account_sid = os.environ.get("SID")
auth_token = os.environ.get("TOKEN")
lat = 12.901319
lon = 80.197859

API = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
prediction = []
data = requests.get(API).json()
for i in range(8):
    prediction.append(data['list'][i]['weather'][0]['id'])

for i in prediction:
    if i < 700:
        proxy = TwilioHttpClient()
        proxy.session.proxies = {'https': os.environ['http_proxy']}
        client = Client(account_sid, auth_token,http_client=proxy)
        message = client.messages.create(body='Bring an Umbrella☔☂. It\'s going to rain🌧', from_='+15139352451', to='+917904692237')
        print(message.status)
        break



