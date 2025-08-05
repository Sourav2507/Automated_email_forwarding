import os
from twilio.rest import Client
from config import TWILIO_FROM, TWILIO_TO

def send_whatsapp_message(body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=body,
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )
    return message.sid
