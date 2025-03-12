from fastapi import FastAPI, Form
import joblib
import numpy as np
import pandas as pd
from pydantic import BaseModel
from sklearn.preprocessing import LabelEncoder, StandardScaler
from fastapi.middleware.cors import CORSMiddleware


model_diabetes = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DiabetesInput(BaseModel):
    age: float
    polyuria: int
    polydipsia: int
    sudden_weight_loss: int
    weakness: int
    polyphagia: int
    genital_thrush: int
    visual_blurring: int
    itching: int
    irritability: int


@app.post("/predict/")
async def predict_diabetes(
    age: float = Form(...),
    polyuria: int = Form(...),
    polydipsia: int = Form(...),
    sudden_weight_loss: int = Form(...),
    weakness: int = Form(...),
    polyphagia: int = Form(...),
    genital_thrush: int = Form(...),
    visual_blurring: int = Form(...),
    itching: int = Form(...),
    irritability: int = Form(...)
):
    
    input_data = pd.DataFrame([[age, polyuria, polydipsia, sudden_weight_loss, weakness,
                                polyphagia, genital_thrush, visual_blurring, itching, irritability]],
                              columns=["Age", "Polyuria", "Polydipsia", "sudden weight loss", "weakness", 
                                       "Polyphagia", "Genital thrush", "visual blurring", "Itching", "Irritability"])

    
    input_data["Age"] = scaler.transform(input_data[["Age"]])

    
    for col in ["Polyuria", "Polydipsia", "sudden weight loss", "weakness", "Polyphagia", 
                "Genital thrush", "visual blurring", "Itching", "Irritability"]:
        input_data[col] = label_encoder.transform(input_data[col])

    
    prediction = model_diabetes.predict(input_data)

    
    result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

    return {"prediction": result}
