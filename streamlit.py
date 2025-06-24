import streamlit as st
import joblib
import numpy as np
import requests
    
def main():
    st.set_page_config(page_title = "RS Setia Gaji")
    st.title("Patient Obesity Checkkk")

    gender = st.radio("Gender : ", ["Male", "Female"])
    age = st.number_input("Age : ", 1, 100)
    height_cm = st.number_input("Height (cm) : ", 1, 210)
    weight_kg = st.number_input("Weight (kg) : ", 1.0, 200.0)
    foh = st.radio("Family Overweight Histroy : ", ["yes","no"])
    vcf = st.number_input("Frequency of Vegetable Consumtion : ", 1, 3)
    mmc = st.number_input("Count of Main Meal : ", 1, 4)
    snack_freq = st.radio("Frequecny of Snack Consumtion : ", ["Always", "Frequently", "Sometimes", "no"])
    tut = st.number_input("Tech Usage Time: ", 1, 3)
    acf = st.radio("Frequecny of Alcohol Consumtion : ", ["Always", "Frequently", "Sometimes", "no"])

    inputs = {
        'gender' : gender,
        'age' : int(age),
        'height_m' : float(height_cm/100),
        'weight_kg' : float(weight_kg),
        'family_overweight_history' : foh,
        'vegetable_consumtion_freq' : float(vcf),
        'main_meal_count' : float(mmc),
        'snack_freq' : snack_freq,
        'tech_use_time' : float(tut),
        'alcohol_consumption_freq' : acf
    }

    if st.button('Make Predicition'):
        result = make_preds(inputs)
        st.success(f'This Patient is on : {result}')

def make_preds(inputs):
    response = requests.post("http://127.0.0.1:8000/predict", json=inputs)
    return response.json()["prediction"]

if __name__ == '__main__':
    main()
