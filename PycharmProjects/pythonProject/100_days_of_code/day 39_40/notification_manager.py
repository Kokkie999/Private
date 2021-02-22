import json
from twilio.rest import Client

with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
    api_data = json.load(data_file)


ACCOUNT_SID = api_data['Twilio']['api_id']
AUTH_TOKEN = api_data['Twilio']['token']


class NotificationManager:

    TWILIO_SID = YOUR
    TWILIO
    ACCOUNT
    SID
    TWILIO_AUTH_TOKEN = YOUR
    TWILIO
    AUTH
    TOKEN
    TWILIO_VIRTUAL_NUMBER = YOUR
    TWILIO
    VIRTUAL
    NUMBER
    TWILIO_VERIFIED_NUMBER = YOUR
    TWILIO
    VERIFIED
    NUMBER