from diabetes import *

def predict_manual_input(input_data):
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
    
    input_data_scaled = scaler.transform([input_data])
    prediction = model.predict(input_data_scaled)
    return "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

# Example manual test
manual_input = [45, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1]  # Example input
print("Manual Input Prediction:", predict_manual_input(manual_input))
