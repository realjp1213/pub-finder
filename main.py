from fastapi import FastAPI
from whois_agent import lookup_domain

# Create the FastAPI app
app = FastAPI()

# Define your first endpoint
@app.post("/lookup")
def lookup(domain: str):
    # Call lookup_domain and return the result
    whoxy_result = lookup_domain(domain)
    return whoxy_result