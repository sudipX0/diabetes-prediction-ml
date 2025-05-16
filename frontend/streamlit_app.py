import requests
import streamlit as st

st.title("Diabetes Prediction")

# Input fields for only the 5 features the model expects
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0.0, max_value=300.0, value=120.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=30.0)
diabetes_pedigree_function = st.number_input(
    "Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5
)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

if st.button("Predict"):
    input_data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "bmi": bmi,
        "diabetes_pedigree_function": diabetes_pedigree_function,
        "age": age,
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)
        prediction = response.json().get("prediction")
        if prediction == 1:
            st.error("Prediction: Diabetes Positive")
        else:
            st.success("Prediction: Diabetes Negative")
    except Exception as e:
        st.error(f"Error: {e}")
