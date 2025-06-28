import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

@st.cache_data
def load_data():
    """Load and cache the movie recommendation dataset"""
    ratings = pd.read_csv("ml-100k/u.data", sep="\t", names=["user_id", "movie_id", "rating", "timestamp"])
    movies = pd.read_csv(
        "ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        header=None,
        names=[
            "movie_id", "title", "release_date", "video_release_date", "IMDb_URL",
            "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
            "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
            "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
        ],
        usecols=["movie_id", "title", "Action", "Comedy", "Drama", "Romance", "Thriller"]
    )
    df = pd.merge(ratings, movies, on="movie_id")
    return df

def create_user_movie_matrix(df):
    """Create user-movie rating matrix for collaborative filtering"""
    return df.pivot_table(index='user_id', columns='title', values='rating')

def get_collaborative_recommendations(title, df, n=5):
    """Get movie recommendations using collaborative filtering"""
    matrix = create_user_movie_matrix(df)
    movie_ratings = matrix.fillna(0).T
    similarity = cosine_similarity(movie_ratings)
    similarity_df = pd.DataFrame(similarity, index=movie_ratings.index, columns=movie_ratings.index)
    
    if title not in similarity_df:
        return []
    
    similar_movies = similarity_df[title].sort_values(ascending=False)[1:n+1]
    return similar_movies.index.tolist()

def get_content_based_recommendations(fav_title, df, n=5):
    """Get movie recommendations using content-based filtering"""
    genre_cols = ["Action", "Comedy", "Drama", "Romance", "Thriller"]
    genre_map = df.drop_duplicates("title")[["title"] + genre_cols]
    genre_map["genre_str"] = genre_map[genre_cols].astype(str).agg("".join, axis=1)
    
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(genre_map["genre_str"])
    similarity = cosine_similarity(genre_matrix)
    sim_df = pd.DataFrame(similarity, index=genre_map['title'], columns=genre_map['title'])
    
    if fav_title not in sim_df:
        return []
    
    return sim_df[fav_title].sort_values(ascending=False)[1:n+1].index.tolist()

def main():
    """Main Streamlit application"""
    st.set_page_config(
        page_title="Movie Recommendation System",
        page_icon="🎬",
        layout="wide"
    )
    
    # Load data
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("❌ Dataset not found! Please ensure the ml-100k folder is present.")
        st.info("Download the MovieLens 100K dataset and place it in the ml-100k folder.")
        return
    
    # Header
    st.title("🎬 Movie Recommendation System")
    st.markdown("---")
    
    # Sidebar with information
    with st.sidebar:
        st.header("📊 Dataset Info")
        st.write(f"**Movies**: {len(df['title'].unique()):,}")
        st.write(f"**Users**: {len(df['user_id'].unique()):,}")
        st.write(f"**Ratings**: {len(df):,}")
        
        st.header("🔍 How it works")
        st.write("**Collaborative Filtering**: Finds users with similar movie preferences")
        st.write("**Content-Based**: Matches movies by genre similarity")
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        movie_list = sorted(df['title'].unique())
        selected_movie = st.selectbox(
            "🎥 Select a movie you like:",
            movie_list,
            help="Choose a movie to get recommendations based on"
        )
    
    with col2:
        method = st.radio(
            "🔧 Choose recommendation method:",
            ["Collaborative Filtering", "Content-Based Filtering"],
            help="Select the algorithm for generating recommendations"
        )
    
    if st.button("🚀 Get Recommendations", type="primary"):
        with st.spinner("Generating recommendations..."):
            if method == "Collaborative Filtering":
                results = get_collaborative_recommendations(selected_movie, df)
                method_desc = "Based on users with similar movie preferences"
            else:
                results = get_content_based_recommendations(selected_movie, df)
                method_desc = "Based on movie genre similarity"
        
        if results:
            st.success(f"✅ Found recommendations using {method}")
            st.caption(method_desc)
            
            st.subheader("🏆 Top 5 Recommended Movies:")
            
            for i, movie in enumerate(results, 1):
                with st.container():
                    st.write(f"**{i}.** {movie}")
        else:
            st.warning("⚠️ No recommendations found. Try another movie or different method.")

if __name__ == "__main__":
    main()
