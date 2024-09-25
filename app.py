import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.header('Movie Recommendation System')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Custom CSS to adjust image size and button styles
st.markdown("""
    <style>
    div.stButton > button {
        background-color: blue;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    
    div.stButton > button:hover {
        background-color: darkblue;
        color: white;
        transform: scale(1.05);
        transition: all 0.2s ease-in-out;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    div.stButton > button:focus {
        background-color: blue !important;
        color: white !important;
    }

    .movie-container {
        text-align: center;
        margin-bottom: 10px;
    }

    .movie-poster {
        width: 100%;
        height: auto;
        max-height: 300px; /* Set a max height to prevent oversized images */
        object-fit: contain; /* Ensure the image fits well within the given space */
    }

    .movie-name {
        color: white;
        margin-top: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    # Loop to display 10 movies, 5 per row
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for j, col in enumerate(cols):
            with col:
                st.markdown(f"""
                    <div class='movie-container'>
                        <img class='movie-poster' src="{recommended_movie_posters[i + j]}" alt="{recommended_movie_names[i + j]}">
                        <div class='movie-name'>{recommended_movie_names[i + j]}</div>
                    </div>
                    """, unsafe_allow_html=True)