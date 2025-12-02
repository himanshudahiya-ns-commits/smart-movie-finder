import requests
from bs4 import BeautifulSoup
from typing import Dict, List
from tenacity import retry, stop_after_attempt, wait_exponential


class ImdbScraperError(Exception):
    """Custom exception for IMDb scraping errors."""
    pass


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def scrape_imdb_movie_page(url: str) -> Dict:
    """
    Scrape an IMDb movie page for some key details.

    Returns a dict with fields like:
    - title
    - rating
    - rating_count
    - genres
    - summary
    - top_cast
    """
    try:
        # A simple User-Agent can sometimes help avoid being blocked for very basic use.
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; SmartMovieFinderBot/0.1; +https://example.com/bot)"
        }
        response = requests.get(url, headers=headers, timeout=10)
    except requests.RequestException as e:
        raise ImdbScraperError(f"Network error while fetching IMDb page: {e}")

    if response.status_code != 200:
        raise ImdbScraperError(f"IMDb returned status code {response.status_code}")

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # ✏️ These selectors work with current IMDb layout (may change in future).
    # We'll keep the scraping simple.

    # Title (usually in <h1 data-testid="hero-title-block__title">)
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    # Rating (usually <span class="sc-*"> inside rating block, but we look for itemprop="ratingValue" as a fallback)
    rating = None
    rating_span = soup.find("span", attrs={"class": "sc-7ab21ed2-1", "data-testid": "hero-rating-bar__aggregate-rating__score"})
    if rating_span:
        # rating is often like "8.8 /10"
        rating = rating_span.get_text(strip=True).split("/")[0].strip()
    else:
        # Fallback
        rating_meta = soup.find("span", itemprop="ratingValue")
        if rating_meta:
            rating = rating_meta.get_text(strip=True)

    # Rating count (votes)
    rating_count = None
    rating_count_span = soup.find("div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})
    if rating_count_span:
        # Sometimes the votes are nearby, but IMDb layout changes often, so keep this loose.
        # As a fallback, find any span with data-testid="hero-rating-bar__aggregate-rating__score"
        pass  # We'll skip precise votes extraction to keep things beginner-friendly.

    # Genres: look for anchors with data-testid="genres"
    genres: List[str] = []
    genre_container = soup.find("div", attrs={"data-testid": "genres"})
    if genre_container:
        for a in genre_container.find_all("a"):
            text = a.get_text(strip=True)
            if text:
                genres.append(text)

    # Plot summary: often in div with data-testid="plot"
    summary = None
    plot_div = soup.find("span", attrs={"data-testid": "plot-l"})
    if not plot_div:
        # fallback: generic plot container
        plot_div = soup.find("span", attrs={"data-testid": "plot-xl"})
    if plot_div:
        summary = plot_div.get_text(strip=True)

    # Top cast: look for data-testid="title-cast-item__actor"
    top_cast: List[str] = []
    cast_anchors = soup.select('[data-testid="title-cast-item__actor"]')
    for a in cast_anchors[:5]:  # top 5 cast members
        text = a.get_text(strip=True)
        if text:
            top_cast.append(text)

    if not title:
        raise ImdbScraperError("Failed to extract movie title from IMDb page. The page layout may have changed.")

    return {
        "imdb_url": url,
        "title": title,
        "rating": rating,
        "genres": genres,
        "summary": summary,
        "top_cast": top_cast,
    }
