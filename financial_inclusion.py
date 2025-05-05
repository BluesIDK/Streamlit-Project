import pandas as pd
# Load the dataset
df = pd.read_csv("C:/Users/amira/Desktop/WHATEVER/Financial_inclusion_dataset.csv")

# Display first rows
print(df.head())

# Dataset shape (rows, columns)
print(df.shape)

# Column names
print(df.columns)

# Unique values in the target variable
print(df['bank_account'].value_counts())

# Info about types, non-null counts, etc.
df.info()

# Check for missing values
print(df.isnull().sum())

# Basic stats
print(df.describe(include='all'))

# Drop rows with missing target values
df = df.dropna(subset=['bank_account'])

# For simplicity, drop rows with any NA (or handle specific columns)
df = df.dropna()

# Remove duplicated rows
df = df.drop_duplicates()

# Example: remove age outliers using IQR
Q1 = df['age_of_respondent'].quantile(0.25)
Q3 = df['age_of_respondent'].quantile(0.75)
IQR = Q3 - Q1

# Filter data
df = df[(df['age_of_respondent'] >= Q1 - 1.5*IQR) & (df['age_of_respondent'] <= Q3 + 1.5*IQR)]

from sklearn.preprocessing import LabelEncoder

# Encode target variable
df['bank_account'] = df['bank_account'].map({'Yes': 1, 'No': 0})

# Encode all object columns (except uniqueid)
categorical_columns = df.select_dtypes(include=['object']).columns.drop('uniqueid')

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Define features and target
X = df.drop(columns=['bank_account', 'uniqueid'])
y = df['bank_account']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# streamlit_app.py
import streamlit as st
import pickle

# Load model
model = pickle.load(open("rf_model.pkl", "rb"))

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

import pickle

with open("rf_model.pkl", "wb") as f:
    pickle.dump(model, f)
