from app import create_app
from app.tasks import start_scheduler

app = create_app()

@app.route('/')
def health():
    return 'Gmail to WhatsApp notifier is running!', 200

if __name__ == '__main__':
    start_scheduler()
    app.run(host='0.0.0.0', port=5000)
