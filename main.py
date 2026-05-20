import json
import schedule
import time

from scraper import *
from notifier import send_message
from seen_manager import is_new
from classifier import classify


def load_universities():

    with open("universities.json", "r") as f:
        return json.load(f)


# KEEP ONLY THIS JOB FUNCTION
def job():

    try:

        universities = load_universities()

        updates = []
        status_lines = []

        total_updates = 0

        for uni in universities:

            name = uni["name"]
            url = uni["url"]

            found_update = False

            links, page_text = get_page_links(url)

            # WEBSITE TEXT CHECK
            if is_phd(page_text) and is_new(page_text):

                updates.append(
                    f"🎓 {name}\n"
                    f"🌐 Website PhD Update\n"
                    f"🔗 {url}"
                )

                found_update = True

            # PDF CHECK
            for link in links:

                if ".pdf" in link.lower():

                    pdf_text = read_pdf(link)

                    if pdf_text and is_phd(pdf_text):

                        if is_new(pdf_text):

                            dept = classify(pdf_text)

                            updates.append(
                                f"🎓 {name}\n"
                                f"📄 PDF PhD Notification\n"
                                f"🏛 Department: {dept}\n"
                                f"🔗 {link}"
                            )

                            found_update = True

            # STATUS SUMMARY
            if found_update:
                status_lines.append(f"✅ {name} — New Update")
                total_updates += 1
            else:
                status_lines.append(f"❌ {name} — No Update")

        # FINAL MESSAGE
        message = (
            "🎓 <b>Daily PhD University Summary</b>\n\n"
            f"✅ Universities With Updates: {total_updates}\n"
            f"❌ No Updates: {len(universities)-total_updates}\n\n"
        )

        # NEW NOTIFICATIONS
        if updates:

            message += "🆕 <b>NEW PhD Notifications</b>\n\n"

            message += "\n\n".join(updates)

        else:

            message += "🆕 No new PhD notifications today.\n\n"

        # FULL STATUS
        message += "\n\n📊 <b>University Status</b>\n\n"

        message += "\n".join(status_lines)

        send_message(message)

    except Exception as e:

        error_msg = f"❌ Bot Error:\n{str(e)}"

        print(error_msg)

        try:
            send_message(error_msg)
        except:
            pass


# TEST MESSAGE
send_message("🚀 Smart PhD Bot Started")


# DAILY SCHEDULE (9 AM IST = 03:30 UTC)
schedule.every().day.at("03:30").do(job)


# TEMPORARY TEST (REMOVE AFTER TESTING)
job()


while True:
    schedule.run_pending()
    time.sleep(30)
