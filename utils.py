from urllib.parse import unquote

def clean_domain(url):
    # Error handles if url is None or empty
    if url is None or url == "":
        return "Please input a valid domain"
    # converts decodes back into slashes
    decoded_url = unquote(url)
    # clean domain - makes it accessible for engines agents will be using
    url_lowercase = decoded_url.lower()
    url_clean = url_lowercase.replace("https://", "").replace("http://", "").replace("www.", "").replace(" ", "").replace("/", "")
    return url_clean

# Test the function
if __name__ == "__main__":
    print(clean_domain("https://www.BBC.co.uk"))
    print(clean_domain("  http://www.guardian.com  "))
    print(clean_domain(""))
    print(clean_domain(None))