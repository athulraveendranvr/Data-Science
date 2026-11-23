import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Vehicle Collision Risk Prediction",
    page_icon="🚗",
    layout="wide"
)

st.title("Vehicle Collision Risk Prediction")
st.write(
    "Predict the collision-risk category of a driving scenario "
    "using vehicle, road, traffic and environmental conditions."
)


# ---------------------------------------------------------
# Dataset and feature configuration
# ---------------------------------------------------------
DATA_FILE = "Vehicle_crash_risk.csv"

categorical_cols = [
    "vehicle_type",
    "road_type",
    "weather",
    "road_condition",
    "time_of_day"
]

numerical_cols = [
    "vehicle_speed_kmh",
    "speed_limit_kmh",
    "front_vehicle_distance_m",
    "front_vehicle_speed_kmh",
    "vehicle_acceleration_mps2",
    "front_vehicle_acceleration_mps2",
    "visibility_km",
    "nearby_vehicle_count",
    "traffic_density_index"
]

target_col = "collision_risk"

model_descriptions = {
    "KNN": "K-Nearest Neighbors predicts the risk category using nearby, similar training examples.",
    "Naive Bayes": "Naive Bayes uses probability and Bayes' theorem to classify the driving scenario.",
    "Decision Tree": "Decision Tree makes a prediction through a sequence of feature-based decisions.",
    "Random Forest": "Random Forest combines multiple decision trees to produce a more stable prediction."
}


# ---------------------------------------------------------
# Train models once and cache them
# ---------------------------------------------------------
@st.cache_resource
def train_models():
    data = pd.read_csv(DATA_FILE)

    required_cols = categorical_cols + numerical_cols + [target_col]
    missing_cols = [col for col in required_cols if col not in data.columns]

    if missing_cols:
        raise ValueError(
            "The dataset is missing these required columns: "
            + ", ".join(missing_cols)
        )

    # Keep only the features used by the models and the target.
    data = data[required_cols].copy()

    # Separate features and target.
    X = data[categorical_cols + numerical_cols].copy()
    y = data[target_col].copy()

    # Split before fitting preprocessing objects to avoid data leakage.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Handle missing values using statistics calculated from training data.
    categorical_fill_values = {}
    for col in categorical_cols:
        mode_values = X_train[col].mode(dropna=True)
        fill_value = mode_values.iloc[0] if not mode_values.empty else "Unknown"
        categorical_fill_values[col] = fill_value
        X_train.loc[:, col] = X_train[col].fillna(fill_value)
        X_test.loc[:, col] = X_test[col].fillna(fill_value)

    numerical_fill_values = {}
    for col in numerical_cols:
        fill_value = X_train[col].median()
        numerical_fill_values[col] = fill_value
        X_train.loc[:, col] = X_train[col].fillna(fill_value)
        X_test.loc[:, col] = X_test[col].fillna(fill_value)

    # One-Hot Encode categorical features.
    encoder = OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False
    )

    train_encoded = encoder.fit_transform(X_train[categorical_cols])
    test_encoded = encoder.transform(X_test[categorical_cols])

    encoded_cols = encoder.get_feature_names_out(categorical_cols)

    train_encoded_df = pd.DataFrame(
        train_encoded,
        columns=encoded_cols,
        index=X_train.index
    )

    test_encoded_df = pd.DataFrame(
        test_encoded,
        columns=encoded_cols,
        index=X_test.index
    )

    # Combine numerical and encoded categorical features in a fixed order.
    X_train_combined = pd.concat(
        [X_train[numerical_cols], train_encoded_df],
        axis=1
    )

    X_test_combined = pd.concat(
        [X_test[numerical_cols], test_encoded_df],
        axis=1
    )

    # Scale the complete feature matrix using training data only.
    scaler = MinMaxScaler()
    X_train_final = scaler.fit_transform(X_train_combined)
    X_test_final = scaler.transform(X_test_combined)

    # Initialize and train the four classifiers.
    models = {
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Naive Bayes": GaussianNB(),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
    }

    model_metrics = {}

    for name, model in models.items():
        model.fit(X_train_final, y_train)
        predictions = model.predict(X_test_final)

        model_metrics[name] = {
            "accuracy": accuracy_score(y_test, predictions),
            "report": classification_report(
                y_test,
                predictions,
                output_dict=True,
                zero_division=0
            ),
            "confusion_matrix": confusion_matrix(
                y_test,
                predictions,
                labels=model.classes_
            ),
            "classes": model.classes_
        }

    return (
        models,
        encoder,
        scaler,
        categorical_fill_values,
        numerical_fill_values,
        encoded_cols,
        model_metrics,
        data
    )


# ---------------------------------------------------------
# Load and train
# ---------------------------------------------------------
try:
    (
        models,
        encoder,
        scaler,
        categorical_fill_values,
        numerical_fill_values,
        encoded_cols,
        model_metrics,
        data
    ) = train_models()

except FileNotFoundError:
    st.error(
        f"Could not find '{DATA_FILE}'. Keep the CSV file in the same "
        "folder as app.py."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to prepare the dataset or train the models: {error}")
    st.stop()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
st.sidebar.title("About the Project")
st.sidebar.write(
    "A Machine Learning classification project that predicts "
    "vehicle collision risk from driving and environmental conditions."
)

st.sidebar.divider()
st.sidebar.subheader("Available Models")
st.sidebar.write(
    "- K-Nearest Neighbors\n"
    "- Naive Bayes\n"
    "- Decision Tree\n"
    "- Random Forest"
)

st.sidebar.caption(
    f"Training dataset: {len(data):,} records"
)


# ---------------------------------------------------------
# Model selection
# ---------------------------------------------------------
st.subheader("Choose a Machine Learning Model")

model_choice = st.selectbox(
    "Select model",
    ["Random Forest", "Decision Tree", "KNN", "Naive Bayes"]
)

st.info(model_descriptions[model_choice])


# ---------------------------------------------------------
# Input form
# ---------------------------------------------------------
st.subheader("Enter Driving Scenario Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Vehicle and Road Conditions")

    vehicle_type = st.selectbox(
        "Vehicle type",
        sorted(data["vehicle_type"].dropna().unique().tolist()),
        index=0
    )

    road_type = st.selectbox(
        "Road type",
        sorted(data["road_type"].dropna().unique().tolist()),
        index=0
    )

    road_condition = st.selectbox(
        "Road condition",
        sorted(data["road_condition"].dropna().unique().tolist()),
        index=0
    )

    weather = st.selectbox(
        "Weather",
        sorted(data["weather"].dropna().unique().tolist()),
        index=0
    )

    time_of_day = st.selectbox(
        "Time of day",
        sorted(data["time_of_day"].dropna().unique().tolist()),
        index=0
    )

with col2:
    st.markdown("#### Driving Measurements")

    vehicle_speed = st.number_input(
        "Vehicle speed (km/h)",
        min_value=0.0,
        max_value=250.0,
        value=float(data["vehicle_speed_kmh"].median()),
        step=1.0
    )

    speed_limit = st.number_input(
        "Speed limit (km/h)",
        min_value=0.0,
        max_value=250.0,
        value=float(data["speed_limit_kmh"].median()),
        step=1.0
    )

    front_distance = st.number_input(
        "Distance to front vehicle (m)",
        min_value=0.0,
        max_value=500.0,
        value=float(data["front_vehicle_distance_m"].median()),
        step=1.0
    )

    front_speed = st.number_input(
        "Front vehicle speed (km/h)",
        min_value=0.0,
        max_value=250.0,
        value=float(data["front_vehicle_speed_kmh"].median()),
        step=1.0
    )

    vehicle_acceleration = st.number_input(
        "Vehicle acceleration (m/s²)",
        min_value=-15.0,
        max_value=15.0,
        value=float(data["vehicle_acceleration_mps2"].median()),
        step=0.1
    )

    front_acceleration = st.number_input(
        "Front vehicle acceleration (m/s²)",
        min_value=-15.0,
        max_value=15.0,
        value=float(data["front_vehicle_acceleration_mps2"].median()),
        step=0.1
    )

    visibility = st.number_input(
        "Visibility (km)",
        min_value=0.0,
        max_value=30.0,
        value=float(data["visibility_km"].median()),
        step=0.1
    )

    nearby_vehicles = st.number_input(
        "Nearby vehicle count",
        min_value=0,
        max_value=100,
        value=int(round(data["nearby_vehicle_count"].median())),
        step=1
    )

    traffic_density = st.number_input(
        "Traffic density index",
        min_value=0.0,
        max_value=10.0,
        value=float(data["traffic_density_index"].median()),
        step=0.1
    )


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------
if st.button("Predict Collision Risk", type="primary"):

    new_incident = pd.DataFrame({
        "vehicle_type": [vehicle_type],
        "road_type": [road_type],
        "weather": [weather],
        "road_condition": [road_condition],
        "time_of_day": [time_of_day],
        "vehicle_speed_kmh": [vehicle_speed],
        "speed_limit_kmh": [speed_limit],
        "front_vehicle_distance_m": [front_distance],
        "front_vehicle_speed_kmh": [front_speed],
        "vehicle_acceleration_mps2": [vehicle_acceleration],
        "front_vehicle_acceleration_mps2": [front_acceleration],
        "visibility_km": [visibility],
        "nearby_vehicle_count": [nearby_vehicles],
        "traffic_density_index": [traffic_density]
    })

    # Apply the same missing-value replacements used during training.
    for col in categorical_cols:
        new_incident[col] = new_incident[col].fillna(
            categorical_fill_values[col]
        )

    for col in numerical_cols:
        new_incident[col] = new_incident[col].fillna(
            numerical_fill_values[col]
        )

    # Transform categorical inputs with the fitted encoder.
    new_encoded = encoder.transform(new_incident[categorical_cols])

    new_encoded_df = pd.DataFrame(
        new_encoded,
        columns=encoded_cols
    )

    # Combine features in exactly the same order as the training data.
    new_numeric = new_incident[numerical_cols].reset_index(drop=True)

    new_incident_combined = pd.concat(
        [new_numeric, new_encoded_df],
        axis=1
    )

    # Scale using the already-fitted scaler.
    new_incident_final = scaler.transform(new_incident_combined)

    selected_model = models[model_choice]

    prediction = selected_model.predict(new_incident_final)
    probabilities = selected_model.predict_proba(new_incident_final)

    st.divider()
    st.subheader("Prediction Result")

    predicted_risk = prediction[0]

    if predicted_risk == "High":
        st.error("HIGH RISK")
    elif predicted_risk == "Medium":
        st.warning("MEDIUM RISK")
    else:
        st.success("LOW RISK")

    st.write(f"Selected model: **{model_choice}**")

    # Display predicted class probabilities.
    probability_df = pd.DataFrame({
        "Risk Category": selected_model.classes_,
        "Probability": probabilities[0] * 100
    }).sort_values("Probability", ascending=False)

    st.subheader("Prediction Probabilities")

    fig, ax = plt.subplots(figsize=(6, 3.5))
    bars = ax.bar(
        probability_df["Risk Category"],
        probability_df["Probability"]
    )
    ax.bar_label(bars, fmt="%.1f%%", padding=3)
    ax.set_ylabel("Probability (%)")
    ax.set_xlabel("Risk Category")
    ax.set_title("Collision Risk Prediction Probabilities")
    ax.set_ylim(0, 110)
    plt.tight_layout()

    st.pyplot(fig, use_container_width=False)
    plt.close(fig)

    with st.expander("View input scenario"):
        st.dataframe(new_incident, use_container_width=True)

    st.caption(
        "Disclaimer: This project uses synthetic data for educational "
        "purposes. Predictions are not based on verified real-world accident "
        "records and must not be used for real-world driving decisions."
    )


# ---------------------------------------------------------
# Model evaluation
# ---------------------------------------------------------
st.divider()
with st.expander("View model evaluation results"):
    st.write(
        "The following scores are calculated on the held-out test set. "
        "Because the target classes are imbalanced, accuracy should not "
        "be considered on its own."
    )

    evaluation_rows = []
    for name, results in model_metrics.items():
        evaluation_rows.append({
            "Model": name,
            "Accuracy": results["accuracy"]
        })

    evaluation_df = pd.DataFrame(evaluation_rows)
    evaluation_df["Accuracy"] = evaluation_df["Accuracy"].map(
        lambda value: f"{value:.3f}"
    )
    st.dataframe(evaluation_df, hide_index=True, use_container_width=True)

    selected_eval_model = st.selectbox(
        "Choose a model to inspect its classification report",
        list(models.keys()),
        key="evaluation_model"
    )

    report_df = pd.DataFrame(
        model_metrics[selected_eval_model]["report"]
    ).transpose()

    st.write("Classification Report")
    st.dataframe(report_df.round(3), use_container_width=True)

    st.write("Confusion Matrix")
    cm = model_metrics[selected_eval_model]["confusion_matrix"]
    class_labels = model_metrics[selected_eval_model]["classes"]

    fig_cm, ax_cm = plt.subplots(figsize=(5, 4))
    image = ax_cm.imshow(cm, interpolation="nearest")
    ax_cm.figure.colorbar(image, ax=ax_cm)

    ax_cm.set(
        xticks=range(len(class_labels)),
        yticks=range(len(class_labels)),
        xticklabels=class_labels,
        yticklabels=class_labels,
        xlabel="Predicted Values",
        ylabel="Actual Values",
        title=f"{selected_eval_model} Confusion Matrix"
    )

    threshold = cm.max() / 2 if cm.size else 0
    for row in range(cm.shape[0]):
        for col in range(cm.shape[1]):
            ax_cm.text(
                col,
                row,
                format(cm[row, col], "d"),
                ha="center",
                va="center",
                color="white" if cm[row, col] > threshold else "black"
            )

    plt.tight_layout()
    st.pyplot(fig_cm, use_container_width=False)
    plt.close(fig_cm)
