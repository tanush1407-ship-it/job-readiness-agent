 
# GrowthAI — Your Personal Career Roadmap Agent

## The Problem

I remember the moment after finishing my Python bootcamp. I had built a 
Weather App — CLI and GUI both. It worked perfectly. But when it came to 
posting it on LinkedIn, I hesitated. "Is this too basic? Will people judge 
me? Am I even good enough to apply for jobs?"

That feeling — that paralyzing self-doubt — is something every fresher 
experiences. And it's not just about confidence. It's about not knowing:
- What skills does the market actually want RIGHT NOW?
- Which jobs can I realistically apply for at my level?
- What should I learn next to get there?

Without clear answers, talented people stay stuck. They keep learning 
randomly, applying blindly, and getting rejected without understanding why.

GrowthAI was built to solve exactly this.

## The Solution

GrowthAI is an AI-powered career guidance agent that combines real job 
market data with personalized AI advice to give freshers and career 
switchers exactly what they need — hope, direction, and a clear roadmap.

Here's what GrowthAI does in a single conversation:

1. Asks about your domain of interest
2. Asks about your target city
3. Assesses your current skill level
4. Understands what excites you about the field
5. Fetches REAL job listings from the Adzuna API
6. Uses Gemini 2.0 Flash to analyze the jobs and generate a personalized 
   career roadmap based on YOUR specific profile

The result? A fresher in Mumbai interested in Python gets told exactly 
which companies are hiring, what skills they're asking for, and what to 
learn next — in under 60 seconds.

## Why Agents?

A simple job listing website like Naukri or LinkedIn shows you jobs. 
But it doesn't THINK about you.

GrowthAI is different because it's an agent — it doesn't just retrieve 
information, it reasons about it. When GrowthAI fetches 5 Python jobs in 
Mumbai and sees that 4 of them require Django and REST APIs, it tells a 
beginner "learn these first" and tells an intermediate developer "build a 
project using these and apply!"

The same data. Different people. Completely different advice. That's what 
agents do that websites can't.

## Technical Architecture

GrowthAI is built on four core components:

### 1. Agent System (Google ADK)
The agent is built using Google's Agent Development Kit (ADK), which 
provides the framework for managing conversations, tool calls, and 
responses. The root agent is powered by Gemini 2.0 Flash.

### 2. MCP Server
A Model Context Protocol (MCP) server wraps the Adzuna job fetching 
functionality as a proper tool. This means any agent can use this tool 
to fetch Indian job listings.

### 3. Adzuna API Integration
Real job listings are fetched from Adzuna's API, which has strong coverage 
of the Indian job market. When a user says "Python jobs in Mumbai", GrowthAI 
fetches live listings from companies like TCS, ICICI Lombard, and Kotak 
Securities.

### 4. SQLite Database (Memory)
Every search is saved to a SQLite database. This gives GrowthAI persistent 
memory — it remembers what domains and locations users have searched for.

## Tech Stack

- **Language:** Python
- **AI Model:** Gemini 2.0 Flash (via Google ADK)
- **Jobs API:** Adzuna API (real Indian job listings)
- **Database:** SQLite3 (persistent memory)
- **Tools Protocol:** MCP (Model Context Protocol)
- **Agent Framework:** Google ADK

## How It Works — A Real Example


GrowthAI: Hi! I am GrowthAI. I help anyone who wants to grow

professionally — whether you're a fresher, switching careers,

or looking to upskill. Let's build your personalized career

roadmap together!
What domain are you interested in?: Python

Which city are you looking for jobs in?: Mumbai

What is your current skill level?: Beginner

What excites you most about this field?: Building apps
Found 5 jobs for Python in Mumbai:

Python Developer at DEQODE
Backend Engineer at Turing
Software Developer at TCS
Junior Python Developer at Infosys
Python Intern at Startup Hub

GrowthAI Career Advice for Beginner in Python:

Since you're just starting in Python and love building apps,

here's your personalized roadmap:

1.Learn Python fundamentals — variables, functions, loops, OOP
2.Build 2 small projects: a Todo App and a simple API
3.Learn Flask or Django to build web apps
4.Target internships and fresher roles at startups first
5.Apply to junior roles at TCS and Infosys in 3-6 months!

The market is hiring! Companies like DEQODE and Turing are

actively looking for Python developers in Mumbai. You're on

the right path — keep building!

This entire conversation happens in under 60 seconds.
GrowthAI fetches LIVE job data and gives advice specific to 
YOUR skill level and interests — not generic tips you can 
find anywhere.


## Build Journey

Building GrowthAI was a journey from zero knowledge of AI agents to a 
fully working agent in under two weeks.

Key challenges faced:

**1. Understanding Agents vs Chatbots**
The biggest mindset shift was understanding that an agent doesn't just 
respond — it perceives, plans, acts, and iterates. GrowthAI doesn't just 
answer questions. It fetches real data, analyzes it against the user's 
profile, and gives actionable advice. Every conversation is different.

**2. MCP Server Integration**
Building the MCP server to expose the Adzuna tool was challenging but 
rewarding. It meant GrowthAI's job-fetching capability could be used by 
any other agent in the future — making it truly modular.

**3. Context Engineering**
The quality of Gemini's advice depended entirely on how well the prompt 
was structured. Including domain, location, skill level, interests AND 
actual job listings gave Gemini the context it needed for truly 
personalized advice. This was the key insight — better context = 
better advice.

**4. Handling Quota Limits**
Free tier API limits required building a smart fallback system. When 
Gemini is unavailable, GrowthAI still gives skill-level specific advice 
based on rule-based logic — ensuring the user always gets value regardless 
of API availability.

**5. Database Memory**
Adding SQLite persistence meant GrowthAI remembers every search. This 
enables future features like "you searched Python last week — here's 
what's changed in the market!"

## Agent Architecture Diagram

User Input

↓

GrowthAI Agent (Google ADK)

↓

Ask Questions (domain, location, skill level, interests)

↓

fetch_jobs Tool (via MCP Server)

↓

Adzuna API → Real Job Listings

↓

Gemini 2.0 Flash Analysis

↓

Personalized Career Roadmap

↓

SQLite Database (save for memory)

↓

User Gets: Jobs + Roadmap + Hope


## Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| Agent System (ADK) | Google ADK root_agent with Gemini 2.0 Flash |
| MCP Server | FastMCP server exposing fetch_jobs tool |
| Database/Memory | SQLite3 saving all user searches |
| Context Engineering | Rich prompts with user profile + job data |
| Fallback System | Skill-level specific advice when AI unavailable |

## What Makes GrowthAI Special

Most career tools tell you what jobs exist. GrowthAI tells you:
- Which jobs YOU can apply for RIGHT NOW based on your level
- What YOU specifically need to learn to get the ones you can't
- How YOUR interests connect to real market opportunities
- A step by step roadmap tailored to YOU

It's not just a job search tool. It's a career counselor that never 
sleeps, never judges, and always gives honest, data-driven advice.

## Impact

GrowthAI targets the 15 million+ freshers who enter India's job market 
every year feeling lost and underconfident. By combining real job market 
data with personalized AI guidance, GrowthAI gives every fresher the same 
advantage that previously only came from expensive career counselors or 
well-connected networks.

The three questions every fresher asks — "Am I good enough?", "What 
should I learn?", "Which jobs can I apply for?" — GrowthAI answers all 
three in under 60 seconds.

## Conclusion

GrowthAI started as a personal frustration — not knowing if a bootcamp 
project was good enough to share. It became something much bigger — a 
tool that gives hope and direction to anyone feeling stuck in their 
career journey.

Generation is solved. Verification, judgment, and direction are the 
new craft. GrowthAI embodies exactly that.

## GitHub Repository
https://github.com/tanush1407-ship-it/job-readiness-agent

