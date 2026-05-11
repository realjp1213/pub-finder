import requests
import json
from utils import clean_domain

def fetch_whois(url):
    url_clean = clean_domain(url)
    api_key = "df7a1d181329b96hgwca36a0440b66ce4"
    print(f"Fetching WHOIS data for: {url_clean}")
    # Step 1: build the full API url using an f-string
    api_url = f"https://api.whoxy.com/?key={api_key}&whois={url_clean}"

    # Step 2: make the request and store the response
    response = requests.get(api_url)
    
    # Step 3: convert response to JSON and return it
    return response.json()

def parse_whois(data):
    # Guard clause: check if registrant_contact exists
    if "registrant_contact" not in data:
        return "No registrant contact found"
        # Pull out the three fields
    registrant = data["registrant_contact"]
    name = registrant.get("full_name", "Full name not found")
    company = registrant.get("company_name", "Company name not found")
    email = registrant.get("email_address", "Email not found")
    return {
        "name": name,
        "company": company,
        "email": email
        }

def lookup_domain(url):
    whoxy_fetch = fetch_whois(url)
    whoxy_data = parse_whois(whoxy_fetch)
    return whoxy_data


if __name__ == "__main__":
    result = lookup_domain("diariomedico.com")
    print(result)

