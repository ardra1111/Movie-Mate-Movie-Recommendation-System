import streamlit as st
import pandas as pd
import pickle
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances =  similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
# Display the title and header
st.title("Movie Mate")
st.subheader("Movie Recommendation System")
st.image('moviemate.png', width=250)


# Function to replace blank space with an actual space
def format_movie_name(movie_name):
    if movie_name == '':
        return ' '
    else:
        return movie_name

# Display the input message with emphasized text
st.markdown("<p style='font-weight: bold;'>Enter a movie title and get recommendations for similar movies</p>", unsafe_allow_html=True)

# Display the select box for movie selection
selected_movie_name = st.selectbox(
    'Select a movie title:',
    [''] + list(movies['title'].values),  # Add a blank space as the first option
    format_func=format_movie_name
)

# Button to trigger recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)