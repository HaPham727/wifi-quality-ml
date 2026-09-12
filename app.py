import streamlit as st
import pandas as pd
import joblib

from src.preprocessing import prepare_features


# =========================
# 1. Load trained model
# =========================

MODEL_PATH = "models/linear_regression_pipeline.joblib"

model = joblib.load(MODEL_PATH)


# =========================
# 2. Page configuration
# =========================

st.set_page_config(
    page_title="Wi-Fi Throughput Predictor",
    page_icon="📶",
    layout="centered"
)

st.title("📶 Wi-Fi Throughput Prediction")

st.write(
    "Predict Wi-Fi downlink throughput using "
    "client-side Wi-Fi measurements."
)


# =========================
# 3. User inputs
# =========================

st.header("Wi-Fi Measurements")

distance = st.number_input(
    "Distance (m)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)

signal = st.number_input(
    "Signal strength (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

rx_rate = st.number_input(
    "RX link rate (Mbps)",
    min_value=0.0,
    value=433.0,
    step=1.0
)

rtt = st.number_input(
    "RTT mean (ms)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

jitter = st.number_input(
    "Jitter (ms)",
    min_value=0.0,
    value=2.0,
    step=0.1
)

packet_loss = st.number_input(
    "Packet loss (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1
)


# =========================
# 4. Prediction
# =========================

if st.button("Predict Throughput"):

    input_data = pd.DataFrame([{
        "distance_m": distance,
        "signal_mean_pct": signal,
        "rx_link_rate_mean": rx_rate,
        "rtt_mean_ms": rtt,
        "jitter_ms": jitter,
        "packet_loss_pct": packet_loss
    }])

    # Apply the same feature engineering
    # used during model training
    X_input = prepare_features(input_data)

    # Make prediction
    prediction = model.predict(X_input)[0]

    # Prevent negative displayed throughput
    prediction = max(0, prediction)

    st.success(
        f"Predicted Throughput: {prediction:.2f} Mbps"
    )