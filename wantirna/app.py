""" This is the flask application called 'Wantirna'
with both UI and API components
"""

# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Model Setup
#################################################

from joblib import load
model_path = os.environ.get('MODEL_PATH', '') or "model.joblib"
print("Loading model...")
model = load(model_path)

#################################################
# Web User Interface - Front End
#################################################
# note that UI routes return a html response
# you can add as many html pages as you need
# below is an example to get you started...

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# TODO: Add more routes if needed

#################################################
# API - Back End
#################################################
# we will use '/api/..' for our api within flask application
# note that api returns a JSON response
# you can add as many API routes as you need
# below is an example to get you started...

@app.route("/score", methods=["POST"])
def predict():
    labels = ['setosa', 'versicolor', 'virginica']
    index = model.predict(
        [
            [
            float(request.form["Sepal length"]),
            float(request.form["Sepal width"]),
            float(request.form["Petal length"]),
            float(request.form["Petal width"]),
            ],
        ]
    )[0]
    return jsonify(f"Predicted Iris Species: {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
