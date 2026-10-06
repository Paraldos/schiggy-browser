import requests

def load_page(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    response = requests.get(url)
    print(response.text)
