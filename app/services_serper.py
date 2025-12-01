import requests
from typing import List, Dict

from .config import SERPER_API_KEY, SERPER_BASE_URL


class SerperError(Exception):
    """Custom exception for Serper-related errors."""
    pass


def search_web_with_serper(query: str, num_results: int = 5) -> Dict:
    """
    Perform a web search using Serper API.

    Returns the raw JSON from Serper, but you can later shape it.
    Raises SerperError on failure.
    """
    if not SERPER_API_KEY:
        raise SerperError("SERPER_API_KEY is not set. Please add it to your .env file.")

    url = f"{SERPER_BASE_URL}/search"

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json",
    }

    payload = {
        "q": query,
        "num": num_results,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
    except requests.RequestException as e:
        raise SerperError(f"Network error while calling Serper API: {e}")

    if response.status_code != 200:
        raise SerperError(f"Serper API returned status code {response.status_code}: {response.text}")

    data = response.json()

    # Optional: basic validation
    if "organic" not in data:
        raise SerperError("Unexpected Serper API response format: 'organic' results missing.")

    return data


def extract_simple_results(serper_response: Dict, limit: int = 5) -> List[Dict]:
    """
    Extract a simplified list of search results from Serper response.

    Each result contains: title, link, snippet.
    """
    organic = serper_response.get("organic", [])
    simplified = []

    for item in organic[:limit]:
        simplified.append(
            {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
            }
        )

    return simplified


def find_imdb_url(serper_response: Dict) -> str:
    """
    Find the first IMDb title URL from Serper organic results.
    Returns the URL as a string, or raises SerperError if none found.
    """
    organic = serper_response.get("organic", [])
    for item in organic:
        link = item.get("link", "")
        if "imdb.com/title/" in link:
            return link

    raise SerperError("No IMDb title URL found in Serper search results.")