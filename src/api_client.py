
import requests


def get_live_air_quality(latitude, longitude):
    """
    Fetch current real-time air quality data
    from Open-Meteo Air Quality API.
    """

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "pm10,"
            "pm2_5,"
            "carbon_monoxide,"
            "nitrogen_dioxide,"
            "sulphur_dioxide,"
            "ozone"
        )
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        current = data.get(
            "current",
            {}
        )

        return {
            "PM2.5": current.get(
                "pm2_5",
                0
            ),

            "PM10": current.get(
                "pm10",
                0
            ),

            "NO2": current.get(
                "nitrogen_dioxide",
                0
            ),

            "CO": current.get(
                "carbon_monoxide",
                0
            ),

            "SO2": current.get(
                "sulphur_dioxide",
                0
            ),

            "O3": current.get(
                "ozone",
                0
            )
        }

    except requests.exceptions.RequestException as error:

        print(
            f"Live AQI API Error: {error}"
        )

        return None


def get_air_quality_forecast(latitude, longitude):
    """
    Fetch 72-hour air quality forecast
    from Open-Meteo Air Quality API.
    """

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,

        "hourly": (
            "pm10,"
            "pm2_5,"
            "carbon_monoxide,"
            "nitrogen_dioxide,"
            "sulphur_dioxide,"
            "ozone"
        ),

        "forecast_days": 3
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "hourly",
            {}
        )

    except requests.exceptions.RequestException as error:

        print(
            f"Forecast API Error: {error}"
        )

        return None

