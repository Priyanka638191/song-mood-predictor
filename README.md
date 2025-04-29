A machine learning web application that predicts the mood of a song based on its musical attributes like danceability, acousticness, tempo, energy, and more. Built with Python, Flask, and a Random Forest Classifier trained on structured audio features.

 Features
 Predicts mood of a song using audio features (no lyrics required)
 Machine learning model trained on a labeled dataset (mood_data.csv)
 User-friendly web interface using Flask
 Input includes features like tempo, loudness, valence, etc.
 Model persistence using pickle

 Tech Stack
 Frontend: HTML (Flask templates)
 Backend: Python, Flask
 ML Model: RandomForestClassifier (via scikit-learn)
 Dataset: Structured .csv with song audio features and mood labels
