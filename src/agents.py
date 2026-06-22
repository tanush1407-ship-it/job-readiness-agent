import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


model= genai.GenerativeModel("gemini-2.0-flash")

def start_agent():
    print("Hi! I am GrowthAI. I help anyone who wants to grow professionally — whether you're a fresher, switching careers, or looking to upskill. Let's build your personalized career roadmap together!")
    
    domain = input("What domain are you interested in? (e.g. Python, Web Development, Data Science): ")
    
    response = model.generate_content(f"A person is interested in {domain}. Ask them one question to assess their current knowledge level in a friendly, encouraging way.")
    
    print(response.text)

start_agent()