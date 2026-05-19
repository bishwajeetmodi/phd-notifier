import json
import schedule
import time

from scraper import get_page_links, read_pdf, is_phd
from notifier import send_message
from seen_manager import is_new
from classifier import classify


def load_universities():
    with open("universities.json", "r") as f:
        return json.load(f)


def job():

    universities = load_universities()

    updates = []

    for uni in universities:

        name = uni["name"]
        url = uni["url"]

        links, page_text = get_page_links(url)

        # check page itself
        if is_phd(page_text) and is_new(page_text):
            updates.append(f"{name} (Website Update)\n{url}")

        # check PDFs
        for link in links:
            if ".pdf" in link:

                pdf_text = read_pdf(link)

                if is_phd(pdf_text) and is_new(pdf_text):

                    dept = classify(pdf_text)

                    updates.append(
                        f"🎓 {name}\n"
                        f"📄 PDF PhD Notification\n"
                        f"🏛 Department: {dept}\n"
                        f"🔗 {link}"
                    )

    # FINAL SUMMARY
    if updates:
        message = "🎓 <b>AI PhD Daily Digest</b>\n\n"
        message += "\n\n".join(updates)
    else:
        message = "🎓 No new PhD updates today."

    send_message(message)


schedule.every().day.at("03:30").do(job)

send_message("🚀 Smart PhD Bot v2 Started")

while True:
    schedule.run_pending()
    time.sleep(30)
