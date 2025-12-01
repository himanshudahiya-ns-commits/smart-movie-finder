import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
OMDB_BASE_URL = os.getenv("OMDB_BASE_URL", "http://www.omdbapi.com/")


SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_BASE_URL = os.getenv("SERPER_BASE_URL", "https://google.serper.dev")