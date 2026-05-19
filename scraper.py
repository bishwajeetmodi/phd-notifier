import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "phd", "ph.d", "doctoral",
    "research admission",
    "phd admission",
    "fellowship",
    "doctor of philosophy"
]

def check_updates(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        text = soup.get_text().lower()

        return any(keyword in text for keyword in KEYWORDS)

    except:
        return False
