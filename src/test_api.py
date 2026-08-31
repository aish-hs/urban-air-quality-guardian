
from src.api_client import get_live_air_quality


# Bengaluru coordinates
latitude = 12.9716
longitude = 77.5946


data = get_live_air_quality(
    latitude,
    longitude
)


print(data)

