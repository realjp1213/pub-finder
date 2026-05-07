# A fake Whoxy response stored as a Python dictionary
data = {
    "status": 1,
    "domain_name": "bbc.co.uk",
    "registrant_contact": {
        "full_name": "BBC",
        "company_name": "British Broadcasting Corporation",
        "email_address": "domains@bbc.co.uk"
    },
    "registrar": {
        "registrar_name": "Nominet UK"
    }
}

# Your challenge: print these three things
# 1. The domain name
# 2. The full name of the registrant
# 3. The email address

domain_name = data["domain_name"]
registrant_full_name = data["registrant_contact"]["full_name"]
email_address = data["registrant_contact"]["email_address"]
print(f"Domain: {domain_name}")
print(f"Name: {registrant_full_name}")
print(f"Email: {email_address}")