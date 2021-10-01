import streamlit as st
import pandas as pd
import pickle

  
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances   = similarity[movie_index]
    mlist  = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies= []
    for i in mlist:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies = pickle.load(open('movies.pkl','rb'))
movies = movies['title'].values

st.title("Movie Recommendation System")

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
'Enter the movie',movies)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
