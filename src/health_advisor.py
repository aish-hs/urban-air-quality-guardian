def get_health_advice(aqi):
    """
    Generate health recommendations based on AQI level.
    """

    if aqi <= 50:
        return {
            "general": "Air quality is excellent. Outdoor activities are safe.",
            "children": "Children can safely play outdoors.",
            "elderly": "Outdoor activities are safe for elderly individuals.",
            "sensitive": "No special precautions are generally required.",
            "recommendation": "Enjoy outdoor activities and maintain a healthy lifestyle."
        }

    elif aqi <= 100:
        return {
            "general": "Air quality is acceptable for most people.",
            "children": "Sensitive children should take breaks during prolonged outdoor activity.",
            "elderly": "Sensitive elderly individuals should monitor symptoms.",
            "sensitive": "People with respiratory conditions should consider reducing prolonged exertion.",
            "recommendation": "Avoid prolonged outdoor exercise if you experience breathing discomfort."
        }

    elif aqi <= 150:
        return {
            "general": "Most people can continue normal activities but should monitor air quality.",
            "children": "Children should reduce prolonged or heavy outdoor activity.",
            "elderly": "Elderly individuals should limit extended outdoor exposure.",
            "sensitive": "People with asthma or respiratory conditions should avoid prolonged outdoor exposure.",
            "recommendation": "Prefer indoor exercise and avoid high-traffic areas during peak pollution."
        }

    elif aqi <= 200:
        return {
            "general": "Everyone may begin experiencing health effects. Reduce prolonged outdoor activity.",
            "children": "Children should avoid prolonged outdoor activities.",
            "elderly": "Elderly individuals should stay indoors when possible.",
            "sensitive": "People with respiratory or heart conditions should avoid outdoor exertion.",
            "recommendation": "Keep windows closed during peak pollution and consider protective measures outdoors."
        }

    elif aqi <= 300:
        return {
            "general": "Health alert. Avoid unnecessary outdoor activities.",
            "children": "Children should remain indoors as much as possible.",
            "elderly": "Elderly individuals should avoid outdoor exposure.",
            "sensitive": "Sensitive groups should remain indoors and follow medical advice.",
            "recommendation": "Use air filtration indoors and avoid outdoor exercise."
        }

    else:
        return {
            "general": "Health emergency conditions. Avoid outdoor exposure.",
            "children": "Children should remain indoors.",
            "elderly": "Elderly individuals should remain indoors.",
            "sensitive": "Sensitive individuals should avoid any outdoor exposure.",
            "recommendation": "Stay indoors, keep doors and windows closed, and follow local health advisories."
        }