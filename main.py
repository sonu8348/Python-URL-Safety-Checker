
from urllib.parse import urlparse
import re


def check_url(url):
    url = url.strip()

    if not url:
        print("Please enter a URL.")
        return

    if "://" not in url:
        url = "https://" + url

    try:
        parsed = urlparse(url)
        host = parsed.hostname
    except ValueError:
        print("Invalid URL.")
        return

    if not host:
        print("Invalid URL: hostname missing.")
        return

    warnings = []

    # Check connection scheme
    if parsed.scheme != "https":
        warnings.append("Connection is not HTTPS")

    # Check for username or @ symbol
    if "@" in parsed.netloc:
        warnings.append("Contains an @ symbol")

    # Check URL length
    if len(url) > 100:
        warnings.append("URL is unusually long")

    # Check IP address hostname
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", host):
        warnings.append("Uses an IP address as hostname")

    # Check number of domain sections
    if len(host.split(".")) >= 5:
        warnings.append("Contains many subdomains")

    # Check punycode
    if "xn--" in host:
        warnings.append("Contains a punycode hostname")

    if warnings:
        print("\n⚠️ Review this URL:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo warning signs detected.")


while True:
    url = input("\nEnter URL (q to quit): ")

    if url.lower().strip() == "q":
        print("Goodbye!")
        break

    check_url(url)
