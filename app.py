# To check if Flask is installed, run the following command in your terminal:
# python -m pip show flask

# Example Python code to check if Flask is installed:
# try:
# 	import flask
# 	print("Flask is installed.")
# except ImportError:
# 	print("Flask is not installed.")

from flask import Flask, jsonify, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity= request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = int(request.form.get('reading_score')),
            writing_score = int(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)