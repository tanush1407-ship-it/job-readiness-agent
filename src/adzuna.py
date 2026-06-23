import requests
import os
from dotenv import load_dotenv

load_dotenv()

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY")

def fetch_jobs(domain, location):    
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_API_KEY,
        "what": domain,
        "where": location,
        "results_per_page": 5
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])