from langsmith import traceable
from tavily import TavilyClient

from app.config import TAVILY_API_KEY

@traceable(name="web_search", run_type="tool")
def search_web(query : str) -> str:
    if not TAVILY_API_KEY:
        return "Tavily API key is not configured."

    client = TavilyClient(api_key=TAVILY_API_KEY)
    result = client.search(query=query, max_results=3)
    results = result.get("results",[])
    if not results:
        return "No web results found."

    output = []

    for item in results:
        title = item.get("title","")
        content = item.get("content","")
        url = item.get("url","")

        output.append(
            f"Title : {title} \n Content : {content} \n URL : {url} \n"
        )
        return  "\n".join(output)