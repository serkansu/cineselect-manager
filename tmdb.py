import os
import requests
import json

API_KEY = os.getenv("TMDB_API_KEY")  # Render veya yerel ortamdan API_KEY al
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
            "imdb": 7.5,   # Placeholder – ileride API'den alınabilir
            "rt": 85       # Placeholder – ileride RT API'den alınabilir
        })
    return results

def search_tv(query):
    url = f"{BASE_URL}/search/tv?api_key={API_KEY}&query={query}"
    res = requests.get(url).json()
    results = []
    for item in res.get("results", []):
        results.append({
            "id": f"tt{item['id']}",
            "title": item["name"],
            "year": item["first_air_date"][:4] if item.get("first_air_date") else "N/A",
            "poster": f"{POSTER_BASE}{item['poster_path']}" if item.get("poster_path") else "",
            "description": item.get("overview", ""),
            "imdb": 7.8,   # Placeholder
            "rt": 80       # Placeholder
        })
    return results

def add_to_favorites(item, stars, media_type):
    filename = "favorites.json"
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                data = {"movies": data, "shows": []}
    except:
        data = {"movies": [], "shows": []}

    key = "movies" if media_type == "movie" else "shows"

    item["cineselectRating"] = stars
    data[key].append(item)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
