
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium

from streamlit_folium import st_folium

from src.aqi_calculator import get_aqi_category
from src.pollutant_analysis import analyze_pollutants
from src.health_advisor import get_health_advice

from src.data_processing import (
    load_air_quality_data,
    get_aqi_statistics,
    get_pollutant_trends
)

from src.prediction import (
    train_prediction_model,
    generate_forecast
)

from src.map_data import get_location_data

from src.hotspot_detection import (
    get_zone_status,
    detect_hotspots
)

from src.route_data import get_routes

from src.route_analyzer import (
    analyze_routes,
    get_safest_route
)

from src.eco_awareness import (
    get_eco_tips,
    get_weekly_challenges,
    get_community_leaderboard
)

from src.alert_system import (
    generate_alerts,
    get_alert_priority
)

from src.report_generator import (
    generate_summary_report,
    generate_location_report,
    generate_trend_report,
    generate_csv_download
)

from src.api_client import get_live_air_quality


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Urban Air Quality Guardian",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #777777;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 650;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .eco-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #dddddd;
        margin-bottom: 15px;
        min-height: 150px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# LOAD HISTORICAL DATA
# ==================================================

@st.cache_data
def load_data():

    df = load_air_quality_data(
        "data/air_quality_data.csv"
    )

    return df


df = load_data()


aqi_stats = get_aqi_statistics(
    df
)


# ==================================================
# TRAIN ML MODEL
# ==================================================

@st.cache_resource
def load_model(data):

    model, mae, r2 = train_prediction_model(
        data
    )

    return model, mae, r2


model, mae, r2 = load_model(
    df
)


# ==================================================
# LIVE AIR QUALITY DATA
# ==================================================

BENGALURU_LATITUDE = 12.9716
BENGALURU_LONGITUDE = 77.5946


@st.cache_data(ttl=600)
def fetch_live_air_quality():

    return get_live_air_quality(
        BENGALURU_LATITUDE,
        BENGALURU_LONGITUDE
    )


live_data = fetch_live_air_quality()


# ==================================================
# PM2.5 TO AQI CALCULATOR
# EPA STYLE APPROXIMATION
# ==================================================

def calculate_pm25_aqi(pm25):

    breakpoints = [

        (0.0, 12.0, 0, 50),

        (12.1, 35.4, 51, 100),

        (35.5, 55.4, 101, 150),

        (55.5, 150.4, 151, 200),

        (150.5, 250.4, 201, 300),

        (250.5, 350.4, 301, 400),

        (350.5, 500.4, 401, 500)

    ]


    for c_low, c_high, i_low, i_high in breakpoints:

        if c_low <= pm25 <= c_high:

            aqi = (
                (i_high - i_low)
                /
                (c_high - c_low)
                *
                (pm25 - c_low)
                +
                i_low
            )

            return round(aqi)


    if pm25 > 500.4:

        return 500


    return 0


# ==================================================
# CURRENT DATA
# ==================================================

latest_data = df.iloc[-1]


# ==================================================
# USE LIVE DATA IF AVAILABLE
# OTHERWISE FALLBACK TO CSV
# ==================================================

if live_data:

    pollutants = {

        "PM2.5": round(
            live_data.get(
                "PM2.5",
                0
            ),
            2
        ),

        "PM10": round(
            live_data.get(
                "PM10",
                0
            ),
            2
        ),

        "NO2": round(
            live_data.get(
                "NO2",
                0
            ),
            2
        ),

        # Open-Meteo CO is returned in µg/m³.
        # Convert to mg/m³ to match the project dataset.
        "CO": round(
            live_data.get(
                "CO",
                0
            )
            /
            1000,
            3
        ),

        "SO2": round(
            live_data.get(
                "SO2",
                0
            ),
            2
        )

    }


    aqi_value = calculate_pm25_aqi(
        pollutants["PM2.5"]
    )


    data_source = "Live Open-Meteo Data"


else:

    pollutants = {

        "PM2.5": latest_data["PM2.5"],

        "PM10": latest_data["PM10"],

        "NO2": latest_data["NO2"],

        "CO": latest_data["CO"],

        "SO2": latest_data["SO2"]

    }


    aqi_value = int(
        latest_data["AQI"]
    )


    data_source = "Historical CSV Fallback"


# ==================================================
# ANALYSIS
# ==================================================

aqi_info = get_aqi_category(
    aqi_value
)


pollutant_results = analyze_pollutants(
    pollutants
)


health_advice = get_health_advice(
    aqi_value
)


# ==================================================
# AI FORECAST
# ==================================================

forecasts = generate_forecast(
    model,
    pollutants
)


# ==================================================
# MAP DATA
# ==================================================

locations = get_location_data()


hotspots = detect_hotspots(
    locations
)


# ==================================================
# ROUTE DATA
# ==================================================

routes = get_routes()


location_names = [

    location["name"]

    for location in locations

]


# ==================================================
# ECO DATA
# ==================================================

eco_tips = get_eco_tips()


weekly_challenges = get_weekly_challenges()


leaderboard = get_community_leaderboard()


# ==================================================
# ALERTS
# ==================================================

alerts = generate_alerts(
    aqi_value,
    forecasts,
    hotspots
)


# ==================================================
# REPORT DATA
# ==================================================

summary_report = generate_summary_report(
    df,
    aqi_stats,
    hotspots,
    forecasts
)


location_report = generate_location_report(
    locations
)


weekly_trend, monthly_trend = generate_trend_report(
    df
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title(
        "🌍 Air Guardian"
    )


    st.caption(
        "AI-Powered Urban Air Intelligence"
    )


    st.divider()


    page = st.radio(

        "Navigation",

        [

            "🏠 Dashboard",

            "🗺️ Live Pollution Map",

            "🤖 Predictions & Alerts",

            "🛣️ Safe Route",

            "🌱 Eco Awareness",

            "📊 Reports & Insights",

            "ℹ️ About Project"

        ]

    )


    st.divider()


    st.caption(
        "Monitor • Analyze • Predict • Protect"
    )


# ==================================================
# HEADER
# ==================================================

st.markdown(
    """
    <div class="main-title">
    🌍 Urban Air Quality Guardian
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="subtitle">
    AI-Powered Urban Air Monitoring & Public Safety Platform
    <br>
    Monitor • Analyze • Predict • Protect
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# DASHBOARD PAGE
# ==================================================

if page == "🏠 Dashboard":

    source_col1, source_col2 = st.columns(
        [4, 1]
    )


    with source_col1:

        st.caption(
            f"📡 Data Source: {data_source}"
        )


    with source_col2:

        if st.button(
            "🔄 Refresh Live Data"
        ):

            fetch_live_air_quality.clear()

            st.rerun()


    st.markdown(
        '<div class="section-title">📊 Current Air Quality</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(
        [1, 1]
    )


    # ----------------------------------------------
    # AQI GAUGE
    # ----------------------------------------------

    with col1:

        gauge = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=aqi_value,

                title={

                    "text":
                    "Current Air Quality Index"

                },

                gauge={

                    "axis": {

                        "range": [0, 500]

                    },

                    "bar": {

                        "color": "darkblue"

                    },

                    "steps": [

                        {

                            "range": [0, 50],

                            "color": "#00E400"

                        },

                        {

                            "range": [50, 100],

                            "color": "#FFFF00"

                        },

                        {

                            "range": [100, 150],

                            "color": "#FF7E00"

                        },

                        {

                            "range": [150, 200],

                            "color": "#FF0000"

                        },

                        {

                            "range": [200, 300],

                            "color": "#8F3F97"

                        },

                        {

                            "range": [300, 500],

                            "color": "#7E0023"

                        }

                    ]

                }

            )

        )


        gauge.update_layout(
            height=350
        )


        st.plotly_chart(
            gauge,
            use_container_width=True
        )


    # ----------------------------------------------
    # AQI SUMMARY
    # ----------------------------------------------

    with col2:

        st.markdown(
            "### Air Quality Summary"
        )


        st.metric(
            "Current AQI",
            aqi_value
        )


        st.metric(
            "Status",
            f"{aqi_info['emoji']} "
            f"{aqi_info['category']}"
        )


        st.metric(
            "30-Day Historical Average AQI",
            round(
                aqi_stats["average_aqi"],
                2
            )
        )


        st.info(
            aqi_info["description"]
        )


    # ----------------------------------------------
    # LIVE POLLUTANTS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        '<div class="section-title">🧪 Current Pollutant Concentrations</div>',
        unsafe_allow_html=True
    )


    pollutant_columns = st.columns(
        5
    )


    for index, (
        pollutant,
        data
    ) in enumerate(

        pollutant_results[
            "analysis"
        ].items()

    ):

        with pollutant_columns[index]:

            st.metric(

                pollutant,

                f"{data['value']} "
                f"{data['unit']}"

            )


    # ----------------------------------------------
    # DOMINANT POLLUTANT
    # ----------------------------------------------

    st.divider()


    dominant = pollutant_results[
        "dominant_pollutant"
    ]


    dominant_data = pollutant_results[
        "analysis"
    ][dominant]


    st.markdown(
        '<div class="section-title">⚠️ Dominant Pollutant Intelligence</div>',
        unsafe_allow_html=True
    )


    st.warning(
        f"""
        **{dominant}**

        {dominant_data['description']}

        Current concentration:
        **{dominant_data['value']} {dominant_data['unit']}**
        """
    )


    # ----------------------------------------------
    # HEALTH INTELLIGENCE
    # ----------------------------------------------

    st.divider()


    st.markdown(
        '<div class="section-title">🩺 Personalized Health Intelligence</div>',
        unsafe_allow_html=True
    )


    health_col1, health_col2 = st.columns(
        2
    )


    with health_col1:

        st.markdown(
            "#### 👥 General Public"
        )


        st.info(
            health_advice["general"]
        )


        st.markdown(
            "#### 👶 Children"
        )


        st.warning(
            health_advice["children"]
        )


    with health_col2:

        st.markdown(
            "#### 👴 Elderly"
        )


        st.warning(
            health_advice["elderly"]
        )


        st.markdown(
            "#### 🫁 Sensitive Groups"
        )


        st.error(
            health_advice["sensitive"]
        )


    st.success(
        f"""
        💡 **Recommended Action**

        {health_advice['recommendation']}
        """
    )


# ==================================================
# LIVE POLLUTION MAP PAGE
# ==================================================

elif page == "🗺️ Live Pollution Map":

    st.markdown(
        '<div class="section-title">🗺️ Bengaluru Pollution Intelligence Map</div>',
        unsafe_allow_html=True
    )


    st.caption(
        """
        Location-level AQI monitoring with
        safe zones and pollution hotspots.
        """
    )


    map_center = [

        12.9716,

        77.5946

    ]


    pollution_map = folium.Map(

        location=map_center,

        zoom_start=11

    )


    for location in locations:

        zone = get_zone_status(
            location["aqi"]
        )


        popup_text = f"""
        <b>📍 {location['name']}</b><br><br>

        AQI: <b>{location['aqi']}</b><br>

        Status: <b>{zone['status']}</b><br>

        Risk Level: <b>{zone['risk']}</b><br><br>

        PM2.5: {location['pm25']} µg/m³<br>

        PM10: {location['pm10']} µg/m³
        """


        folium.CircleMarker(

            location=[

                location["latitude"],

                location["longitude"]

            ],

            radius=14,

            popup=folium.Popup(

                popup_text,

                max_width=300

            ),

            color=zone["color"],

            fill=True,

            fill_color=zone["color"],

            fill_opacity=0.75

        ).add_to(
            pollution_map
        )


    st_folium(

        pollution_map,

        width=None,

        height=600

    )


    # ----------------------------------------------
    # HOTSPOTS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        '<div class="section-title">🔴 Pollution Hotspots</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(
        2
    )


    with col1:

        st.metric(

            "Hotspots Detected",

            len(hotspots)

        )


    with col2:

        safe_locations = [

            location

            for location in locations

            if location["aqi"] <= 100

        ]


        st.metric(

            "Safer Locations",

            len(safe_locations)

        )


    for hotspot in hotspots:

        st.error(
            f"""
            🔴 **{hotspot['name']}**

            AQI: **{hotspot['aqi']}**

            PM2.5: **{hotspot['pm25']} µg/m³**

            PM10: **{hotspot['pm10']} µg/m³**

            Avoid prolonged outdoor exposure
            in this area.
            """
        )


# ==================================================
# PREDICTIONS & ALERTS PAGE
# ==================================================

elif page == "🤖 Predictions & Alerts":

    st.markdown(
        '<div class="section-title">🤖 AI Air Quality Forecast</div>',
        unsafe_allow_html=True
    )


    st.caption(
        """
        Machine learning predictions for
        upcoming air quality conditions.
        """
    )


    forecast_cols = st.columns(
        len(forecasts)
    )


    for index, (
        period,
        prediction
    ) in enumerate(
        forecasts.items()
    ):

        prediction_info = get_aqi_category(
            prediction
        )


        with forecast_cols[index]:

            st.metric(

                period,

                f"AQI {prediction}"

            )


            st.write(
                f"{prediction_info['emoji']} "
                f"{prediction_info['category']}"
            )


    # ----------------------------------------------
    # MODEL PERFORMANCE
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 🧠 Prediction Model Performance"
    )


    model_col1, model_col2 = st.columns(
        2
    )


    with model_col1:

        st.metric(

            "Mean Absolute Error",

            round(mae, 2)

        )


    with model_col2:

        st.metric(

            "R² Score",

            round(r2, 3)

        )


    # ----------------------------------------------
    # ALERTS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        '<div class="section-title">🚨 Smart Air Quality Alerts</div>',
        unsafe_allow_html=True
    )


    for alert in alerts:

        priority = get_alert_priority(
            alert["type"]
        )


        message = (

            f"{alert['icon']} "
            f"**{alert['title']}** "
            f"({priority} Priority)\n\n"

            f"{alert['message']}"

        )


        if priority == "High":

            st.error(
                message
            )


        elif priority == "Medium":

            st.warning(
                message
            )


        else:

            st.success(
                message
            )


# ==================================================
# SAFE ROUTE PAGE
# ==================================================

elif page == "🛣️ Safe Route":

    st.markdown(
        '<div class="section-title">🛣️ Safe Route Intelligence</div>',
        unsafe_allow_html=True
    )


    st.caption(
        """
        Choose routes with lower estimated
        pollution exposure.
        """
    )


    route_col1, route_col2, route_col3 = st.columns(
        3
    )


    with route_col1:

        selected_start = st.selectbox(

            "Starting Location",

            location_names

        )


    with route_col2:

        destination_options = [

            name

            for name in location_names

            if name != selected_start

        ]


        selected_destination = st.selectbox(

            "Destination",

            destination_options

        )


    with route_col3:

        travel_mode = st.selectbox(

            "Travel Mode",

            [

                "🚶 Walking",

                "🚴 Cycling",

                "🚗 Driving"

            ]

        )


    route_results = analyze_routes(

        routes,

        locations,

        selected_start,

        selected_destination

    )


    if route_results:

        safest_route = get_safest_route(
            route_results
        )


        st.success(
            f"""
            🟢 **Recommended Safest Route**

            **{safest_route['name']}**

            Distance:
            **{safest_route['distance']} km**

            Average AQI Exposure:
            **{safest_route['average_aqi']}**

            Pollution Risk:
            **{safest_route['risk']}**

            Route:
            **{" → ".join(safest_route['locations'])}**
            """
        )


        route_df = pd.DataFrame(
            route_results
        )


        st.markdown(
            "### Route Comparison"
        )


        st.dataframe(

            route_df[

                [

                    "name",

                    "distance",

                    "average_aqi",

                    "risk"

                ]

            ],

            use_container_width=True,

            hide_index=True

        )


        route_chart = px.bar(

            route_df,

            x="name",

            y="average_aqi",

            text="average_aqi",

            title="Pollution Exposure by Route"

        )


        route_chart.update_traces(
            textposition="outside"
        )


        st.plotly_chart(

            route_chart,

            use_container_width=True

        )


    else:

        st.info(
            """
            No predefined route exists for this
            location combination.

            Try:

            • Whitefield → Jayanagar

            • Whitefield → Majestic

            • Indiranagar → Electronic City
            """
        )


# ==================================================
# ECO AWARENESS PAGE
# ==================================================

elif page == "🌱 Eco Awareness":

    st.markdown(
        '<div class="section-title">🌱 Eco-Awareness Zone</div>',
        unsafe_allow_html=True
    )


    st.caption(
        """
        Learn, participate, and contribute
        towards cleaner cities.
        """
    )


    # ----------------------------------------------
    # ECO TIPS
    # ----------------------------------------------

    st.markdown(
        "### 💡 Eco Tips"
    )


    tip_columns = st.columns(
        3
    )


    for index, tip in enumerate(
        eco_tips
    ):

        with tip_columns[index % 3]:

            st.markdown(

                f"""
                <div class="eco-card">

                <h3>
                {tip['icon']} {tip['title']}
                </h3>

                <p>
                {tip['description']}
                </p>

                </div>
                """,

                unsafe_allow_html=True

            )


    # ----------------------------------------------
    # CHALLENGES
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 🎯 Weekly Eco Challenges"
    )


    for challenge in weekly_challenges:

        progress_percentage = (

            challenge["progress"]

            /

            challenge["goal"]

        )


        st.markdown(
            f"#### {challenge['icon']} "
            f"{challenge['title']}"
        )


        st.write(
            challenge["description"]
        )


        st.progress(

            min(
                progress_percentage,
                1.0
            )

        )


        col1, col2, col3 = st.columns(
            3
        )


        with col1:

            st.metric(

                "Progress",

                f"{challenge['progress']} "
                f"/ {challenge['goal']}"

            )


        with col2:

            st.metric(

                "CO₂ Saved",

                f"{challenge['co2_saved']} kg"

            )


        with col3:

            st.metric(

                "Eco Points",

                challenge["points"]

            )


    # ----------------------------------------------
    # LEADERBOARD
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 🏆 Community Eco Leaderboard"
    )


    leaderboard_df = pd.DataFrame(
        leaderboard
    )


    leaderboard_df["rank"] = (

        leaderboard_df["rank"]

        .apply(

            lambda rank:

            "🥇" if rank == 1

            else "🥈" if rank == 2

            else "🥉" if rank == 3

            else f"#{rank}"

        )

    )


    leaderboard_df.columns = [

        "Rank",

        "Community Member",

        "Eco Points",

        "CO₂ Saved (kg)"

    ]


    st.dataframe(

        leaderboard_df,

        use_container_width=True,

        hide_index=True

    )


# ==================================================
# REPORTS & INSIGHTS PAGE
# ==================================================

elif page == "📊 Reports & Insights":

    st.markdown(
        '<div class="section-title">📊 Reports & Insights</div>',
        unsafe_allow_html=True
    )


    st.caption(
        """
        Data-driven environmental intelligence
        for analysis and decision-making.
        """
    )


    # ----------------------------------------------
    # SUMMARY REPORT
    # ----------------------------------------------

    st.markdown(
        "### 📋 Air Quality Summary"
    )


    summary_df = pd.DataFrame(

        list(summary_report.items()),

        columns=[

            "Metric",

            "Value"

        ]

    )


    st.dataframe(

        summary_df,

        use_container_width=True,

        hide_index=True

    )


    # ----------------------------------------------
    # HISTORICAL AQI TREND
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 📈 Historical AQI Trend"
    )


    fig_aqi = px.line(

        df,

        x="Date",

        y="AQI",

        markers=True,

        title="Historical AQI Trend"

    )


    st.plotly_chart(

        fig_aqi,

        use_container_width=True

    )


    # ----------------------------------------------
    # POLLUTANT TRENDS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 🧪 Pollutant Trends"
    )


    pollutant_trends = get_pollutant_trends(
        df
    )


    fig_pollutants = px.line(

        pollutant_trends,

        x="Date",

        y=[

            "PM2.5",

            "PM10",

            "NO2",

            "CO",

            "SO2"

        ],

        title="Pollutant Concentration Trends"

    )


    st.plotly_chart(

        fig_pollutants,

        use_container_width=True

    )


    # ----------------------------------------------
    # LOCATION COMPARISON
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 📍 Location Comparison"
    )


    location_chart = px.bar(

        location_report,

        x="Location",

        y="AQI",

        text="AQI",

        title="AQI Across Bengaluru Locations"

    )


    location_chart.update_traces(
        textposition="outside"
    )


    st.plotly_chart(

        location_chart,

        use_container_width=True

    )


    # ----------------------------------------------
    # WEEKLY TREND
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 📅 Weekly AQI Trend"
    )


    weekly_chart = px.line(

        weekly_trend,

        x="Week",

        y="AQI",

        markers=True,

        title="Average Weekly AQI"

    )


    st.plotly_chart(

        weekly_chart,

        use_container_width=True

    )


    # ----------------------------------------------
    # MONTHLY TREND
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 📆 Monthly AQI Trend"
    )


    monthly_chart = px.bar(

        monthly_trend,

        x="Date",

        y="AQI",

        text="AQI",

        title="Average Monthly AQI"

    )


    monthly_chart.update_traces(
        textposition="outside"
    )


    st.plotly_chart(

        monthly_chart,

        use_container_width=True

    )


    # ----------------------------------------------
    # BEST & WORST DAYS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### 🏆 Best & Worst Air Quality Days"
    )


    col1, col2 = st.columns(
        2
    )


    with col1:

        st.success(
            f"""
            🌿 **Best Air Quality Day**

            Date:
            **{aqi_stats['best_date'].strftime('%d %B %Y')}**

            AQI:
            **{aqi_stats['minimum_aqi']}**
            """
        )


    with col2:

        st.error(
            f"""
            🚨 **Worst Air Quality Day**

            Date:
            **{aqi_stats['worst_date'].strftime('%d %B %Y')}**

            AQI:
            **{aqi_stats['maximum_aqi']}**
            """
        )


    # ----------------------------------------------
    # DOWNLOAD REPORTS
    # ----------------------------------------------

    st.divider()


    st.markdown(
        "### ⬇️ Download Reports"
    )


    download_col1, download_col2 = st.columns(
        2
    )


    with download_col1:

        st.download_button(

            label="📥 Download Air Quality Dataset",

            data=generate_csv_download(
                df
            ),

            file_name=(
                "urban_air_quality_report.csv"
            ),

            mime="text/csv"

        )


    with download_col2:

        st.download_button(

            label="📥 Download Location AQI Report",

            data=generate_csv_download(
                location_report
            ),

            file_name=(
                "bengaluru_location_aqi_report.csv"
            ),

            mime="text/csv"

        )


# ==================================================
# ABOUT PROJECT PAGE
# ==================================================

elif page == "ℹ️ About Project":

    st.markdown(
        '<div class="section-title">ℹ️ About Urban Air Quality Guardian</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        """
        ### 🌍 Our Mission

        Urban Air Quality Guardian is an AI-powered
        environmental intelligence platform designed to help
        citizens understand and respond to urban air pollution.

        The platform combines live air quality data,
        historical analysis, machine learning predictions,
        geographic intelligence, public health recommendations,
        and community participation.
        """
    )


    st.divider()


    st.markdown(
        "### 🚀 Key Features"
    )


    features = [

        "🌐 Live air quality data integration",

        "📊 AQI monitoring and visualization",

        "🧪 Pollutant concentration analysis",

        "🤖 Machine learning AQI prediction",

        "🗺️ Interactive pollution intelligence maps",

        "🔴 Pollution hotspot detection",

        "🛣️ Safe route recommendation",

        "🚨 Smart pollution alerts",

        "🩺 Personalized health recommendations",

        "🌱 Eco-awareness challenges",

        "🏆 Community leaderboard",

        "📄 Environmental reports and downloads"

    ]


    for feature in features:

        st.write(
            feature
        )


    st.divider()


    st.markdown(
        "### 🛠️ Technology Stack"
    )


    tech_col1, tech_col2, tech_col3 = st.columns(
        3
    )


    with tech_col1:

        st.markdown(
            """
            **Frontend**

            - Streamlit
            - Plotly
            - Folium
            """
        )


    with tech_col2:

        st.markdown(
            """
            **Backend & Data**

            - Python
            - Pandas
            - Requests
            - Open-Meteo API
            """
        )


    with tech_col3:

        st.markdown(
            """
            **AI / ML**

            - Scikit-learn
            - Regression Model
            - Predictive Analytics
            """
        )


    st.divider()


    st.success(
        """
        🌱 **Vision**

        To empower citizens and institutions with intelligent
        environmental insights that support healthier,
        safer, and more sustainable urban communities.
        """
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()


st.caption(
    """
    🌍 Urban Air Quality Guardian |
    Monitor • Analyze • Predict • Protect
    """
)

