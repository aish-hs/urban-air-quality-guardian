def get_location_data():
    """
    Return demo air quality monitoring data
    for different locations in Bengaluru.
    """

    locations = [
        {
            "name": "Whitefield",
            "latitude": 12.9698,
            "longitude": 77.7500,
            "aqi": 165,
            "pm25": 85,
            "pm10": 140
        },
        {
            "name": "Koramangala",
            "latitude": 12.9352,
            "longitude": 77.6245,
            "aqi": 118,
            "pm25": 58,
            "pm10": 105
        },
        {
            "name": "Indiranagar",
            "latitude": 12.9784,
            "longitude": 77.6408,
            "aqi": 92,
            "pm25": 42,
            "pm10": 80
        },
        {
            "name": "Majestic",
            "latitude": 12.9767,
            "longitude": 77.5713,
            "aqi": 175,
            "pm25": 95,
            "pm10": 150
        },
        {
            "name": "Jayanagar",
            "latitude": 12.9250,
            "longitude": 77.5938,
            "aqi": 75,
            "pm25": 35,
            "pm10": 65
        },
        {
            "name": "Electronic City",
            "latitude": 12.8456,
            "longitude": 77.6603,
            "aqi": 105,
            "pm25": 52,
            "pm10": 95
        }
    ]

    return locations