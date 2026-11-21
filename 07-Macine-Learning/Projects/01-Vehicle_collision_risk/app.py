import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load models
knn = joblib.load('model/knn.pkl')
nb = joblib.load('model/naive_bayes.pkl')
dt = joblib.load('model/decision_tree.pkl')
rf = joblib.load('model/random_forest.pkl')

# Load preprocessing objects
encoder = joblib.load('model/encoder.pkl')
scaler = joblib.load('model/scaler.pkl')

# Page configuration
st.set_page_config(
    page_title="Vehicle Collision Prediction",
    page_icon="🚗",
    layout="wide"
)
st.sidebar.title("About the Project")

st.sidebar.write(
    "A Machine Learning project that predicts "
    "vehicle collision risk based on vehicle, "
    "road and environmental conditions."
)

st.sidebar.divider()

st.sidebar.subheader("Available Models")

st.sidebar.write(
    "- K-Nearest Neighbors\n"
    "- Naive Bayes\n"
    "- Decision Tree\n"
    "- Random Forest"
)

# Title
st.title("🚗 Vehicle Collision Risk Prediction")

st.write(
    "Enter the vehicle and road conditions below "
    "to predict the collision risk."
)

st.divider()

# Model selection
model_choice = st.selectbox(
    "Select Machine Learning Model",
    ["Random Forest", "Decision Tree", "KNN", "Naive Bayes"]
)
model_descriptions = {
    "Random Forest": "Uses multiple decision trees to improve prediction stability.",
    "Decision Tree": "Makes predictions using a tree-like sequence of decisions.",
    "KNN": "Predicts risk based on the nearest similar data points.",
    "Naive Bayes": "Uses probability and Bayes' theorem for classification."
}

st.info(model_descriptions[model_choice])

st.divider()
st.subheader("Vehicle Information")

col1, col2 = st.columns(2)

with col1:
    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Car", "Bike", "Bus", "Truck"]
    )

    vehicle_speed = st.number_input(
        "Vehicle Speed (km/h)", min_value=0.0
    )

    vehicle_acceleration = st.number_input(
        "Vehicle Acceleration (m/s²)"
    )

with col2:
    speed_limit = st.number_input(
        "Speed Limit (km/h)", min_value=0.0
    )

    front_distance = st.number_input(
        "Distance from Front Vehicle (m)", min_value=0.0
    )

    front_speed = st.number_input(
        "Front Vehicle Speed (km/h)", min_value=0.0
    )

st.divider()
st.subheader("Road and Environment")

col1, col2 = st.columns(2)

with col1:
    road_type = st.selectbox(
        "Road Type",
        ["Highway", "Urban", "Rural", "Residential"]
    )

    weather = st.selectbox(
        "Weather",
        ["Clear", "Rainy", "Foggy", "Cloudy"]
    )

    road_condition = st.selectbox(
        "Road Condition",
        ["Dry", "Wet", "Icy", "Damaged"]
    )

with col2:
    time_of_day = st.selectbox(
        "Time of Day",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

    visibility = st.number_input(
        "Visibility (km)", min_value=0.0
    )

st.divider()
st.subheader("Traffic Information")

col1, col2 = st.columns(2)

with col1:
    front_acceleration = st.number_input(
        "Front Vehicle Acceleration (m/s²)"
    )

with col2:
    nearby_vehicles = st.number_input(
        "Nearby Vehicle Count", min_value=0, step=1
    )

traffic_density = st.number_input(
    "Traffic Density Index", min_value=0.0
)

st.divider()

predict = st.button("Predict Collision Risk")

if predict:

    new_incident = pd.DataFrame({
        'vehicle_type': [vehicle_type],
        'road_type': [road_type],
        'weather': [weather],
        'road_condition': [road_condition],
        'time_of_day': [time_of_day],
        'vehicle_speed_kmh': [vehicle_speed],
        'speed_limit_kmh': [speed_limit],
        'front_vehicle_distance_m': [front_distance],
        'front_vehicle_speed_kmh': [front_speed],
        'vehicle_acceleration_mps2': [vehicle_acceleration],
        'front_vehicle_acceleration_mps2': [front_acceleration],
        'visibility_km': [visibility],
        'nearby_vehicle_count': [nearby_vehicles],
        'traffic_density_index': [traffic_density]
    })

    st.write("Input received successfully!")
    st.dataframe(new_incident)

    categorical_cols = [
        'vehicle_type',
        'road_type',
        'weather',
        'road_condition',
        'time_of_day'
    ]

    new_incident_encoded = encoder.transform(
        new_incident[categorical_cols]
    )

    new_incident_encoded_df = pd.DataFrame(
        new_incident_encoded,
        columns=encoder.get_feature_names_out(categorical_cols)
    )

    new_incident_numeric = new_incident.drop(
        columns=categorical_cols
    )

    new_incident_combined = pd.concat(
        [new_incident_numeric, new_incident_encoded_df],
        axis=1
    )

    new_incident_final = scaler.transform(new_incident_combined)

    # Select model
    if model_choice == "KNN":
        selected_model = knn
    elif model_choice == "Naive Bayes":
        selected_model = nb
    elif model_choice == "Decision Tree":
        selected_model = dt
    else:
        selected_model = rf

    # Prediction
    prediction = selected_model.predict(new_incident_final)

    st.subheader("Prediction Result")
    if prediction[0] == "High":

        st.error("🔴 HIGH RISK")
    
    elif prediction[0] == "Medium":
        st.warning("🟡 MEDIUM RISK")
    
    else:
        st.success("🟢 LOW RISK")

    # Prediction probabilities
    probabilities = selected_model.predict_proba(new_incident_final)

    probability_df = pd.DataFrame({
        'Risk Category': selected_model.classes_,
        'Probability': probabilities[0] * 100
    })

    # Probability chart
    fig, ax = plt.subplots(figsize=(5, 3))

    bars = ax.bar(
    probability_df['Risk Category'],
    probability_df['Probability']
    )

    ax.bar_label(bars, fmt='%.1f%%', padding=3)

    ax.set_ylabel("Probability (%)")
    ax.set_xlabel("Risk Category")
    ax.set_title("Collision Risk Prediction Probabilities")
    ax.set_ylim(0, 100)
    plt.tight_layout()

    st.pyplot(fig, use_container_width=False)

    st.caption(
    "Disclaimer: This project uses synthetic data for educational purposes. "
    "Predictions should not be used for real-world driving decisions."
    )