from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from model.cts import rounding, binary_encode
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('model/mercury_pipeline.pkl')
target_le = joblib.load('model/le_target.pkl')

class ObesityFeature(BaseModel):
    gender: str
    age: int
    height_m: float
    weight_kg: float
    family_overweight_history: str
    vegetable_consumtion_freq: float
    main_meal_count : float
    snack_freq : str
    tech_use_time : float
    alcohol_consumption_freq : str

@app.get("/")
def read_root():
    return {"message" : "Welkam API berjalan"}

@app.post("/predict")
def predict(obesity: ObesityFeature):
    data_input = obesity.dict()
    features = pd.DataFrame([data_input])
    prediction = model.predict(features)
    prediction = target_le.inverse_transform(prediction)[0]
    return {'prediction': prediction}