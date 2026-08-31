def get_zone_status(aqi):
    """
    Classify a location based on AQI.
    """

    if aqi <= 50:
        return {
            "status": "Safe Zone",
            "color": "green",
            "risk": "Low"
        }

    elif aqi <= 100:
        return {
            "status": "Moderate Zone",
            "color": "orange",
            "risk": "Moderate"
        }

    elif aqi <= 150:
        return {
            "status": "High Pollution Zone",
            "color": "darkorange",
            "risk": "High"
        }

    else:
        return {
            "status": "Pollution Hotspot",
            "color": "red",
            "risk": "Very High"
        }


def detect_hotspots(locations):
    """
    Detect locations with high pollution.
    """

    hotspots = []

    for location in locations:

        if location["aqi"] > 150:
            hotspots.append(location)

    return hotspots