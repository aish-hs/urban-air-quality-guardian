import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


def prepare_features(df):
    """
    Prepare features for AQI prediction.
    """

    feature_columns = [
        "PM2.5",
        "PM10",
        "NO2",
        "CO",
        "SO2"
    ]

    X = df[feature_columns]

    y = df["AQI"]

    return X, y


def train_prediction_model(df):
    """
    Train Random Forest model for AQI prediction.
    """

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    return model, mae, r2


def predict_future_aqi(model, pollutants):
    """
    Predict AQI using pollutant values.
    """

    feature_data = pd.DataFrame(
        [pollutants],
        columns=[
            "PM2.5",
            "PM10",
            "NO2",
            "CO",
            "SO2"
        ]
    )

    prediction = model.predict(
        feature_data
    )[0]

    return round(float(prediction), 2)


def generate_forecast(model, current_pollutants):
    """
    Generate demo forecasts for
    24, 48 and 72 hours.
    """

    forecasts = {}

    changes = {
        "24 Hours": 1.05,
        "48 Hours": 0.97,
        "72 Hours": 1.02
    }

    for period, factor in changes.items():

        future_pollutants = {
            pollutant: value * factor
            for pollutant, value in current_pollutants.items()
        }

        predicted_aqi = predict_future_aqi(
            model,
            future_pollutants
        )

        forecasts[period] = predicted_aqi

    return forecasts