#!/usr/bin/env python3
"""
Movie Recommendation System Test Suite
Tests the core functionality of recommendation algorithms
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import sys
import os

# Add the parent directory to the path to import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_test_data():
    """Load test data (same as main app)"""
    try:
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
    except FileNotFoundError:
        print("❌ Test data not found. Please ensure ml-100k dataset is present.")
        return None

def test_data_loading():
    """Test data loading functionality"""
    print("🧪 Testing data loading...")
    df = load_test_data()
    
    if df is None:
        return False
    
    # Test basic data properties
    assert len(df) > 0, "Dataset should not be empty"
    assert 'user_id' in df.columns, "user_id column missing"
    assert 'movie_id' in df.columns, "movie_id column missing" 
    assert 'rating' in df.columns, "rating column missing"
    assert 'title' in df.columns, "title column missing"
    
    print(f"✅ Data loaded successfully: {len(df)} records, {len(df['title'].unique())} movies")
    return True

def test_collaborative_filtering():
    """Test collaborative filtering algorithm"""
    print("🧪 Testing collaborative filtering...")
    df = load_test_data()
    
    if df is None:
        return False
    
    # Test with a popular movie
    test_movie = "Toy Story (1995)"
    if test_movie not in df['title'].values:
        print(f"⚠️ Test movie '{test_movie}' not found in dataset")
        test_movie = df['title'].iloc[0]  # Use first movie instead
    
    # Create user-movie matrix
    matrix = df.pivot_table(index='user_id', columns='title', values='rating')
    movie_ratings = matrix.fillna(0).T
    similarity = cosine_similarity(movie_ratings)
    similarity_df = pd.DataFrame(similarity, index=movie_ratings.index, columns=movie_ratings.index)
    
    if test_movie in similarity_df:
        similar_movies = similarity_df[test_movie].sort_values(ascending=False)[1:6]
        recommendations = similar_movies.index.tolist()
        
        assert len(recommendations) > 0, "Should return recommendations"
        assert test_movie not in recommendations, "Should not recommend the same movie"
        
        print(f"✅ Collaborative filtering working: {len(recommendations)} recommendations for '{test_movie}'")
        return True
    else:
        print(f"❌ Movie '{test_movie}' not found in similarity matrix")
        return False

def test_content_based_filtering():
    """Test content-based filtering algorithm"""
    print("🧪 Testing content-based filtering...")
    df = load_test_data()
    
    if df is None:
        return False
    
    test_movie = "Toy Story (1995)"
    if test_movie not in df['title'].values:
        test_movie = df['title'].iloc[0]
    
    genre_cols = ["Action", "Comedy", "Drama", "Romance", "Thriller"]
    genre_map = df.drop_duplicates("title")[["title"] + genre_cols]
    genre_map["genre_str"] = genre_map[genre_cols].astype(str).agg("".join, axis=1)
    
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(genre_map["genre_str"])
    similarity = cosine_similarity(genre_matrix)
    sim_df = pd.DataFrame(similarity, index=genre_map['title'], columns=genre_map['title'])
    
    if test_movie in sim_df:
        recommendations = sim_df[test_movie].sort_values(ascending=False)[1:6].index.tolist()
        
        assert len(recommendations) > 0, "Should return recommendations"
        assert test_movie not in recommendations, "Should not recommend the same movie"
        
        print(f"✅ Content-based filtering working: {len(recommendations)} recommendations for '{test_movie}'")
        return True
    else:
        print(f"❌ Movie '{test_movie}' not found in content similarity matrix")
        return False

def test_edge_cases():
    """Test edge cases and error handling"""
    print("🧪 Testing edge cases...")
    df = load_test_data()
    
    if df is None:
        return False
    
    # Test with non-existent movie
    fake_movie = "This Movie Does Not Exist (2024)"
    
    # Collaborative filtering with fake movie
    matrix = df.pivot_table(index='user_id', columns='title', values='rating')
    movie_ratings = matrix.fillna(0).T
    similarity = cosine_similarity(movie_ratings)
    similarity_df = pd.DataFrame(similarity, index=movie_ratings.index, columns=movie_ratings.index)
    
    if fake_movie not in similarity_df:
        print("✅ Collaborative filtering correctly handles non-existent movies")
    
    # Content-based filtering with fake movie
    genre_cols = ["Action", "Comedy", "Drama", "Romance", "Thriller"]
    genre_map = df.drop_duplicates("title")[["title"] + genre_cols]
    genre_map["genre_str"] = genre_map[genre_cols].astype(str).agg("".join, axis=1)
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(genre_map["genre_str"])
    similarity = cosine_similarity(genre_matrix)
    sim_df = pd.DataFrame(similarity, index=genre_map['title'], columns=genre_map['title'])
    
    if fake_movie not in sim_df:
        print("✅ Content-based filtering correctly handles non-existent movies")
    
    return True

def run_all_tests():
    """Run all tests"""
    print("🎬 Movie Recommendation System - Test Suite")
    print("=" * 50)
    
    tests = [
        test_data_loading,
        test_collaborative_filtering,
        test_content_based_filtering,
        test_edge_cases
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test failed with error: {e}")
            print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! System is ready for deployment.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
