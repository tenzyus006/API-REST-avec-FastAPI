from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import requests

app = FastAPI()
mlb = joblib.load("mlb.pkl")
pipeline = joblib.load("logistic_model_tfidf.pkl")

@app.get("/")
def home():
    return {"message": "API is running!"}

class InputData(BaseModel):
    text: str

@app.post("/predict")
def predict(data: InputData):
    if not pipeline or not mlb:
        raise HTTPException(status_code=503, detail="Model not loaded.")
    
    input_text = data.text
    try:
        predicted_binary = pipeline.predict([input_text])
        predicted_tags = mlb.inverse_transform(predicted_binary)
        return {"tags": predicted_tags[0] if predicted_tags else []}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
