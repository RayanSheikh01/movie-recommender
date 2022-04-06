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
                return [movie_title, genres, poster_path]
        except:
            pass
    
    

st.title("PickMeMovie")
st.header("The place where you are recommended your next movie")
movie = getMovieDetails()
movie_title = movie[0]
genres = movie[1]
genres_dict = {}
for genre in genres:
    name = genre['name']
    genres_dict[name] = genre
poster_path = movie[2]
genres = []
for genre in genres_dict:
    genres.append(genre)


st.header(movie_title)
st.write('Genres:')
for genre in genres:
    st.write(genre)
st.image('https://image.tmdb.org/t/p/w500/' + str(poster_path))
