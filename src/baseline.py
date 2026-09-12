import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

class MeanBaseline:
    def fit(self, y_train):
        self.mean_ = np.mean(y_train)
        return self

    def predict(self, X):
        return np.full(
            shape=len(X),
            fill_value=self.mean_
        )


def evaluate_baseline(y_true, y_pred):
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