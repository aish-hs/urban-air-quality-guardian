import pandas as pd


def generate_summary_report(
    df,
    aqi_stats,
    hotspots,
    forecasts
):
    """
    Generate a comprehensive air quality summary report.
    """

    latest = df.iloc[-1]

    report = {
        "Current AQI": latest["AQI"],
        "Average AQI": round(aqi_stats["average_aqi"], 2),
        "Maximum AQI": aqi_stats["maximum_aqi"],
        "Minimum AQI": aqi_stats["minimum_aqi"],
        "Total Records": len(df),
        "Hotspots Detected": len(hotspots)
    }

    # Add forecast data
    for period, value in forecasts.items():

        report[f"Predicted AQI ({period})"] = value

    return report


def generate_location_report(locations):
    """
    Generate location-wise air quality report.
    """

    data = []

    for location in locations:

        data.append({
            "Location": location["name"],
            "AQI": location["aqi"],
            "PM2.5": location["pm25"],
            "PM10": location["pm10"]
        })

    return pd.DataFrame(data)


def generate_trend_report(df):
    """
    Generate trend comparison data.
    """

    trend_df = df.copy()

    trend_df["Date"] = pd.to_datetime(
        trend_df["Date"]
    )

    trend_df["Week"] = (
        trend_df["Date"]
        .dt.isocalendar()
        .week
    )

    weekly_trend = (
        trend_df
        .groupby("Week")["AQI"]
        .mean()
        .reset_index()
    )

    monthly_trend = (
        trend_df
        .groupby(
            trend_df["Date"].dt.to_period("M")
        )["AQI"]
        .mean()
        .reset_index()
    )

    monthly_trend["Date"] = (
        monthly_trend["Date"]
        .astype(str)
    )

    return weekly_trend, monthly_trend


def generate_csv_download(df):
    """
    Convert dataframe into CSV bytes for download.
    """

    return df.to_csv(
        index=False
    ).encode("utf-8")