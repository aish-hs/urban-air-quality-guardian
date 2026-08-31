POLLUTANT_INFO = {
    "PM2.5": {
        "name": "Fine Particulate Matter",
        "unit": "µg/m³",
        "description": "Tiny particles that can penetrate deep into the lungs."
    },
    "PM10": {
        "name": "Coarse Particulate Matter",
        "unit": "µg/m³",
        "description": "Particles that can cause respiratory irritation."
    },
    "NO2": {
        "name": "Nitrogen Dioxide",
        "unit": "µg/m³",
        "description": "Gas mainly produced by traffic and fuel combustion."
    },
    "CO": {
        "name": "Carbon Monoxide",
        "unit": "mg/m³",
        "description": "Gas produced by incomplete combustion."
    },
    "SO2": {
        "name": "Sulfur Dioxide",
        "unit": "µg/m³",
        "description": "Gas mainly produced by industrial processes."
    }
}


def analyze_pollutants(pollutants):
    """
    Analyze pollutant concentrations and identify
    the dominant pollutant.
    """

    dominant_pollutant = max(
        pollutants,
        key=pollutants.get
    )

    analysis = {}

    for pollutant, value in pollutants.items():

        info = POLLUTANT_INFO.get(
            pollutant,
            {}
        )

        analysis[pollutant] = {
            "value": value,
            "unit": info.get("unit", ""),
            "description": info.get("description", "")
        }

    return {
        "dominant_pollutant": dominant_pollutant,
        "analysis": analysis
    }