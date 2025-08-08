import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("house_pred_mod.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 USA Housing Price Prediction")
st.markdown("Predict house price based on area-specific parameters.")

# Input form
income = st.number_input("Income (in USD)", value=60000.0, format="%.2f")
age = st.number_input("House Age (in years)", value=5.0)
rooms = st.number_input("Number of Rooms", value=6.0)
bedrooms = st.number_input("Number of Bedrooms", value=3.0)
population = st.number_input("Population", value=30000.0)

# Predict button
if st.button("Predict House Price"):
    features = np.array([[income, age, rooms, bedrooms, population]])
    prediction = model.predict(features)[0]
    st.success(f"🏡 Estimated House Price: ${prediction:,.2f}")
