def get_location_aqi(location_name, locations):
    """
    Get AQI for a specific location.
    """

    for location in locations:

        if location["name"] == location_name:
            return location["aqi"]

    return None


def calculate_route_aqi(route, locations):
    """
    Calculate average AQI exposure
    across a route.
    """

    aqi_values = []

    for location_name in route["locations"]:

        aqi = get_location_aqi(
            location_name,
            locations
        )

        if aqi is not None:
            aqi_values.append(aqi)

    if not aqi_values:
        return 0

    average_aqi = sum(aqi_values) / len(aqi_values)

    return round(average_aqi, 1)


def get_route_risk_level(average_aqi):
    """
    Determine pollution risk level.
    """

    if average_aqi <= 50:
        return "Low"

    elif average_aqi <= 100:
        return "Moderate"

    elif average_aqi <= 150:
        return "High"

    else:
        return "Very High"


def analyze_routes(routes, locations, start, destination):
    """
    Analyze all available routes between
    selected locations.
    """

    available_routes = []

    for route in routes:

        if (
            route["start"] == start
            and route["destination"] == destination
        ):

            average_aqi = calculate_route_aqi(
                route,
                locations
            )

            risk = get_route_risk_level(
                average_aqi
            )

            route_result = {
                "name": route["name"],
                "distance": route["distance"],
                "average_aqi": average_aqi,
                "risk": risk,
                "locations": route["locations"]
            }

            available_routes.append(
                route_result
            )

    return available_routes


def get_safest_route(route_results):
    """
    Find route with lowest pollution exposure.
    """

    if not route_results:
        return None

    safest_route = min(
        route_results,
        key=lambda route: route["average_aqi"]
    )

    return safest_route