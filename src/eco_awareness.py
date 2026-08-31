def get_eco_tips():
    """
    Return environmental awareness tips.
    """

    return [
        {
            "title": "Use Public Transport",
            "description": (
                "Choose buses or metro whenever possible to reduce "
                "vehicle emissions and traffic pollution."
            ),
            "icon": "🚌"
        },
        {
            "title": "Walk Short Distances",
            "description": (
                "Walking short distances instead of driving helps reduce "
                "urban pollution and improves personal health."
            ),
            "icon": "🚶"
        },
        {
            "title": "Choose Cycling",
            "description": (
                "Cycling produces zero direct emissions and helps "
                "reduce your carbon footprint."
            ),
            "icon": "🚴"
        },
        {
            "title": "Save Electricity",
            "description": (
                "Reducing unnecessary electricity consumption can lower "
                "indirect emissions from energy generation."
            ),
            "icon": "🔌"
        },
        {
            "title": "Plant and Protect Trees",
            "description": (
                "Trees help improve urban environments and support "
                "better long-term air quality."
            ),
            "icon": "🌳"
        }
    ]


def get_weekly_challenges():
    """
    Return demo weekly environmental challenges.
    """

    return [
        {
            "title": "Public Transport Challenge",
            "description": "Use public transport 5 times this week.",
            "goal": 5,
            "progress": 3,
            "co2_saved": 4.2,
            "points": 100,
            "icon": "🚌"
        },
        {
            "title": "Car-Free Day Challenge",
            "description": "Avoid using a private vehicle for one full day.",
            "goal": 1,
            "progress": 1,
            "co2_saved": 2.5,
            "points": 80,
            "icon": "🚶"
        },
        {
            "title": "Cycling Challenge",
            "description": "Cycle for at least 10 kilometers this week.",
            "goal": 10,
            "progress": 6,
            "co2_saved": 1.8,
            "points": 70,
            "icon": "🚴"
        }
    ]


def get_community_leaderboard():
    """
    Return demo community environmental leaderboard.
    """

    return [
        {
            "rank": 1,
            "user": "GreenHero",
            "points": 850,
            "co2_saved": 42
        },
        {
            "rank": 2,
            "user": "EcoWarrior",
            "points": 720,
            "co2_saved": 36
        },
        {
            "rank": 3,
            "user": "CleanAirFan",
            "points": 650,
            "co2_saved": 31
        },
        {
            "rank": 4,
            "user": "EarthGuardian",
            "points": 540,
            "co2_saved": 25
        },
        {
            "rank": 5,
            "user": "GreenCitizen",
            "points": 460,
            "co2_saved": 20
        }
    ]