import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuración de la página
st.set_page_config(page_title="Spaceship Titanic Predictor", page_icon="🚀", layout="wide")

# Título y Descripción
st.title("🚀 Spaceship Titanic: Predicción de Supervivencia Interestelar")
st.markdown("""
    Bienvenido al sistema de predicción interestelar. Este sistema utiliza un modelo de Machine Learning entrenado
    para determinar si un pasajero fue **transportado a otra dimensión** tras la anomalía espacio-temporal.
""")

# Carga del modelo
@st.cache_resource
def load_model():
    model_path = os.path.join("..", "models", "spaceship_titanic_model.pkl")
    return joblib.load(model_path)

try:
    model = load_model()
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}. Asegúrate de haber ejecutado el cuaderno de modelado primero.")
    st.stop()

# Sidebar para inputs
st.sidebar.header("📋 Datos del Pasajero")

def passenger_inputs():
    home_planet = st.sidebar.selectbox("Planeta de Origen", ["Earth", "Europa", "Mars"])
    cryo_sleep = st.sidebar.selectbox("¿Estuvo en Criosueño?", ["True", "False"])
    destination = st.sidebar.selectbox("Destino", ["TRAPPIST-1e", "PSO J318.5-22", "55 Cancri e"])
    age = st.sidebar.slider("Edad", 0, 100, 25)
    vip = st.sidebar.selectbox("¿Es Pasajero VIP?", ["True", "False"])
    
    st.sidebar.subheader("💰 Gastos en Servicios")
    room_service = st.sidebar.number_input("Room Service", 0.0, 15000.0, 0.0)
    food_court = st.sidebar.number_input("Food Court", 0.0, 15000.0, 0.0)
    shopping_mall = st.sidebar.number_input("Shopping Mall", 0.0, 15000.0, 0.0)
    spa = st.sidebar.number_input("Spa", 0.0, 15000.0, 0.0)
    vr_deck = st.sidebar.number_input("VR Deck", 0.0, 15000.0, 0.0)
    
    st.sidebar.subheader("🚢 Ubicación en la Nave")
    deck = st.sidebar.selectbox("Cubierta (Deck)", ["B", "F", "A", "G", "E", "D", "C", "T"])
    side = st.sidebar.selectbox("Lado (Side)", ["P (Babor)", "S (Estribor)"])
    
    # Procesamiento de inputs para el modelo
    planet_map = {"Earth": 0, "Europa": 1, "Mars": 2}
    dest_map = {"TRAPPIST-1e": 2, "PSO J318.5-22": 1, "55 Cancri e": 0}
    deck_map = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "T": 7}
    side_map = {"P (Babor)": 0, "S (Estribor)": 1}
    
    data = {
        'HomePlanet': planet_map[home_planet],
        'CryoSleep': 1 if cryo_sleep == "True" else 0,
        'Destination': dest_map[destination],
        'Age': age,
        'VIP': 1 if vip == "True" else 0,
        'RoomService': room_service,
        'FoodCourt': food_court,
        'ShoppingMall': shopping_mall,
        'Spa': spa,
        'VRDeck': vr_deck,
        'Deck': deck_map[deck],
        'Side': side_map[side]
    }
    
    return pd.DataFrame([data])

input_df = passenger_inputs()

# Main Area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Datos Ingresados")
    st.write(input_df)
    
    if st.button("🔮 Predecir Destino"):
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]
        
        if prediction == 1:
            st.success(f"🌠 ¡EL PASAJERO HA SIDO TRANSPORTADO! (Probabilidad: {prob:.2%})")
            st.balloons()
        else:
            st.info(f"🛸 EL PASAJERO PERMANECE EN NUESTRA DIMENSIÓN (Probabilidad de transporte: {prob:.2%})")

with col2:
    st.image("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80", caption="Exploración Espacial")

st.markdown("---")
st.markdown("© 2024 Proyecto Interestelar - Ruta de Aprendizaje")
