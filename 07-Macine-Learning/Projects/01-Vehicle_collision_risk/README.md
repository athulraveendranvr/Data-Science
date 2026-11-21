# 🚗 Vehicle Collision Risk Prediction

A Machine Learning project that predicts vehicle collision risk based on vehicle characteristics, road conditions, traffic, and environmental factors.

## 🎯 Project Objective

Develop a classification system that categorizes driving scenarios into three collision risk levels:

- Low
- Medium
- High

## 📊 Dataset

- Approximately 8,000 records.
- Synthetically generated dataset.
- Contains numerical and categorical features.
- Includes missing values and an imbalanced target variable.

**Target:** `collision_risk`

## ⚙️ Data Preprocessing

- Missing value handling
- Outlier analysis
- Removal of unnecessary columns
- Categorical encoding using One-Hot Encoding
- Numerical feature scaling
- Train-test splitting with stratification

## 🤖 Machine Learning Models

Four classification algorithms were implemented:

1. K-Nearest Neighbors (KNN)
2. Naive Bayes
3. Decision Tree
4. Random Forest

## 📈 Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 🌐 Streamlit Application

An interactive web application featuring:

- Selection between four trained models
- Custom vehicle and road condition inputs
- Automated preprocessing
- Collision risk predictions
- Prediction probability visualisation

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

## 🚀 Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/athulraveendranvr/Data-Science.git
   ```

2. Navigate to the project folder:

   ```bash
   cd 01-Vehicle_collision_risk
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## ⚠️ Disclaimer

This project uses synthetic data for educational and demonstration purposes. Its predictions are not based on real accident records and should not be used for real-world driving decisions.