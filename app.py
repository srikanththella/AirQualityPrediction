from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

#Load the trained model
model_path = 'final_random_forest_model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/predict',methods=['POST'])
def predict():
    #Extract data from form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    # print(final_features)
    #Make prediction
    prediction = model.predict(final_features)
    output = 'Good Air' if prediction[0]==1 else 'Poor Air'

    return render_template('app.html',prediction_text = 'Prediction:{}'.format(output))


if __name__=="__main__":
    app.run(debug=True)