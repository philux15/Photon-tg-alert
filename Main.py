import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USER_ID = os.getenv("TELEGRAM_USER_ID")

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": USER_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

# Sample test alert
sample_alert = "<b>New Token Detected!</b>\nName: $COIN\nLP: 2k+\nMC: $10k+\nAge: 15 mins\nVolume: $5k+"
send_alert(sample_alert)
