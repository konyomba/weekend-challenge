from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn 

model = joblib.load('obesity_prediction.pkl')
label_encoder = joblib.load('label_encoder.pkl')

app = FastAPI()

# Defining input data model
class ObesityInput(BaseModel):
    Age: int
    Height: float
    Weight: float
    BMI: float

# prediction endpoint
@app.post("/predict/")
def predict(input_data: ObesityInput):
    # Converting the input data into a numpy array to match the model's expected input format
    features = np.array([[input_data.Age, input_data.Height, input_data.Weight, input_data.BMI]])

    
    prediction_encoded = model.predict(features)

    
    prediction = label_encoder.inverse_transform(prediction_encoded)
    return {"ObesityCategory": prediction[0]}

@app.get("/")
def read_root():
    return {"API": "Obesity Prediction API!"}

