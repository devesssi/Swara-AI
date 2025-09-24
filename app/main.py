from fastapi import FastAPI
from pydantic import BaseModel
from .model import model

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    label: str
    confidence: float

@app.post("/predict", response_model=PredictionOut)
def predict(input: TextIn):
    label, confidence = model.predict(input.text)
    return {"label": label, "confidence": round(confidence, 2)}