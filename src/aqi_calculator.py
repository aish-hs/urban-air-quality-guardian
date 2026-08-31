def get_aqi_category(aqi):
    """
    Classify AQI value into air quality categories.
    """

    if aqi <= 50:
        return {
            "category": "Good",
            "emoji": "🟢",
            "color": "green",
            "description": "Air quality is satisfactory and poses little or no risk."
        }

    elif aqi <= 100:
        return {
            "category": "Moderate",
            "emoji": "🟡",
            "color": "orange",
            "description": "Air quality is acceptable, but sensitive individuals may experience minor effects."
        }

    elif aqi <= 150:
        return {
            "category": "Unhealthy for Sensitive Groups",
            "emoji": "🟠",
            "color": "darkorange",
            "description": "Sensitive groups should reduce prolonged outdoor exposure."
        }

    elif aqi <= 200:
        return {
            "category": "Unhealthy",
            "emoji": "🔴",
            "color": "red",
            "description": "Everyone may begin to experience health effects."
        }

    elif aqi <= 300:
        return {
            "category": "Very Unhealthy",
            "emoji": "🟣",
            "color": "purple",
            "description": "Health alert: everyone may experience serious health effects."
        }

    else:
        return {
            "category": "Hazardous",
            "emoji": "⚫",
            "color": "maroon",
            "description": "Health emergency conditions. Avoid outdoor exposure."
        }