import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
TWILIO_FROM = os.getenv('TWILIO_WHATSAPP_FROM')  # e.g., 'whatsapp:+14155238886'
TWILIO_TO = os.getenv('TWILIO_WHATSAPP_TO')      # e.g., 'whatsapp:+919999999999'
