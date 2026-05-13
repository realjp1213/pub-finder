from fastapi import FastAPI
from whois_agent import lookup_domain
from database import get_result, save_result, init_db

# Create the FastAPI app
app = FastAPI()
init_db()

# Define your first endpoint
@app.post("/lookup")
def lookup(domain: str):
    # Step 1: check the database first
    cached = get_result(domain)
    if cached:
        return cached
    
    # Step 2: not in cache - call Whoxy
    result = lookup_domain(domain)

    # Step 3: save to database if we got real data
    if isinstance(result, dict):
        save_result(domain, result)
    return result