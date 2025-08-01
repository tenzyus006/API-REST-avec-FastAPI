from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os

app = FastAPI()
mlb = None
pipeline = None

@app.on_event("startup")
def load_models():
    global mlb, pipeline
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    mlb_path = os.path.join(BASE_DIR, "mlb.pkl")
    pipeline_path = os.path.join(BASE_DIR, "logistic_model_tfidf.pkl")
    mlb = joblib.load(mlb_path)
    pipeline = joblib.load(pipeline_path)

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
