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
# Models Setup
#################################################

from joblib import load

model_path_1 = os.environ.get('MODEL1_PATH', '') or "model_houseprice.joblib"
print("Loading model Property Price Predictor...")
model_1 = load(model_path_1)

model_path_2 = os.environ.get('MODEL2_PATH', '') or "model_creditscore.joblib"
print("Loading model Credit Score...")
model_2 = load(model_path_2)

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
@app.route("/score_house", methods=["POST"])
def predict_house_price():
    print(request.form)
    house_price = model_1.predict(
        [
            [
            float(request.form['Distance']),
            float(request.form['Rooms']),
            float(request.form['Bathrooms']),
            float(request.form['Bedroom2']),
            float(request.form['Car']),
            float(request.form['Landsize']),
            float(request.form['BuildingArea']),
            float(request.form['Latitude']),
            float(request.form['Longitude']),
            float(request.form['Eastern Metropolitan']),
            float(request.form['Eastern Victoria']),
            float(request.form['Northern Metropolitan']),
            float(request.form['Northern Victoria']),
            float(request.form['South-Eastern Metropolitan']),
            float(request.form['Southern Metropolitan']),
            float(request.form['Western Metropolitan']),
            float(request.form['Western Victoria']),
            float(request.form['YearBuilt']),
            float(request.form['Propertycount']),
            ],
        ]
    )[0]
    print(house_price)
    return jsonify(f"Predicted House Price: {house_price}")

@app.route("/score_credit", methods=["POST"])
def predict_credit_score():
    print(request.form)
    credit_score = model_2.predict(
        [
            [
            float(request.form['Annual_Income']),
            float(request.form['Monthly_Inhand_Salary']),
            float(request.form['Num_Bank_Accounts']),
            float(request.form['Interest_Rate']),
            float(request.form['Delay_from_due_date']),
            float(request.form['Num_of_Delayed_Payment']),
            float(request.form['Num_Credit_Inquiries']),
            float(request.form['Total_EMI_per_month']),
            int(request.form['Credit_Score']),
            ],
        ]
    )[0]
    print(credit_score)
    return jsonify(f"Predicted Credit Score: {credit_score}")

if __name__ == "__main__":

    # run the flask app
    app.run()
