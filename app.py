import os
import json
import streamlit as st
from tmdb import search_movie, search_tv, add_to_favorites

# Sayfa başlığı ve yapılandırma
st.set_page_config(page_title="CineSelect Manager", layout="centered")
st.title("🎬 CineSelect Manager")

# --- favorites.json format kontrolü ---
def ensure_favorites_structure():
    if os.path.exists("favorites.json"):
        with open("favorites.json", "r") as f:
            try:
                data = json.load(f)
                if isinstance(data, list):  # eski format
                    new_data = {"movies": data, "shows": []}
                    with open("favorites.json", "w") as fw:
                        json.dump(new_data, fw, indent=2)
            except:
                pass

ensure_favorites_structure()

# Film veya Dizi seçimi
media_type = st.radio("What would you like to search for?", ["Movie", "TV Show"], horizontal=True)

# Arama kutusu
query = st.text_input(f"🔍 Search for a {media_type.lower()}")
if query:
    results = search_movie(query) if media_type == "Movie" else search_tv(query)
    for idx, item in enumerate(results):
        st.image(item["poster"])
        st.markdown(f"**{item['title']} ({item['year']})**")
        st.markdown(f"⭐ IMDb: {item['imdb']} &nbsp;&nbsp; 🍅 RT: {item['rt']}%")

        stars = st.slider("Friend Rating", 1, 5, 3, key=f"stars_{idx}")
        if st.button("Add to Favorites", key=f"btn_{idx}"):
            add_to_favorites(item, stars, media_type.lower())
            st.success(f"✅ {item['title']} added to {media_type.lower()} favorites!")

# --- Favoriler bölümü ---
st.markdown("---")
st.subheader("❤️ Your Favorites")

def show_favorites(fav_type, label):
    if os.path.exists("favorites.json"):
        with open("favorites.json", "r") as f:
            data = json.load(f)
        favs = data.get(fav_type, [])
        if favs:
            st.markdown(f"### 📁 {label}")
            for fav in favs:
                st.image(fav["poster"], width=150)
                st.markdown(f"**{fav['title']} ({fav['year']})**")
                st.markdown(f"⭐ IMDb: {fav['imdb']} &nbsp;&nbsp; 🍅 RT: {fav['rt']}%")
                st.markdown(f"👥 Friend Rating: {fav['friendRating']}")
                st.markdown("---")
        else:
            st.info(f"No {label.lower()} favorites yet.")
    else:
        st.info("No favorites file found.")

show_favorites("movies", "Favorite Movies")
show_favorites("shows", "Favorite TV Shows")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by <b>SS</b></p>", unsafe_allow_html=True)
