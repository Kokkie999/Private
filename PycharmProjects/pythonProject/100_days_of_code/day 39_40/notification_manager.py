import json
from twilio.rest import Client

with open("C:/Users/iwand/OneDrive/api_key.json") as data_file:
    api_data = json.load(data_file)


ACCOUNT_SID = api_data['Twilio']['api_id']
AUTH_TOKEN = api_data['Twilio']['token']
VIRTUAL_NUMBER = api_data['Twilio']['phone_number']
VERIFIED_NUMBER = api_data['Twilio']['my_phone_number']

class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_NUMBER,
            to=VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
