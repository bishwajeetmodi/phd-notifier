import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "phd", "ph.d", "doctoral",
    "research admission",
    "phd admission",
    "fellowship",
    "doctor of philosophy", 
    "2026", 
    "PhD Admission", 
    "doctral programme", 
    "2026-2027",
    "UGC–JRF",
    "PhD Admissions 2025-26",
    "Ph.D. July, 2026 Session",
    "Ph.D Admission Notification"
]

def check_updates(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text().lower()

        return any(keyword in text for keyword in KEYWORDS)

    except:
        return False
