def generate_alerts(current_aqi, forecasts, hotspots):
    """
    Generate smart public safety alerts based on:
    - Current AQI
    - Future AQI predictions
    - Pollution hotspots
    """

    alerts = []

    # Current AQI alert
    if current_aqi > 150:
        alerts.append({
            "type": "Critical",
            "icon": "🚨",
            "title": "Severe Air Pollution Alert",
            "message": (
                f"Current AQI is {current_aqi}. "
                "Avoid prolonged outdoor activity. Sensitive groups "
                "should remain indoors when possible."
            )
        })

    elif current_aqi > 100:
        alerts.append({
            "type": "Warning",
            "icon": "⚠️",
            "title": "Unhealthy Air Quality",
            "message": (
                f"Current AQI is {current_aqi}. "
                "Children, elderly people, and individuals with "
                "respiratory conditions should reduce outdoor exposure."
            )
        })

    # Forecast alerts
    for period, predicted_aqi in forecasts.items():

        if predicted_aqi > 150:

            alerts.append({
                "type": "Forecast",
                "icon": "📈",
                "title": f"High Pollution Expected - {period}",
                "message": (
                    f"Predicted AQI is {predicted_aqi}. "
                    "Plan outdoor activities carefully and consider "
                    "wearing protective masks in high-traffic areas."
                )
            })

    # Hotspot alerts
    if hotspots:

        hotspot_names = ", ".join(
            hotspot["name"]
            for hotspot in hotspots
        )

        alerts.append({
            "type": "Hotspot",
            "icon": "📍",
            "title": "Pollution Hotspots Detected",
            "message": (
                f"High pollution levels detected in: {hotspot_names}. "
                "Consider avoiding prolonged exposure in these areas."
            )
        })

    # Good air quality message
    if not alerts:

        alerts.append({
            "type": "Safe",
            "icon": "🌿",
            "title": "Air Quality is Stable",
            "message": (
                "No major pollution risks detected at this time. "
                "Outdoor activities can continue normally."
            )
        })

    return alerts


def get_alert_priority(alert_type):
    """
    Return priority level for alert type.
    """

    priorities = {
        "Critical": "High",
        "Warning": "Medium",
        "Forecast": "Medium",
        "Hotspot": "High",
        "Safe": "Low"
    }

    return priorities.get(
        alert_type,
        "Low"
    )