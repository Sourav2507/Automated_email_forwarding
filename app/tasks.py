from apscheduler.schedulers.background import BackgroundScheduler
from app.gmail_service import fetch_unread_emails
from app.whatsapp_service import send_whatsapp_message

def poll_and_notify():
    emails = fetch_unread_emails()
    for email in emails:
        msg = f"New Email from {email['from']}:\nSubject: {email['subject']}\nSnippet: {email['snippet']}"
        send_whatsapp_message(msg)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(poll_and_notify, 'interval', minutes=15)
    scheduler.start()
