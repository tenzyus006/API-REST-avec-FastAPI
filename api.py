from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("logistic_model_tfidf.pkl")

@app.get("/")
def home():
    return {"message": "API is running!"}