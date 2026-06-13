import streamlit as st
import pandas as pd
import joblib

# =========================
# Load Model Artifacts
# =========================

model = joblib.load("loanlens_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="LoanLens",
    page_icon="💰",
    layout="centered"
)

# =========================
# Sidebar
# =========================

with st.sidebar:
    st.header("📌 About LoanLens")

    st.write(
        """
        LoanLens is a Machine Learning-based
        Credit Risk Assessment System that predicts
        whether a loan application is likely to be approved.

        The model was trained using:
        - Data Preprocessing
        - Feature Engineering
        - Logistic Regression

        Built for educational and portfolio purposes.
        """
    )

# =========================
# Main Page
# =========================

st.title("💰 LoanLens")
st.subheader("Credit Risk Assessment & Loan Approval Prediction")

st.info(
    "This application is intended for educational and demonstration purposes only."
)

st.write("Enter applicant details below.")

# =========================
# Numerical Inputs
# =========================

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0.0,
    value=5000.0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0.0,
    value=2000.0
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

dependents = st.number_input(
    "Dependents",
    min_value=0,
    max_value=10,
    value=0
)

existing_loans = st.number_input(
    "Existing Loans",
    min_value=0,
    max_value=20,
    value=0
)

savings = st.number_input(
    "Savings",
    min_value=0.0,
    value=10000.0
)

collateral_value = st.number_input(
    "Collateral Value",
    min_value=0.0,
    value=50000.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=20000.0
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1,
    value=60
)

# =========================
# Education Mapping
# =========================

education_label = st.selectbox(
    "Education Level",
    ["High School", "Graduate", "Post Graduate"]
)

education_mapping = {
    "High School": 0,
    "Graduate": 1,
    "Post Graduate": 2
}

education_level = education_mapping[education_label]

credit_score = st.number_input(
    "Credit Score",
    min_value=300.0,
    max_value=900.0,
    value=700.0
)

dti_ratio = st.number_input(
    "DTI Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.30
)

# =========================
# Categorical Inputs
# =========================

employment_status = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-employed", "Unemployed"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Married", "Single"]
)

loan_purpose = st.selectbox(
    "Loan Purpose",
    ["Car", "Education", "Home", "Personal"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

employer_category = st.selectbox(
    "Employer Category",
    ["Government", "MNC", "Private", "Unemployed"]
)

# =========================
# Prediction
# =========================

if st.button("🔍 Predict Loan Approval"):

    data = {feature: 0 for feature in feature_names}

    # Numerical Features

    data["Applicant_Income"] = applicant_income
    data["Coapplicant_Income"] = coapplicant_income
    data["Age"] = age
    data["Dependents"] = dependents
    data["Existing_Loans"] = existing_loans
    data["Savings"] = savings
    data["Collateral_Value"] = collateral_value
    data["Loan_Amount"] = loan_amount
    data["Loan_Term"] = loan_term
    data["Education_Level"] = education_level

    # Feature Engineering

    data["DTI_Ratio_sq"] = dti_ratio ** 2
    data["Credit_Score_sq"] = credit_score ** 2

    # Employment Status

    if employment_status == "Salaried":
        data["Employment_Status_Salaried"] = 1

    elif employment_status == "Self-employed":
        data["Employment_Status_Self-employed"] = 1

    elif employment_status == "Unemployed":
        data["Employment_Status_Unemployed"] = 1

    # Marital Status

    if marital_status == "Single":
        data["Marital_Status_Single"] = 1

    # Loan Purpose

    if loan_purpose == "Car":
        data["Loan_Purpose_Car"] = 1

    elif loan_purpose == "Education":
        data["Loan_Purpose_Education"] = 1

    elif loan_purpose == "Home":
        data["Loan_Purpose_Home"] = 1

    elif loan_purpose == "Personal":
        data["Loan_Purpose_Personal"] = 1

    # Property Area

    if property_area == "Semiurban":
        data["Property_Area_Semiurban"] = 1

    elif property_area == "Urban":
        data["Property_Area_Urban"] = 1

    # Gender

    if gender == "Male":
        data["Gender_Male"] = 1

    # Employer Category

    if employer_category == "Government":
        data["Employer_Category_Government"] = 1

    elif employer_category == "MNC":
        data["Employer_Category_MNC"] = 1

    elif employer_category == "Private":
        data["Employer_Category_Private"] = 1

    elif employer_category == "Unemployed":
        data["Employer_Category_Unemployed"] = 1

    # DataFrame

    input_df = pd.DataFrame([data])

    input_df = input_df[feature_names]

    # Scale

    scaled_input = scaler.transform(input_df)

    # Predict

    prediction = model.predict(scaled_input)[0]

    probability = model.predict_proba(scaled_input)[0][1]

    st.markdown("### Prediction Result")

    if prediction == 1:
        st.success("✅ Loan Approved")

    else:
        st.error("❌ Loan Rejected")

    st.progress(float(probability))

    st.write(
        f"**Approval Probability:** {probability * 100:.2f}%"
    )

# =========================
# Footer
# =========================

st.markdown("---")
st.markdown(
    "Developed by **Hari Krishnan** | LoanLens Credit Risk Assessment System"
)