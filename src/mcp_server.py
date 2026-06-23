from mcp.server.fastmcp import FastMCP
from adzuna import fetch_jobs

mcp = FastMCP("GrowthAI Jobs Server")

@mcp.tool()
def get_jobs(domain: str, location: str) -> str:
    jobs = fetch_jobs(domain, location)
    if not jobs:
        return "No jobs found"
    
    result = f"Found {len(jobs)} jobs for {domain} in {location}:\n"
    for job in jobs:
        result += f"- {job['title']} at {job['company']['display_name']}\n"
    return result

if __name__ == "__main__":
    mcp.run()