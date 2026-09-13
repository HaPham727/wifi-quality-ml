import streamlit as st
import pandas as pd
import joblib

# =========================
# 1. Load mô hình
# =========================

model = joblib.load("models/linear_regression_model.joblib")

# =========================
# 2. Config trang
# =========================

st.set_page_config(
    page_title="Dự đoán băng thông Wi-Fi",
    page_icon="📶",
    layout="centered"
)

st.title("Dự đoán băng thông Wi-Fi")

st.write(
    "Dự đoán băng thông Wi-Fi từ các thông số đo được từ client-side,"
)

# =========================
# 3. Nhận input người dùng
# =========================

st.header("Các thông số đầu vào")

distance = st.number_input(
    "Khoảng cách (m)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)

signal = st.number_input(
    "Cường độ tín hiệu (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

rx_rate = st.number_input(
    "Tốc độ liên kết (Mbps)",
    min_value=0.0,
    value=433.0,
    step=1.0
)

rtt = st.number_input(
    "Thời gian trễ trọn vòng (ms)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

jitter = st.number_input(
    "Biến thiên độ trễ (ms)",
    min_value=0.0,
    value=2.0,
    step=0.1
)

packet_loss = st.number_input(
    "Tỷ lệ mất gói tin (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.1
)

# =========================
# 4. Dự đoán
# =========================

if st.button("Dự đoán băng thông"):

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
    X_input = input_data

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Prevent negative displayed throughput
    prediction = max(0, prediction)

    st.success(
        f"Băng thông dự đoán là: {prediction:.2f} Mbps"
    )