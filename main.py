import json
import schedule
import time
from datetime import datetime

from scraper import check_updates
from notifier import send_message

def load_universities():
    with open("universities.json", "r") as f:
        return json.load(f)

def run_job():

    universities = load_universities()
    results = []

    for uni in universities:
        name = uni["name"]
        url = uni["url"]

        if check_updates(url):
            results.append(f"🎓 {name}\n🔗 {url}")

    today = datetime.now().strftime("%d %b %Y")

    if results:
        message = f"🎓 <b>PhD Daily Summary - {today}</b>\n\n"
        message += "\n\n".join(results)
    else:
        message = f"🎓 <b>PhD Daily Summary - {today}</b>\n\nNo new updates found."

    send_message(message)


def start_bot():
    send_message("🚀 PhD Bot Started Successfully")

# schedule 9 AM daily
schedule.every().day.at("03:30").do(run_job)

start_bot()

while True:
    schedule.run_pending()
    time.sleep(30)
