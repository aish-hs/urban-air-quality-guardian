def get_routes():
    """
    Demo routes between Bengaluru locations.

    Each route contains:
    - route name
    - start location
    - destination
    - distance
    - locations covered
    """

    routes = [
        {
            "name": "Route A - Central Corridor",
            "start": "Whitefield",
            "destination": "Jayanagar",
            "distance": 22,
            "locations": [
                "Whitefield",
                "Indiranagar",
                "Koramangala",
                "Jayanagar"
            ]
        },
        {
            "name": "Route B - Outer Corridor",
            "start": "Whitefield",
            "destination": "Jayanagar",
            "distance": 28,
            "locations": [
                "Whitefield",
                "Electronic City",
                "Jayanagar"
            ]
        },
        {
            "name": "Route A - City Corridor",
            "start": "Whitefield",
            "destination": "Majestic",
            "distance": 19,
            "locations": [
                "Whitefield",
                "Indiranagar",
                "Majestic"
            ]
        },
        {
            "name": "Route B - Alternative Corridor",
            "start": "Whitefield",
            "destination": "Majestic",
            "distance": 23,
            "locations": [
                "Whitefield",
                "Koramangala",
                "Majestic"
            ]
        },
        {
            "name": "Route A - Southern Route",
            "start": "Indiranagar",
            "destination": "Electronic City",
            "distance": 18,
            "locations": [
                "Indiranagar",
                "Koramangala",
                "Electronic City"
            ]
        },
        {
            "name": "Route B - Central Route",
            "start": "Indiranagar",
            "destination": "Electronic City",
            "distance": 22,
            "locations": [
                "Indiranagar",
                "Majestic",
                "Electronic City"
            ]
        }
    ]

    return routes