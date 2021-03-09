import os
import json
from twilio.rest import Client
from dotenv import load_dotenv,find_dotenv

class Messenger:
    def __init__(
        self,
        twilio_sid: str = None,
        twilio_auth: str= None,
        recipient: str= None,
        sender: str= None
    ):
        load_dotenv(find_dotenv(),verbose=True)
        
        twilio_sid = twilio_sid or os.getenv("TWILIO_ACCOUNT_SID")
        twilio_auth = twilio_auth or os.getenv("TWILIO_AUTH_TOKEN")
        recipient = recipient or os.getenv("RECIPIENT")
        sender = sender or os.getenv("SENDER")

        self.client = Client(twilio_sid, twilio_auth)
        self.recipient = recipient
        self.sender = sender
        

   
    def notify_availability(self, store_info):
        print(f"sending to {self.sender}")
        self.client.api.account.messages.create(
            to=self.recipient,
            from_=self.sender,
            body=f"COVID Vaccine Available at Rite Aid {store_info}."
        )
