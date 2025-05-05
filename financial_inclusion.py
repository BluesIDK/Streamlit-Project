import joblib
import streamlit as st

# Load the trained model
model = joblib.load('random_forest_bank_model.pkl')

# Input fields
st.title("Bank Account Prediction")
country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
age = st.slider("Age", 16, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
job_type = st.selectbox("Job Type", ["Self employed", "Formally employed", ...])

# Create input DataFrame (preprocessed format!)
input_data = ...

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("This person is likely to have a bank account.")
    else:
        st.error("This person is unlikely to have a bank account.")
