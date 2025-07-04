from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import requests

app = FastAPI()

# Environment variable names (these should be URLs)
LOGISTIC_MODEL_URL = os.getenv("LOGISTIC_MODEL_URL")
MLB_URL = os.getenv("MLB_URL")

def download_file(url, filename):
    if url and not os.path.exists(filename):
        print(f"Downloading {filename} ...")
        try:
            r = requests.get(url)
            r.raise_for_status()
            with open(filename, "wb") as f:
                f.write(r.content)
            print(f"{filename} downloaded.")
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to download {filename}: {e}")

pipeline = None
mlb = None

@app.on_event("startup")
def load_models():
    global pipeline, mlb
    try:
        download_file(LOGISTIC_MODEL_URL, "logistic_model_tfidf.pkl")
        download_file(MLB_URL, "mlb.pkl")
        pipeline = joblib.load("logistic_model_tfidf.pkl")
        mlb = joblib.load("mlb.pkl")
        print("Models loaded successfully.")
    except Exception as e:
        print(f"Error during model loading: {e}")

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
