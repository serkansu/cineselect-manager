import streamlit as st
from tmdb import search_movie, add_to_favorites

st.title("CineSelect Manager")

query = st.text_input("Search for a movie")
if query:
    results = search_movie(query)
    for movie in results:
        st.image(movie["poster"])
        st.markdown(f"**{movie['title']} ({movie['year']})**")
        st.markdown(f"IMDb: {movie['imdb']}, RT: {movie['rt']}%")
        stars = st.slider("Friend Rating", 1, 5, 3, key=movie["id"])
        if st.button("Add to Favorites", key=movie["id"] + "_btn"):
            add_to_favorites(movie, stars)
            st.success("Added to favorites!")