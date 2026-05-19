import os
import schedule
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })


# TEST MESSAGE ON START
send_message("🚀 PhD Bot is LIVE on Railway!")


def run_job():
    send_message("🎓 Daily PhD Summary Triggered")


# 9 AM IST = 03:30 UTC
schedule.every().day.at("03:30").do(run_job)


print("Bot running...")

while True:
    schedule.run_pending()
    time.sleep(30)
