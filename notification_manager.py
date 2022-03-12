import os
from twilio.rest import Client
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
messaging_service_sid = os.getenv("MESSAGING_SID")
RECEIVING_NUMBER = os.getenv('RECEIVING_NUMBER')


class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        self.message = ""

    def message_sender(self, message):
        self.message = self.client.messages \
                        .create(
                             body=message,
                             from_=messaging_service_sid,
                             to=RECEIVING_NUMBER
                         )

        print(self.message.status)