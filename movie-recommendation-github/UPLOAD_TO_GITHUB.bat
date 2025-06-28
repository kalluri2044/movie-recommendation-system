@echo off
echo 🚀 GitHub Upload Script for Movie Recommendation System
echo =========================================================
echo.
echo This script will help you upload your project to GitHub
echo.
echo Prerequisites:
echo 1. Git must be installed on your system
echo 2. You must have created a repository on GitHub
echo 3. You must have your GitHub username and repository URL ready
echo.
echo Instructions:
echo 1. Create a new repository on GitHub named "movie-recommendation-system"
echo 2. Copy the repository URL (https://github.com/yourusername/movie-recommendation-system.git)
echo 3. Run the commands below in this folder
echo.
echo Commands to run:
echo ================
echo.
echo git init
echo git add .
echo git commit -m "Initial commit: Movie recommendation system with dual algorithms"
echo git branch -M main
echo git remote add origin https://github.com/YOURUSERNAME/movie-recommendation-system.git
echo git push -u origin main
echo.
echo Replace YOURUSERNAME with your actual GitHub username
echo.
echo Press any key to open this folder in Explorer...
pause > nul
explorer .
