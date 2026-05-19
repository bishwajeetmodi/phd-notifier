import json
import hashlib

FILE = "seen.json"


def make_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


def load_seen():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_seen(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def is_new(text):
    seen = load_seen()
    h = make_hash(text)

    if h in seen:
        return False

    seen.append(h)
    save_seen(seen)
    return True
