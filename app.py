from flask import Flask, request, render_template
import pickle
import numpy as np

# Load only the model (NO vectorizer needed!)
model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Collect inputs from form
            input_data = [
                float(request.form['danceability']),
                float(request.form['acousticness']),
                float(request.form['energy']),
                float(request.form['instrumentalness']),
                float(request.form['liveness']),
                float(request.form['valence']),
                float(request.form['loudness']),
                float(request.form['speechiness']),
                float(request.form['tempo']),
                int(request.form['key']),
                int(request.form['time_signature']),
                int(request.form['length']),
                int(request.form['popularity']),
            ]
            input_array = np.array([input_data])
            prediction = model.predict(input_array)[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
