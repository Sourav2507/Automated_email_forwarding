import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GMAIL_SCOPES

def get_gmail_service():
    creds = service_account.Credentials.from_service_account_file(
        os.getenv('GMAIL_CREDENTIALS_FILE'), scopes=GMAIL_SCOPES
    )
    service = build('gmail', 'v1', credentials=creds)
    return service

def fetch_unread_emails():
    service = get_gmail_service()
    user_id = 'me'
    response = service.users().messages().list(userId=user_id, labelIds=['UNREAD']).execute()
    messages = response.get('messages', [])
    fetched_emails = []
    for msg in messages:
        msg_detail = service.users().messages().get(userId=user_id, id=msg['id']).execute()
        subject = next((header['value'] for header in msg_detail['payload']['headers'] if header['name'] == 'Subject'), 'No Subject')
        sender = next((header['value'] for header in msg_detail['payload']['headers'] if header['name'] == 'From'), 'Unknown Sender')
        fetched_emails.append({'subject': subject, 'from': sender, 'snippet': msg_detail.get('snippet', '')})
    return fetched_emails
