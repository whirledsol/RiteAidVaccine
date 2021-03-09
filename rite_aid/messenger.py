import os
import json
from twilio.rest import Client


class Messenger:
    def __init__(
        self,
        twilio_sid: str = os.getenv("TWILIO_ACCOUNT_SID"),
        twilio_auth: str = os.getenv("TWILIO_AUTH_TOKEN"),
        recipient: str = os.getenv("RECIPIENT"),
        sender: str = os.getenv("SENDER"),
    ):
        self.client = Client(twilio_sid, twilio_auth)
        self.recipient = recipient
        self.sender = sender
        
   
    def notify_availability(self, store_info):
        self.client.api.account.messages.create(
            to=self.recipient,
            from_=self.sender,
            body="Availability at #{store_info}.".format(store_info=store_info)
        )
