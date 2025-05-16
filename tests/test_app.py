from fastapi.testclient import TestClient

from dpred.app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Diabetes Prediction API"}


def test_prediction():
    # Sample valid input matching your DiabetesInput model
    input_data = {
        "pregnancies": 1,
        "glucose": 120.0,
        "blood_pressure": 70.0,
        "skin_thickness": 20.0,
        "insulin": 85.0,
        "bmi": 28.0,
        "diabetes_pedigree_function": 0.5,
        "age": 35,
    }
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200
    # Prediction should be 0 or 1 (binary classification)
    prediction = response.json().get("prediction")
    assert prediction in [0, 1]
