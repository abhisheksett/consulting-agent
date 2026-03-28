from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
import json
import os

load_dotenv()

mcp = FastMCP("consulting-research")
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@mcp.tool()
def search_industry(query: str, num_results: int = 5) -> str:
    """Search for industry trends, market analysis, and sector insights
    relevant to consulting engagements."""
    results = tavily.search(query, max_results=num_results)
    return json.dumps(results, indent=2)


@mcp.tool()
def research_company(company_name: str) -> str:
    """Research a specific company — recent news, strategy,
    financials, key challenges, and competitive position."""
    results = tavily.search(
        f"{company_name} company news strategy challenges 2026",
        max_results=5
    )
    return json.dumps(results, indent=2)


@mcp.tool()
def get_tech_trends(domain: str) -> str:
    """Get current technology and AI trends for a specific domain.
    Examples: 'AI agents', 'cloud migration', 'data platforms'."""
    results = tavily.search(
        f"{domain} enterprise technology trends adoption 2026",
        max_results=5
    )
    return json.dumps(results, indent=2)


if __name__ == "__main__":
    mcp.run()
