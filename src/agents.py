import requests
from google import genai
from dotenv import load_dotenv
from adzuna import fetch_jobs
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def start_agent():
    
    print("Hi! I am GrowthAI. I help anyone who wants to grow professionally — whether you're a fresher, switching careers, or looking to upskill. Let's build your personalized career roadmap together!")
    
    domain = input("What domain are you interested in? (e.g. Python, Web Development, Data Science): ")
    location = input("Which city are you looking for jobs in? (e.g. Mumbai, Bangalore, Delhi): ")
    jobs = fetch_jobs(domain, location)
    print(f"\nFound {len(jobs)} jobs for {domain} in {location}:")
    for job in jobs:
        print(f"- {job['title']} at {job['company']['display_name']}")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"A person is interested in {domain}..."
    )   
    print(response.text)

start_agent()
