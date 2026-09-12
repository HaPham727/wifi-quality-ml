import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

FEATURES = [
    "distance_m",
    "signal_mean_pct",
    "rx_link_rate_mean",
    "rtt_mean_ms",
    "jitter_ms",
    "packet_loss_pct"
]

TARGET = "throughput_down_mbps"

def create_preprocessor():
    return Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("scaler", StandardScaler())
    ])