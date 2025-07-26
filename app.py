import streamlit as st
from tmdb import search_movie, add_to_favorites

st.set_page_config(page_title="CineSelect Manager", layout="centered")
st.title("🎬 CineSelect Manager")

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
