import os
import json
from twilio.rest import Client


class Messenger:
    def __init__(
        self,
        twilio_sid: str = os.environ["TWILIO_ACCOUNT_SID"],
        twilio_auth: str = os.environ["TWILIO_AUTH_TOKEN"],
        recipient: str = os.environ["RECIPIENT"],
        sender: str = os.environ["SENDER"],
    ):
        self.client = Client(twilio_sid, twilio_auth)
        self.recipient = recipient
        self.sender = sender
        self.store_details = self.load_store_info()
        
    def load_store_info(self, path:str='store_details.json'):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, path)
        with open(file_path, 'r') as store_info:
            return json.load(store_info)

    def notify_availability(self, store_num: int):
        self.client.api.account.messages.create(
            to=self.recipient,
            from_=self.sender,
            body="Availability at #{store_number}. {address}".format(
                store_number=store_num, address=self.store_details[str(store_num)]['address']
            ),
        )
