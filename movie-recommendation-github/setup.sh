#!/bin/bash

# Movie Recommendation System Setup Script
echo "🎬 Movie Recommendation System Setup"
echo "===================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.7+ first."
    exit 1
fi

echo "✅ Python found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv movie-rec-env

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source movie-rec-env/Scripts/activate
else
    source movie-rec-env/bin/activate
fi

echo "✅ Virtual environment activated"

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

echo "✅ All dependencies installed"

# Check if dataset exists
if [ ! -d "ml-100k" ]; then
    echo "⚠️  MovieLens dataset not found!"
    echo "📥 Please download the MovieLens 100K dataset:"
    echo "   1. Visit: https://grouplens.org/datasets/movielens/100k/"
    echo "   2. Download ml-100k.zip"
    echo "   3. Extract to this directory"
    echo ""
fi

echo "🚀 Setup complete!"
echo ""
echo "To run the application:"
echo "1. Activate virtual environment:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "   source movie-rec-env/Scripts/activate"
else
    echo "   source movie-rec-env/bin/activate"
fi
echo "2. Run: streamlit run app.py"
echo "3. Open: http://localhost:8501"
