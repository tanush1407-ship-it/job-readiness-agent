 # GrowthAI 🚀
An AI-powered Job Readiness Agent that helps anyone grow professionally — 
by finding real job listings, analyzing market trends, and providing 
personalized career roadmaps based on your domain and location.

## The Problem
Every fresher or career switcher faces the same questions:
- "Am I skilled enough to apply?"
- "What should I learn next?"
- "Which jobs are actually hiring in my city?"

Without clear answers, talented people stay stuck. GrowthAI 
gives them hope, direction, and real market data to move forward.


## Solution
GrowthAI is an AI agent that:
1. Asks about your domain of interest and location
2. Fetches REAL job listings from Adzuna API
3. Analyzes what skills companies are demanding RIGHT NOW
4. Uses Gemini AI to generate a personalized career roadmap
5. Saves your search history for future reference



## Tech Stack
- **Language:** Python
- **AI Model:** Gemini 2.0 Flash
- **Jobs API:** Adzuna API
- **Database:** SQLite
- **Tools Protocol:** MCP (Model Context Protocol)


## How to Run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Add your API keys to `.env` file:
GEMINI_API_KEY=your_key
ADZUNA_APP_ID=your_id
ADZUNA_API_KEY=your_key
4. Run the agent: `cd src && python agents.py`

## Project Structure
job_readiness_agent/
├── src/
│   ├── agents.py      # Main agent
│   ├── adzuna.py      # Job listings fetcher
│   ├── database.py    # User memory
│   └── mcp_server.py  # MCP tools server
├── database/          # SQLite storage
├── .env               # API keys (not shared)
└── requirements.txt   # Dependencies