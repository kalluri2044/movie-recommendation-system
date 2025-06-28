# Contributing to Movie Recommendation System

Thank you for your interest in contributing to the Movie Recommendation System! This document provides guidelines for contributions.

## 🤝 How to Contribute

### 1. Fork the Repository
- Click the "Fork" button on the top right of the repository page
- Clone your fork locally:
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Set Up Development Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests to ensure everything works
python test_app.py
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
- Write clean, well-documented code
- Follow Python PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed

### 5. Test Your Changes
```bash
# Run tests
python test_app.py

# Test the app locally
streamlit run app.py
```

### 6. Commit and Push
```bash
git add .
git commit -m "Add feature: your feature description"
git push origin feature/your-feature-name
```

### 7. Create a Pull Request
- Go to your fork on GitHub
- Click "New Pull Request"
- Provide a clear description of your changes

## 🐛 Bug Reports

When reporting bugs, please include:
- Python version
- Operating system
- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- Screenshots (if applicable)

## 💡 Feature Requests

For feature requests, please:
- Check if the feature already exists
- Provide a clear description of the feature
- Explain the use case and benefits
- Consider implementation complexity

## 📝 Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Comment complex logic

## 🧪 Testing

- Add tests for new features
- Ensure all existing tests pass
- Test on different Python versions if possible
- Test the Streamlit interface manually

## 📚 Documentation

- Update README.md for new features
- Add docstrings to new functions
- Update comments for changed logic
- Consider adding examples

## 🎯 Areas for Contribution

### High Priority
- 🔧 **Performance Optimization**: Improve recommendation speed
- 🎨 **UI/UX Improvements**: Better interface design
- 🧪 **More Algorithms**: Add new recommendation methods
- 📊 **Evaluation Metrics**: Add accuracy measurements

### Medium Priority
- 🔍 **Search Functionality**: Find movies by genre/year
- 📈 **Analytics Dashboard**: User behavior insights
- 🌐 **Deployment**: Docker/cloud deployment guides
- 🔐 **User Authentication**: User profiles and history

### Low Priority
- 🎵 **Other Domains**: Music/book recommendations
- 🤖 **Deep Learning**: Neural collaborative filtering
- 📱 **Mobile App**: React Native/Flutter version
- 🌍 **Internationalization**: Multi-language support

## ❓ Questions?

Feel free to:
- Open an issue for questions
- Join discussions in pull requests
- Reach out to maintainers

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors will be:
- Added to the Contributors section in README
- Mentioned in release notes
- Given credit in documentation

Thank you for making the Movie Recommendation System better! 🎬✨
