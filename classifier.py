def classify(text):
    text = text.lower()

    # Engineering
    if any(k in text for k in ["engineering", "technology", "mechanical", "electrical", "computer science"]):
        return "Engineering"

    # Management
    if any(k in text for k in ["management", "mba", "business", "finance", "marketing"]):
        return "Management"

    # Science
    if any(k in text for k in ["physics", "chemistry", "mathematics", "science", "biology"]):
        return "Science"

    # Humanities
    if any(k in text for k in ["history", "english", "literature", "language", "philosophy"]):
        return "Humanities"

    # 🌟 SOCIAL WORK (YOUR SUBJECT)
    if any(k in text for k in [
        "social work",
        "social welfare",
        "community development",
        "ngo",
        "development studies",
        "sociology",
        "human development",
        "public policy"
    ]):
        return "Social Work"

    return "General"
