import os
import json
import streamlit as st
from tmdb import search_movie, add_to_favorites

# Sayfa başlığı ve yapılandırma
st.set_page_config(page_title="CineSelect Manager", layout="centered")
st.title("🎬 CineSelect Manager")

# Film arama bölümü
query = st.text_input("🔍 Search for a movie")
if query:
    results = search_movie(query)
    for idx, movie in enumerate(results):
        st.image(movie["poster"])
        st.markdown(f"**{movie['title']} ({movie['year']})**")
        st.markdown(f"⭐ IMDb: {movie['imdb']} &nbsp;&nbsp; 🍅 RT: {movie['rt']}%")

        stars = st.slider("Friend Rating", 1, 5, 3, key=f"stars_{idx}")
        if st.button("Add to Favorites", key=f"btn_{idx}"):
            add_to_favorites(movie, stars)
            st.success(f"✅ {movie['title']} added to favorites!")

# Favori filmleri gösterme bölümü
st.markdown("---")
st.subheader("❤️ Your Favorite Movies")

if os.path.exists("favorites.json"):
    with open("favorites.json", "r") as f:
        favs = json.load(f)

    if favs:
        for fav in favs:
            st.image(fav["poster"], width=150)
            st.markdown(f"**{fav['title']} ({fav['year']})**")
            st.markdown(f"⭐ IMDb: {fav['imdb']} &nbsp;&nbsp; 🍅 RT: {fav['rt']}%")
            st.markdown(f"👥 Friend Rating: {fav['friendRating']}")
            st.markdown("---")
    else:
        st.info("You haven't added any favorites yet.")
else:
    st.info("No favorites found yet.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Created by <b>SS</b></p>", unsafe_allow_html=True)
