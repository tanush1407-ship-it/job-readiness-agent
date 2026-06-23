from database import init_db, save_search
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
    init_db()
    save_search(domain, location, jobs)
    print(f"\nFound {len(jobs)} jobs for {domain} in {location}:")
    for job in jobs:
        print(f"- {job['title']} at {job['company']['display_name']}")

    try:
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"A person is interested in {domain} in {location}. They found these jobs: {jobs}. Give them a short encouraging career roadmap and top 3 skills to learn."
    )
        print(response.text)
    except Exception as e:
    
        print(f"\nGrowthAI Career Advice:")
        print(f"Great choice exploring {domain}! Based on job listings in {location},")
        print(f"here are your top 3 next steps:")
        print(f"1. Build strong fundamentals in {domain}")
        print(f"2. Work on 2-3 portfolio projects")
        print(f"3. Apply to entry level roles and keep learning!")
     
    
start_agent()
