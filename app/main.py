from fastapi import FastAPI

app = FastAPI(
    title="Smart Movie Finder API",
    description="Backend-only API that uses OMDb, Serper, and web scraping to fetch movie info.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Smart Movie Finder API is running"}

