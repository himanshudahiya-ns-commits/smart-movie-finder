import requests

api_key = "f9c67ab"
title = "Inception"

url = f"https://www.omdbapi.com/?apikey={api_key}&t={title}"

response = requests.get(url)
data = response.json()

print("Movie Title:", data["Title"])
print("Year:", data["Year"])
print("Genre:", data["Genre"])
print("Plot:", data["Plot"])

