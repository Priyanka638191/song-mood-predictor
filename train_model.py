import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("mood_data.csv")

# Define the features and target
features = [
    'danceability', 'acousticness', 'energy', 'instrumentalness', 
    'liveness', 'valence', 'loudness', 'speechiness', 'tempo', 
    'key', 'time_signature', 'length', 'popularity'
]

X = df[features]
y = df['mood']

# Handle missing values if any
X = X.fillna(0)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
