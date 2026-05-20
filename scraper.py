import requests
from bs4 import BeautifulSoup
import hashlib

from pdfminer.high_level import extract_text


KEYWORDS = ["phd", "ph.d", "doctoral", "research", "phd admission", "fellowship", "doctor of philosophy", 
    "2026", "PhD Admission", "doctral programme", "2026-2027","UGC–JRF","PhD Admissions 2025-26", "Ph.D. July, 2026 Session",
    "Ph.D Admission Notification"]

def is_phd(text):
    text = text.lower()
    return any(k in text for k in KEYWORDS)


def get_page_links(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        links = []
        for a in soup.find_all("a", href=True):
            links.append(a["href"])

        return links, soup.get_text()

    except:
        return [], ""


def read_pdf(url):
    try:
        import requests
        import os
        from pdfminer.high_level import extract_text

        r = requests.get(url, timeout=15)

        if r.status_code != 200:
            return ""

        filename = "temp.pdf"

        with open(filename, "wb") as f:
            f.write(r.content)

        try:
            text = extract_text(filename)

            if text:
                return text.lower()

            return ""

        except Exception as pdf_error:
            print(f"PDF Parse Error: {pdf_error}")
            return ""

        finally:
            if os.path.exists(filename):
                os.remove(filename)

    except Exception as e:
        print(f"PDF Download Error: {e}")
        return ""
