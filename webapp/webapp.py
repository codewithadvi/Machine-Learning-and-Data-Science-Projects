import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model (load it once outside the Streamlit button)
rf = joblib.load(r"E:\ADVI\Code\python\webapp\fhs_rf_model.pkl")

# Streamlit UI
st.write("# 10 Year Heart Disease Prediction")

# Collect user input
gender = st.selectbox("Select your gender:", ["Male", "Female"])
col1, col2, col3 = st.columns(3)

# Getting user input
age = col2.number_input("Enter your age")
education = col3.selectbox("Highest academic qualification", ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])

isSmoker = col1.selectbox("Are you currently a smoker?", ["Yes", "No"])
yearsSmoking = col2.number_input("Number of daily cigarettes")

BPMeds = col3.selectbox("Are you currently on BP medication?", ["Yes", "No"])
stroke = col1.selectbox("Have you ever experienced a stroke?", ["Yes", "No"])
hyp = col2.selectbox("Do you have hypertension?", ["Yes", "No"])
diabetes = col3.selectbox("Do you have diabetes?", ["Yes", "No"])

chol = col1.number_input("Enter your cholesterol level")
sys_bp = col2.number_input("Enter your systolic blood pressure")
dia_bp = col3.number_input("Enter your diastolic blood pressure")
bmi = col1.number_input("Enter your BMI")
heart_rate = col2.number_input("Enter your resting heart rate")
glucose = col3.number_input("Enter your glucose level")

# Only process prediction if button is pressed
if st.button('Predict'):
    # Prepare input data for prediction
    df_pred = pd.DataFrame([[gender, age, education, isSmoker, yearsSmoking, BPMeds, stroke, hyp, diabetes, chol, sys_bp, dia_bp, bmi, heart_rate, glucose]],
                    columns=['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

    # Apply transformations to the data to match the model's expectations
    df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)  # Convert gender to 0/1
    df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)

    # Transform education levels to numeric values
    def transform(data):
        result = 3
        if data == 'High school diploma':
            result = 0
        elif data == 'Undergraduate degree':
            result = 1
        elif data == 'Postgraduate degree':
            result = 2
        return result
    df_pred['education'] = df_pred['education'].apply(transform)

    # Ensure the model uses the correct feature names (including the corrected 'male' column)
    df_pred = df_pred.rename(columns={'gender': 'male'})  # Rename 'gender' to 'male' as per model expectations

    # Predict using the model
    prediction = rf.predict(df_pred)

    # Display result based on prediction
    if prediction[0] == 0:
        st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>', unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>', unsafe_allow_html=True)
