from flask import Flask, render_template, request
from sklearn.preprocessing import OrdinalEncoder
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
try:
    with open('model/Salary_prediction_decision_tree.pkl', 'rb') as file:
        salary_pred = pickle.load(file)
except Exception as e:
    print(f"Error loading the model: {e}")

# Sample categorical features
categorical_features_designation = ['Analyst', 'Senior Analyst', 'Associate', 'Senior Manager', 'Manager', 'Director']
categorical_features_unit = ['Finance', 'IT', 'Marketing', 'Operations', 'Web', 'Management']

# Initialize OrdinalEncoder
encoder = OrdinalEncoder()

# Fit and transform the encoder for each categorical feature
encoded_designation = encoder.fit_transform([[category] for category in categorical_features_designation])
encoded_unit = encoder.fit_transform([[category] for category in categorical_features_unit])

# Create dictionaries to store the mapping of category to encoded value
designation_mapping = {category: int(encoded_value) for category, encoded_value in zip(categorical_features_designation, encoded_designation.flatten())}
unit_mapping = {category: int(encoded_value) for category, encoded_value in zip(categorical_features_unit, encoded_unit.flatten())}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        Designation = request.form['Designation']
        Unit = request.form['Unit']
        leaves_used = float(request.form['Leaves_used'])
        leaves_rem = float(request.form['Leaves_rem'])
        Rating = float(request.form['Rating'])
        past_exp = float(request.form['past_exp'])
        
        # Get the encoded values
        design = designation_mapping.get(Designation, None)
        unit = unit_mapping.get(Unit, None)

        if design is None or unit is None:
            return render_template('index.html', prediction='Invalid Designation or Unit')

        # Prepare input for prediction
        input_data = [[design, unit, leaves_used, leaves_rem, Rating, past_exp]]
        print(input_data)
        
        # Make prediction
        
        pred = salary_pred.predict(input_data)
        final_prediction = pred[0]
        return render_template('index.html', prediction=final_prediction)

    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('index.html', prediction='Error in prediction')

if __name__ == "__main__":
    app.run(port=3000, debug=True)
