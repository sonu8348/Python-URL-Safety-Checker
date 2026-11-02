# Phishing URL Awareness Checker

A simple Python program that checks URLs for common phishing warning signs.

## Features
- Detects `@` symbols in URLs.
- Flags URLs longer than 100 characters.
- Checks for IP-address hostnames.
- Detects multiple subdomains.
- Checks for punycode markers (`xn--`).
- Warns about HTTP connections.

## Requirements
- Python 3.10+
- No external libraries required.

## How to Run

```bash
python phishing_checker.py
```

Enter a URL to check it. Type `q` to exit.

