# Movie Recommendation System 🎬

A comprehensive movie recommendation system built with Streamlit and scikit-learn, featuring both collaborative filtering and content-based filtering algorithms.

## 🌟 Features

- **Dual Recommendation Algorithms**:
  - **Collaborative Filtering**: Recommends movies based on users with similar preferences
  - **Content-Based Filtering**: Recommends movies based on genre similarity

- **Interactive Web Interface**: Built with Streamlit for easy use
- **Large Dataset**: Uses MovieLens 100K dataset with 100,000+ ratings
- **Real-time Recommendations**: Get instant movie suggestions
- **Responsive Design**: Works on desktop and mobile devices

## 🎯 Demo

![Movie Recommendation System](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

### How it works:
1. **Select a movie** you like from the dropdown (1,600+ movies available)
2. **Choose recommendation method** (Collaborative or Content-Based)
3. **Get 5 personalized recommendations** instantly!

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download MovieLens Dataset**
```bash
# The ml-100k dataset should be included, but if not:
# Download from: https://grouplens.org/datasets/movielens/100k/
# Extract to ml-100k/ folder
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Dataset Information

**MovieLens 100K Dataset**:
- 🎬 **1,682 movies**
- 👥 **943 users** 
- ⭐ **100,000 ratings** (1-5 scale)
- 🏷️ **19 movie genres**

## 🔧 Technical Details

### Algorithms Implemented

#### 1. Collaborative Filtering
- Creates user-item rating matrix
- Uses cosine similarity to find similar movies
- Recommends based on user behavior patterns

#### 2. Content-Based Filtering  
- Analyzes movie genres (Action, Comedy, Drama, Romance, Thriller)
- Uses CountVectorizer for feature extraction
- Calculates similarity using cosine similarity

### Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **ML Libraries**: scikit-learn, pandas
- **Data Processing**: NumPy, pandas

## 📁 Project Structure

```
movie-recommendation-system/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── ml-100k/              # MovieLens dataset
│   ├── u.data           # User ratings
│   ├── u.item           # Movie information
│   └── ...              # Other dataset files
├── notebooks/            # Development notebooks
└── tests/               # Unit tests
```

## 🎨 Screenshots

### Main Interface
- Clean, intuitive movie selection
- Toggle between recommendation methods
- Real-time results display

### Features Showcase
- **Sidebar**: Dataset statistics and method explanations
- **Responsive**: Works on all screen sizes
- **Fast**: Cached data loading for better performance

## 🔍 Example Usage

```python
# Example: Get recommendations for "Toy Story (1995)"
# Method 1: Collaborative Filtering
recommendations = get_collaborative_recommendations("Toy Story (1995)", df)
# Returns: ["Aladdin (1992)", "Beauty and the Beast (1991)", ...]

# Method 2: Content-Based Filtering  
recommendations = get_content_based_recommendations("Toy Story (1995)", df)
# Returns movies with similar genres
```

## 🧪 Running Tests

```bash
# Run unit tests
python -m pytest tests/

# Run specific test file
python test_app.py
```

## 📈 Performance

- **Data Loading**: Optimized with Streamlit caching
- **Memory Usage**: Efficient matrix operations
- **Response Time**: < 2 seconds for recommendations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MovieLens**: For providing the excellent dataset
- **GroupLens Research**: University of Minnesota
- **Streamlit**: For the amazing web framework
- **scikit-learn**: For machine learning algorithms

## 🎓 Educational Purpose

This project was created for educational purposes to demonstrate:
- Machine Learning recommendation algorithms
- Web application development with Streamlit
- Data processing and analysis with pandas
- User interface design principles

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/movie-recommendation-system](https://github.com/yourusername/movie-recommendation-system)

---

⭐ **Star this repository if you found it helpful!** ⭐
