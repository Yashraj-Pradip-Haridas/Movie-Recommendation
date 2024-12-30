import pandas as pd
import streamlit as st
import pickle
from streamlit import title

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        st.write(movies.iloc[i[0]].title)
    return


movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))
st.title('MovieWatch')
selected_movie_name = st.selectbox('What would you like to watch?', movies["title"].values)
if st.button('Recommend'):
    recommend(selected_movie_name)