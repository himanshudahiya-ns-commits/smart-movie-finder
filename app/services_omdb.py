import requests
from typing import Optional

from .config import OMDB_API_KEY, OMDB_BASE_URL


class OmdbError(Exception):
    """Custom exception for OMDb-related errors."""
    pass


def fetch_movie_from_omdb(title: str, year: Optional[int] = None) -> dict:
    """
    Fetch movie details from OMDb API by title (and optional year).

    Raises OmdbError on failure.
    """
    if not OMDB_API_KEY:
        raise OmdbError("OMDB_API_KEY is not set. Please add it to your .env file.")

    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
        "plot": "full",
    }

    if year:
        params["y"] = str(year)

    try:
        response = requests.get(OMDB_BASE_URL, params=params, timeout=10)
    except requests.RequestException as e:
        # Network issues, DNS, timeout, etc.
        raise OmdbError(f"Network error while calling OMDb: {e}")

    if response.status_code != 200:
        raise OmdbError(f"OMDb returned status code {response.status_code}")

    data = response.json()

    # OMDb uses "Response": "False" for not found / errors
    if data.get("Response") == "False":
        error_message = data.get("Error", "Unknown error from OMDb")
        raise OmdbError(f"OMDb error: {error_message}")

    return data
