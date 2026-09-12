import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)



from preprocessing import (
    FEATURES,
    TARGET,
    create_preprocessor
)


DATA_PATH = "../data/data.csv"
MODEL_PATH = "../models/linear_regression_pipeline.joblib"


data = pd.read_csv(DATA_PATH)

X = data[FEATURES]
y = data[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=data["distance_m"]
)

model = Pipeline([
    ("preprocessing", create_preprocessor()),
    ("regression", LinearRegression())
])

model.fit(X_train, y_train)

joblib.dump(model, MODEL_PATH)

print("Model saved to:", MODEL_PATH)


def evaluate_linear_regression(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y_true, y_pred)
    )

    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }