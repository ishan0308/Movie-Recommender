# Movie Recommendation System using Cosine Similarity

This repository features a movie recommendation system that leverages cosine similarity to deliver personalized recommendations. By analyzing the similarity between movies based on their features, the system suggests movies that share similar characteristics with those the user prefers.

## Features
- Measures movie similarity using cosine similarity.
- Extracts key features like genre, actors, and ratings to compute similarity scores.
- Delivers movie recommendations based on calculated similarity.
- Enables efficient search and retrieval of movie recommendations.

Link to the deployed app : https://isha-movie-recommender.streamlit.app/

## Installation
1. Clone the repository: `git clone https://github.com/ishan0308/Movie-Recommender.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage
1. Data available at https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
2. Run `streamlit run app.py`
3. Select a movie for which recommendations are desired.
4. The system will generate and display a list of top 10 recommended movies based on cosine similarity.
