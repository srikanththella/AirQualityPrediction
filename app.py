from flask import Flask, request, render_template, redirect, url_for
import pickle
import numpy as np
 
app = Flask(__name__)
 
# Load the pre-trained model
model_path = 'final_random_forest_model.pkl'
with open(model_path, 'rb') as file:
    final_rf_model = pickle.load(file)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
 
    # Make Prediction
    prediction = final_rf_model.predict(final_features)
 
    if prediction[0] == 1:
        prediction_text = 'Good'
    else:
        prediction_text = 'Poor'
 
    # Redirect to result.html with prediction_text
    return render_template('result.html', prediction_text=prediction_text)
 
# @app.route('/result')
# def result():
#     prediction_text = request.args.get('prediction')
#     return render_template('result.html', prediction_text=prediction_text)
 
if __name__ == "__main__":
    app.run(debug=True)
