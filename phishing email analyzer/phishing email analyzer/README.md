# Phishing Email Analyzer

A beginner-friendly Python project that analyzes emails or messages to identify potential phishing attempts. It detects common phishing indicators such as suspicious keywords, malicious links, shortened URLs, and urgent language, then provides a risk assessment.

## Features

- Detects suspicious phishing keywords
- Identifies website links in messages
- Detects shortened URLs (e.g., bit.ly, tinyurl)
- Flags urgent or threatening language
- Calculates a phishing risk score
- Classifies messages as:
  - Appears Safe
  - Suspicious
  - Likely Phishing

## Technologies Used

- Python 3

## Project Structure

```
phishing-analyzer/
├── phishing_analyzer.py
└── README.md
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-projects.git
   ```

2. Navigate to the project folder:
   ```bash
   cd python-projects/phishing-analyzer
   ```

3. Run the program:
   ```bash
   python phishing_analyzer.py
   ```

## Example Input

```
URGENT!

Your bank account has been locked.

Click here:
https://bit.ly/secure-login

Verify your password within 24 hours.
```

## Example Output

```
Analysis Report
------------------------------
Red Flags Found:
- urgent
- verify
- password
- click here
- Link detected
- Shortened URL

Risk Score: 15

Verdict: Likely Phishing
```

## Skills Demonstrated

- Python Programming
- String Handling
- Conditional Statements
- Threat Analysis
- Phishing Detection
- Cybersecurity Awareness
- Basic Risk Assessment

## Learning Objectives

This project was created to practice Python while learning how phishing attacks work. It demonstrates how simple pattern matching can be used to identify common phishing indicators and improve cybersecurity awareness.

## Author

**Vaneeza Nadeem**

Cybersecurity Student | Python Learner | Aspiring Cybersecurity Analyst
