from utils import clean_domain

def fetch_whois(url):
    url_clean = clean_domain(url)
    print(f"Fetching WHOIS data for: {url_clean}")


# Testing fetch whois function
if __name__ == "__main__":
    fetch_whois("https://www.BBC.co.uk")