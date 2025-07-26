import requests
import json

API_KEY = "3028d7f0a392920b78e3549d4e6a66ec"
BASE_URL = "https://api.themoviedb.org/3"
POSTER_BASE = "https://image.tmdb.org/t/p/w500"

def search_movie(query):
    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
    res = requests.get(url).json()
    results = []
    for item in res.get("results", []):
        results.append({
            "id": f"tt{item['id']}",
            "title": item["title"],
            "year": item["release_date"][:4] if item.get("release_date") else "N/A",
            "poster": f"{POSTER_BASE}{item['poster_path']}" if item.get("poster_path") else "",
            "description": item.get("overview", ""),
            "imdb": 7.5,
            "rt": 85  # Placeholder
        })
    return results

def add_to_favorites(movie, stars):
    try:
        with open("favorites.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    movie["friendRating"] = stars
    data.append(movie)
    with open("favorites.json", "w") as f:
        json.dump(data, f, indent=2)