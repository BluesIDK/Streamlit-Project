import joblib
import streamlit as st
import pandas as pd

# Load the trained model
model = joblib.load('random_forest_bank_model.pkl')

# Input fields
st.title("💳 Bank Account Prediction")

country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
year = st.selectbox("Year", [2016, 2017, 2018])  # Adjust if you only trained on one year
location_type = st.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
household_size = st.slider("Household Size", 1, 20)
age = st.slider("Age", 16, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
relationship = st.selectbox("Relationship with Head", [
    "Head of Household", "Spouse", "Child", "Parent", "Other Relative", "Other non-relatives"
])
marital_status = st.selectbox("Marital Status", [
    "Married", "Single", "Widowed", "Divorced/Separated", "Don't know"
])
education_level = st.selectbox("Education Level", [
    "No formal education", "Primary education", "Secondary education", "Tertiary education", "Vocational/Specialised training"
])
job_type = st.selectbox("Job Type", [
    'Dont Know/Refuse to answer', 'Farming and Fishing', 'Formally employed Government',
    'Formally employed Private', 'Government Dependent', 'Informally employed',
    'No Income', 'Other Income', 'Remittance Dependent', 'Self employed'
])

# Mappings (must match training!)
country_map = {'Kenya': 0, 'Rwanda': 1, 'Tanzania': 2, 'Uganda': 3}
location_map = {'Urban': 1, 'Rural': 0}
cell_map = {'Yes': 1, 'No': 0}
gender_map = {'Male': 1, 'Female': 0}
relationship_map = {
    "Head of Household": 0,
    "Spouse": 1,
    "Child": 2,
    "Parent": 3,
    "Other Relative": 4,
    "Other non-relatives": 5
}
marital_map = {
    "Married": 0,
    "Single": 1,
    "Widowed": 2,
    "Divorced/Separated": 3,
    "Don't know": 4
}
education_map = {
    "No formal education": 0,
    "Primary education": 1,
    "Secondary education": 2,
    "Tertiary education": 3,
    "Vocational/Specialised training": 4
}
job_map = {
    'Dont Know/Refuse to answer': 0,
    'Farming and Fishing': 1,
    'Formally employed Government': 2,
    'Formally employed Private': 3,
    'Government Dependent': 4,
    'Informally employed': 5,
    'No Income': 6,
    'Other Income': 7,
    'Remittance Dependent': 8,
    'Self employed': 9
}

# Create DataFrame with ALL features
input_data = pd.DataFrame([{
    'country': country_map[country],
    'year': year,
    'location_type': location_map[location_type],
    'cellphone_access': cell_map[cellphone_access],
    'household_size': household_size,
    'age_of_respondent': age,
    'gender_of_respondent': gender_map[gender],
    'relationship_with_head': relationship_map[relationship],
    'marital_status': marital_map[marital_status],
    'education_level': education_map[education_level],
    'job_type': job_map[job_type]
}])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ This person is likely to have a bank account.")
    else:
        st.warning("🚫 This person is unlikely to have a bank account.")
