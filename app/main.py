from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from .services_omdb import fetch_movie_from_omdb, OmdbError
from .services_serper import search_web_with_serper, SerperError, extract_simple_results , find_imdb_url
from .services_imdb import scrape_imdb_movie_page, ImdbScraperError


app = FastAPI(
    title="Movzie",
    description="Backend-only API that uses OMDb, Serper, and web scraping to fetch movie info.",
    version="0.1.0",
)

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Smart Movie Finder API is running"}


@app.get("/movies/omdb")
def get_movie_from_omdb(
    title: str = Query(..., description="Movie title to search in OMDb"),
    year: Optional[int] = Query(None, description="Optional release year for disambiguation"),
):
    """
    Fetch movie details from OMDb by title (and optional year).

    Example:
    /movies/omdb?title=Inception&year=2010
    """
    try:
        movie_data = fetch_movie_from_omdb(title=title, year=year)
        return movie_data
    except OmdbError as e:
        # Map OMDb errors to a 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Catch-all for unexpected issues
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    



@app.get("/search/serper")
def search_serper(
    query: str = Query(..., description="Search query for Serper (Google search)"),
    num_results: int = Query(5, ge=1, le=10, description="Number of results to return (1–10)"),
):
    """
    Perform a web search using Serper API and return simplified results.

    Example:
    /search/serper?query=Inception%202010%20movie
    """
    try:
        serper_raw = search_web_with_serper(query=query, num_results=num_results)
        results = extract_simple_results(serper_raw, limit=num_results)
        return {
            "query": query,
            "results": results,
        }
    except SerperError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


@app.get("/movies/imdb-scrape")
def get_movie_imdb_scrape(
    title: str = Query(..., description="Movie title to search on IMDb via Serper"),
    year: Optional[int] = Query(None, description="Optional year to improve search"),
):
    """
    Use Serper to find the IMDb page for a movie, then scrape that page for extra details.

    Example:
    /movies/imdb-scrape?title=Inception&year=2010
    """
    # 1. Build search query
    if year:
        query = f"{title} {year} site:imdb.com/title"
    else:
        query = f"{title} movie site:imdb.com/title"

    try:
        # 2. Search via Serper
        serper_raw = search_web_with_serper(query=query, num_results=5)

        # 3. Extract first IMDb title URL
        imdb_url = find_imdb_url(serper_raw)

        # 4. Scrape that IMDb page
        scraped_data = scrape_imdb_movie_page(imdb_url)

        return {
            "search_query": query,
            "imdb_data": scraped_data,
        }

    except SerperError as e:
        raise HTTPException(status_code=400, detail=f"Serper error: {e}")
    except ImdbScraperError as e:
        raise HTTPException(status_code=400, detail=f"IMDb scraping error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
