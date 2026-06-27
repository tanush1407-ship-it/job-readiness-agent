# GrowthAI - Career Guidance Agent
# Uses Gemini AI + Adzuna API to give personalized career roadmaps




from database import init_db, save_search # Database for persistent memory
import requests
from google import genai
from dotenv import load_dotenv
from adzuna import fetch_jobs # Tool for fetching real job listings
import os

load_dotenv() # Load API keys from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Never hardcode API keys!
client = genai.Client(api_key=GEMINI_API_KEY)

def start_agent():
    # Welcome message - establishes GrowthAI's identity
    print("Hi! I am GrowthAI. I help anyone who wants to grow professionally — whether you're a fresher, switching careers, or looking to upskill. Let's build your personalized career roadmap together!")
    # Collect user profile for personalization
    domain = input("What domain are you interested in? (e.g. Python, Web Development, Data Science): ")
    location = input("Which city are you looking for jobs in? (e.g. Mumbai, Bangalore, Delhi): ")
    skill_level = input("What is your current skill level? (Beginner/Intermediate/Advanced): ")
    interests = input("What excites you most about this field?: ")

    # Normalize skill level input - handles typos and abbreviations.

    if not interests:
        interests = "general growth and learning"
    if "beg" in skill_level.lower():
        skill_level = "Beginner"
    elif "inter" in skill_level.lower():
        skill_level = "Intermediate"
    elif "adv" in skill_level.lower():
        skill_level = "Advanced"

    # Fetch REAL job listings using Adzuna API tool  
    jobs = fetch_jobs(domain, location)


    # Save search to SQLite database for persistent memory
    init_db()
    save_search(domain, location, jobs)
    # Display job listings 
    print(f"\nFound {len(jobs)} jobs for {domain} in {location}:") 
    for job in jobs:
        print(f"- {job['title']} at {job['company']['display_name']}")

    try:
        # Use Gemini to generate personalized career roadmap
        # Context engineering: include domain, location, skill level, 
        # interests AND actual job listings for maximum personalization


        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"A person is interested in {domain} in {location}. Their skill level is {skill_level}. What excites them: {interests}. Jobs found: {jobs}. Based on their skill level, give them a personalized career roadmap and top 3 skills to learn. If beginner, focus on learning fundamentals first. If intermediate, focus on portfolio projects. If advanced, focus on senior roles."
        )
        print(response.text)

    except Exception as e:
            
            # Fallback advice when Gemini quota is exceeded
            # Ensures agent always provides value regardless of API availability
            print(f"\nGrowthAI Career Advice for {skill_level} in {domain}:")

            
            
    if skill_level == "Beginner":
                print(f"Since you're just starting in {domain}, here's your roadmap:")
                print(f"1. Learn the fundamentals of {domain} through free resources")
                print(f"2. Build 1-2 small projects to practice")
                print(f"3. Focus on {interests} to stay motivated")
                print(f"4. Don't apply for jobs yet — build skills first!")
                
    elif skill_level == "Intermediate":
                print(f"You're making good progress in {domain}!")
                print(f"1. Build 2-3 strong portfolio projects")
                print(f"2. Contribute to open source")
                print(f"3. Start applying to junior roles")
                print(f"4. Focus on {interests} to specialize!")
                
    else:
                print(f"You're advanced in {domain} — time to level up!")
                print(f"1. Apply for senior/mid-level roles")
                print(f"2. Mentor others and build your network")
                print(f"3. Specialize deeper in {interests}")
        
    
start_agent()
