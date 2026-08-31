import pandas as pd


def load_air_quality_data(file_path):
    """
    Load historical air quality data from CSV.
    """

    df = pd.read_csv(file_path)

    df["Date"] = pd.to_datetime(df["Date"])

    return df


def get_aqi_statistics(df):
    """
    Calculate important AQI statistics.
    """

    return {
        "average_aqi": round(df["AQI"].mean(), 2),
        "maximum_aqi": int(df["AQI"].max()),
        "minimum_aqi": int(df["AQI"].min()),
        "worst_date": df.loc[df["AQI"].idxmax(), "Date"],
        "best_date": df.loc[df["AQI"].idxmin(), "Date"]
    }


def get_pollutant_trends(df):
    """
    Extract pollutant columns for trend visualization.
    """

    pollutant_columns = [
        "PM2.5",
        "PM10",
        "NO2",
        "CO",
        "SO2"
    ]

    return df[
        ["Date"] + pollutant_columns
    ]


def get_recent_data(df, days=7):
    """
    Get most recent air quality records.
    """

    return df.tail(days)