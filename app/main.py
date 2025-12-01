from fastapi import FastAPI, HTTPException, Query
from typing import Optional

from .services_omdb import fetch_movie_from_omdb, OmdbError

app = FastAPI(
    title="Movzie",
    description="Backend-only API that uses OMDb, Serper, and web scraping to fetch movie info.",
    version="0.1.0",
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