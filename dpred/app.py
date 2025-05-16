from fastapi import FastAPI
import joblib
from pydantic import BaseModel

from dpred.config import settings

app = FastAPI(title="Diabetes Prediction API")

model = joblib.load(settings.model_path)


class DiabetesInput(BaseModel):
    pregnancies: int
    glucose: float
    bmi: float
    diabetes_pedigree_function: float
    age: int


@app.get("/")
def root():
    return {"message": "Welcome to the Diabetes Prediction API"}


@app.post("/predict")
def predict(data: DiabetesInput):
    features = [
        data.pregnancies,
        data.glucose,
        data.bmi,
        data.diabetes_pedigree_function,
        data.age,
    ]
    prediction = model.predict([features])[0]
    return {"prediction": int(prediction)}
