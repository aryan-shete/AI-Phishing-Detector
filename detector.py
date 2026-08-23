import re

keywords = [
    "urgent",
    "verify",
    "click here",
    "update payment",
    "bank",
    "winner",
    "password",
    "account suspended",
    "limited time",
    "confirm"
]

def detect(email):
    score = 0
    reasons = []

    email = email.lower()

    for word in keywords:
        if word in email:
            score += 10
            reasons.append(f'Keyword detected: "{word}"')

    # Find URLs
    urls = re.findall(r'https?://\S+', email)

    suspicious_domains = [
        "bit.ly",
        "tinyurl",
        ".ru",
        ".xyz"
    ]

    for url in urls:
        for domain in suspicious_domains:
            if domain in url:
                score += 20
                reasons.append(f"Suspicious URL: {url}")

    if score > 100:
        score = 100

    return score, reasons