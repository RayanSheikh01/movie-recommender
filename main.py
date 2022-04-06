from platform import release
import streamlit as st
import pandas as pd
import random
import json


movies = pd.read_csv('./movies_metadata.csv')
movies = movies.dropna(axis=0)


def getMovieDetails():
    flag = False
    while flag == False:
        try:
            num = random.randint(1, len(movies.index))
            movie = movies.iloc[num, :]
            movie_title = movie.original_title
            if movie_title is not None:
                poster = movie.belongs_to_collection
                poster = poster.replace("'", '"')
                poster = json.loads(poster)
                poster_path = poster['poster_path']
                genres = movie.genres
                genres = genres.replace("'", '"')
                genres = json.loads(genres)
                tagline = movie.tagline
                release_date = movie.release_date
                return [movie_title, genres, poster_path, tagline, release_date]
        except:
            pass
    
    

st.title("WhatMovie")
st.header("Choose a new movie from a press of a button")
movie = getMovieDetails()
movie_title = movie[0]
genres = movie[1]
tagline = movie[3]
release_date = movie[4]
genres_dict = {}
for genre in genres:
    name = genre['name']
    genres_dict[name] = genre
poster_path = movie[2]
genres = []
for genre in genres_dict:
    genres.append(genre)
genres = str(genres)
genres = genres.replace("'", "")


## Create border
## Put Title, Genre, rating, language, actor next to image 

image_col, details_col = st.columns([2, 5])
with image_col:
    st.image('https://image.tmdb.org/t/p/w300/' + str(poster_path))
with details_col:
    st.header(movie_title)
    st.write(release_date+', ' +tagline+ ', '+genres)
    
    
    

st.button('Choose a new movie', on_click=getMovieDetails)

