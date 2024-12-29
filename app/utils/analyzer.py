import requests
from app.config.settings import API_KEY


def analyze_url(url: str):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    body = {
        "client": {
            "clientId": "mobil-ag-analizi",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }
    response = requests.post(api_url, json=body)

    # Yanıtı işleyin
    if response.status_code == 200 and "matches" in response.json():
        return {"url": url, "status": "Malicious"}
    return {"url": url, "status": "Safe"}
