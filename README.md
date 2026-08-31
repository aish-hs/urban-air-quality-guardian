# 🌍 Urban Air Quality Guardian

### AI-Powered Urban Air Monitoring & Public Safety Platform

**Monitor • Analyze • Predict • Protect**

Urban Air Quality Guardian is an AI-powered environmental intelligence platform designed to help citizens monitor air pollution, understand health risks, predict future air quality, identify pollution hotspots, and make safer environmental decisions.

---

## 🚀 Features

### 📊 Real-Time Air Quality Monitoring

* Live air quality data using Open-Meteo Air Quality API
* PM2.5 monitoring
* PM10 monitoring
* NO₂ monitoring
* CO monitoring
* SO₂ monitoring
* Automatic AQI calculation
* AQI visualization using an interactive gauge

### 🤖 AI-Based AQI Prediction

* Machine learning-based air quality forecasting
* Predicts future AQI conditions
* 24-hour forecast
* 48-hour forecast
* 72-hour forecast
* Model performance evaluation using MAE and R² score

### 🗺️ Live Pollution Intelligence Map

* Interactive Bengaluru pollution map
* Location-wise AQI monitoring
* Pollution hotspot detection
* Safe zone identification
* Geographic visualization using Folium

### 🛣️ Safe Route Intelligence

* Route comparison based on pollution exposure
* Average AQI exposure analysis
* Pollution risk estimation
* Safer route recommendation

### 🚨 Smart Air Quality Alerts

* Current AQI alerts
* Predicted pollution alerts
* Pollution hotspot warnings
* Priority-based alert classification

### 🩺 Personalized Health Intelligence

Health recommendations for:

* General public
* Children
* Elderly individuals
* Sensitive groups
* People with respiratory conditions

### 🌱 Eco-Awareness Zone

* Pollution reduction tips
* Weekly eco challenges
* CO₂ reduction tracking
* Eco points system
* Community leaderboard

### 📈 Reports & Insights

* Historical AQI trends
* Pollutant concentration trends
* Location-wise AQI comparison
* Weekly AQI analysis
* Monthly AQI analysis
* Best and worst air quality days
* Downloadable CSV reports

---

# 🏗️ Project Architecture

```text
Open-Meteo Air Quality API
            ↓
      api_client.py
            ↓
     Live Pollutant Data
            ↓
       AQI Calculation
            ↓
 ┌──────────┼───────────┐
 ↓          ↓           ↓
Dashboard  Alerts   Health Analysis
            ↓
      User Intelligence


Historical CSV Dataset
            ↓
     Data Processing
            ↓
   Machine Learning Model
            ↓
       AQI Prediction
            ↓
     Reports & Insights
```

---

# 🛠️ Technology Stack

## Frontend

* Streamlit
* Plotly
* Folium
* Streamlit-Folium

## Backend & Data Processing

* Python
* Pandas
* Requests

## AI & Machine Learning

* Scikit-learn
* Regression Model
* Predictive Analytics

## External API

* Open-Meteo Air Quality API

---

# 📁 Project Structure

```text
urban-air-quality-guardian/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── air_quality_data.csv
│
└── src/
    ├── api_client.py
    ├── aqi_calculator.py
    ├── alert_system.py
    ├── data_processing.py
    ├── eco_awareness.py
    ├── health_advisor.py
    ├── hotspot_detection.py
    ├── map_data.py
    ├── pollutant_analysis.py
    ├── prediction.py
    ├── report_generator.py
    ├── route_analyzer.py
    └── route_data.py
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the project folder

```bash
cd urban-air-quality-guardian
```

## 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 4. Run the application

```bash
python -m streamlit run app.py
```

---

# 🌐 Live Data Integration

The project uses the **Open-Meteo Air Quality API** to fetch live pollutant concentrations.

The application retrieves:

* PM2.5
* PM10
* Nitrogen Dioxide (NO₂)
* Carbon Monoxide (CO)
* Sulphur Dioxide (SO₂)
* Ozone (O₃)

If the live API is unavailable, the application automatically falls back to historical CSV data.

---

# 🤖 Machine Learning

The application includes a machine learning model trained on historical air quality data.

The model is used to:

* Analyze pollutant patterns
* Predict AQI values
* Generate future air quality forecasts
* Evaluate prediction performance

Model evaluation metrics include:

* Mean Absolute Error (MAE)
* R² Score

---

# 🎯 Problem Statement

Urban air pollution is a major public health concern. Citizens often lack easy access to understandable air quality information and do not receive personalized guidance about pollution exposure.

Urban Air Quality Guardian addresses this problem by combining:

* Real-time environmental data
* Artificial Intelligence
* Machine Learning
* Geographic visualization
* Health intelligence
* Community participation

into a single platform.

---

# 🌍 Future Improvements

* Real-time ward-level sensor integration
* GPS-based live safe route navigation
* SMS and push notifications
* User authentication
* Personalized pollution exposure tracking
* Mobile application
* Deep learning-based forecasting
* IoT sensor integration
* Multi-city support
* Government and policymaker dashboards

---

# 👩‍💻 Author

**Aishwarya H S**

---

# 🌱 Vision

> To empower citizens and institutions with intelligent environmental insights that support healthier, safer, and more sustainable urban communities.
