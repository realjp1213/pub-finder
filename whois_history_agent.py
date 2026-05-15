import requests
import json
from utils import clean_domain


def fetch_whois_history(url):
    url_clean = clean_domain(url)
    api_key = "df7a1d181329b96hgwca36a0440b66ce4"
    print(f"Fetching WHOIS history data for: {url_clean}")

    api_url = f"https://api.whoxy.com/?key={api_key}&history={url_clean}"
    response = requests.get(api_url)
    
    return response.json()


def parse_history(data):
    privacy_words = ["redacted", "privacy", "proxy", "whoisguard"]
    records = data.get("whois_records", [])
    clean_records = []
    
    for record in records:
        registrant = record.get("registrant_contact", {})
        name = registrant.get("full_name", "")
        email = registrant.get("email_address", "")
        company = registrant.get("company_name", "")
        country = registrant.get("country_name", "")
        city = registrant.get("city_name", "")
        address = registrant.get("mailing_address", "")
        # Combine the fields you want to check
        fields_to_check = [name, email, company, address]
        # Check if name or email contains any privacy word
        # Hint: you need to loop through privacy_words and check
        # if any of them appear in name.lower() or email.lower()
        is_private = False
        for word in privacy_words:
            for field in fields_to_check:
                if word.lower() in field.lower():
                    is_private = True
        if not is_private:
            clean_records.append({
                "name": name,
                "company": company,
                "email": email,
                "country": country,
                "city": city,
                "address": address,
                "create_date": record.get("create_date", "")
            })
    
    return clean_records

if __name__ == "__main__":
    data = fetch_whois_history("https://www.publicdomainpictures.net/")
    result = parse_history(data)
    print(result)


