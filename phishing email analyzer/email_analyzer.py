email = input("Paste the email/message:\n").lower()

score = 0
red_flags = []

# High-risk keywords
high_risk = [
    "password",
    "verify",
    "urgent",
    "click here",
    "immediately",
    "bank account",
    "within 24 hours"
]

# Medium-risk keywords
medium_risk = [
    "login",
    "confirm",
    "security alert",
    "update your account",
    "gift",
    "winner",
    "free"
]

for word in high_risk:
    if word in email:
        score += 2
        red_flags.append(word)

for word in medium_risk:
    if word in email:
        score += 1
        red_flags.append(word)

# Links
if "http://" in email or "https://" in email:
    score += 2
    red_flags.append("Link detected")

# Shortened URLs
if "bit.ly" in email or "tinyurl.com" in email:
    score += 3
    red_flags.append("Shortened URL")

print("\nAnalysis Report:")

if red_flags:
    print("Red Flags Found:")
    for flag in red_flags:
        print("", flag)
else:
    print("No red flags found.")

print("\nRisk Score:", score)

if score >= 6:
    print("Verdict: Likely Phishing")
elif score >= 3:
    print("Verdict: Suspicious")
else:
    print("Verdict: Appears Safe")