import streamlit as st
import pandas as pd
import joblib

# =========================
# Page Configuration (Must be first)
# =========================
st.set_page_config(
    page_title="LoanLens Pro",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Custom CSS for Premium UI
# =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Main Background & Gradient */
    .stApp {
        background: #f8fafc;
        color: #0f172a;
    }

    /* Reduce default top padding */
    .block-container {
        padding-top: 2rem !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid rgba(0, 0, 0, 0.05);
    }

    /* Input Labels */
    .stNumberInput label, .stSelectbox label {
        color: #475569 !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.5px;
    }

    /* Input Fields (Number, Selectbox) */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 1px solid rgba(0, 0, 0, 0.1) !important;
        border-radius: 8px !important;
        color: #0f172a !important;
        transition: all 0.3s ease;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    
    div[data-baseweb="input"] input {
        background-color: transparent !important;
        color: #0f172a !important;
    }

    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="select"] > div:hover {
        border-color: rgba(0, 0, 0, 0.2) !important;
        background-color: #f8fafc !important;
    }

    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
        background-color: #ffffff !important;
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        padding: 0.85rem 2rem !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        width: 100% !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35), inset 0 2px 4px rgba(255,255,255,0.2) !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 12px 25px rgba(37, 99, 235, 0.45), inset 0 2px 4px rgba(255,255,255,0.3) !important;
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
    }
    .stButton > button:active {
        transform: translateY(1px) scale(0.98) !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.3) !important;
    }

    /* Headers and Text */
    h1, h2, h3 {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    
    /* Section Headers Subtitle Styling */
    h3 {
        padding-bottom: 0.5rem;
        border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem !important;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Success / Error Messages */
    .stSuccess {
        background-color: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.4) !important;
        color: #064e3b !important;
        border-radius: 10px !important;
    }
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid rgba(239, 68, 68, 0.4) !important;
        color: #7f1d1d !important;
        border-radius: 10px !important;
    }
    
    hr {
        border-color: rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Load Model Artifacts
# =========================
@st.cache_resource
def load_artifacts():
    model = joblib.load("loanlens_model.pkl")
    scaler = joblib.load("scaler.pkl")
    feature_names = joblib.load("feature_names.pkl")
    return model, scaler, feature_names

model, scaler, feature_names = load_artifacts()

# =========================
# Sidebar
# =========================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h1 style="font-size: 2.5rem; margin-bottom: 0; background: -webkit-linear-gradient(45deg, #60a5fa, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">LoanLens</h1>
            <p style="color: #64748b; font-size: 0.9rem; margin-top: 0; font-weight: 500; letter-spacing: 1px;">PRO EDITION</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        """
        <div style="font-size: 0.95rem; color: #475569; line-height: 1.6; padding-bottom: 80px;">
        An advanced Machine Learning-based Credit Risk Assessment System that predicts loan approval probabilities.
        <br><br>
        <strong>Engine Capabilities:</strong>
        <ul style="margin-top: 8px; padding-left: 20px; color: #64748b;">
            <li>Dynamic Feature Engineering</li>
            <li>Robust Data Preprocessing</li>
            <li>Predictive Logistic Regression</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div style="position: absolute; bottom: 15px; left: 0; right: 0; text-align: center; padding: 0 15px;">
            <hr style="border-color: rgba(0,0,0,0.1); margin-bottom: 10px;">
            <span style="font-size: 0.8rem; color: #64748b;">Developed by Hari Krishnan</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# Main Page Header
# =========================
st.markdown(
    """
    <div style="margin-bottom: 2rem; margin-top: -1.5rem;">
        <h1 style="font-size: 2.5rem; margin-top: 0; margin-bottom: 0.2rem; color: #0f172a;">
            Credit Risk Assessment Engine
        </h1>
        <p style="color: #64748b; font-size: 1.1rem;">Fill in the applicant details below to evaluate loan approval risk.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Input Layout (Columns)
# =========================
user_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -4px; margin-right: 8px;"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
st.markdown(f"### {user_icon} Applicant Profile", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    applicant_income = st.number_input("Applicant Income ($)", min_value=0.0, value=5000.0, step=500.0)
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    gender = st.selectbox("Gender", ["Female", "Male"])
    marital_status = st.selectbox("Marital Status", ["Married", "Single"])

with col2:
    coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0.0, value=2000.0, step=500.0)
    dependents = st.number_input("Dependents", min_value=0, max_value=10, value=0)
    education_label = st.selectbox("Education Level", ["High School", "Graduate", "Post Graduate"])
    employment_status = st.selectbox("Employment Status", ["Salaried", "Self-employed", "Unemployed"])

with col3:
    savings = st.number_input("Total Savings ($)", min_value=0.0, value=10000.0, step=1000.0)
    employer_category = st.selectbox("Employer Category", ["Government", "MNC", "Private", "Unemployed"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True) # Spacer

st.markdown("<br>", unsafe_allow_html=True)
card_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -4px; margin-right: 8px;"><rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/></svg>'
st.markdown(f"### {card_icon} Loan & Credit Details", unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

with col4:
    loan_amount = st.number_input("Requested Loan Amount ($)", min_value=0.0, value=20000.0, step=1000.0)
    existing_loans = st.number_input("Number of Existing Loans", min_value=0, max_value=20, value=0)
    dti_ratio = st.number_input("Debt-to-Income (DTI) Ratio", min_value=0.0, max_value=1.0, value=0.30, step=0.05)

with col5:
    loan_term = st.number_input("Loan Term (Months)", min_value=1, value=60, step=12)
    collateral_value = st.number_input("Collateral Value ($)", min_value=0.0, value=50000.0, step=1000.0)

with col6:
    loan_purpose = st.selectbox("Purpose of Loan", ["Car", "Education", "Home", "Personal"])
    credit_score = st.number_input("Credit Score", min_value=300.0, max_value=900.0, value=700.0, step=10.0)


st.markdown("<br><br>", unsafe_allow_html=True)

# =========================
# Prediction Engine
# =========================
center_col1, center_col2, center_col3 = st.columns([1, 2, 1])
with center_col2:
    predict_clicked = st.button("Evaluate Risk  ➔", use_container_width=True)

if predict_clicked:
    # --- Education Mapping ---
    education_mapping = {"High School": 0, "Graduate": 1, "Post Graduate": 2}
    education_level = education_mapping[education_label]

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
    if employment_status == "Salaried": data["Employment_Status_Salaried"] = 1
    elif employment_status == "Self-employed": data["Employment_Status_Self-employed"] = 1
    elif employment_status == "Unemployed": data["Employment_Status_Unemployed"] = 1

    # Marital Status
    if marital_status == "Single": data["Marital_Status_Single"] = 1

    # Loan Purpose
    if loan_purpose == "Car": data["Loan_Purpose_Car"] = 1
    elif loan_purpose == "Education": data["Loan_Purpose_Education"] = 1
    elif loan_purpose == "Home": data["Loan_Purpose_Home"] = 1
    elif loan_purpose == "Personal": data["Loan_Purpose_Personal"] = 1

    # Property Area
    if property_area == "Semiurban": data["Property_Area_Semiurban"] = 1
    elif property_area == "Urban": data["Property_Area_Urban"] = 1

    # Gender
    if gender == "Male": data["Gender_Male"] = 1

    # Employer Category
    if employer_category == "Government": data["Employer_Category_Government"] = 1
    elif employer_category == "MNC": data["Employer_Category_MNC"] = 1
    elif employer_category == "Private": data["Employer_Category_Private"] = 1
    elif employer_category == "Unemployed": data["Employer_Category_Unemployed"] = 1

    # DataFrame and Scaling
    input_df = pd.DataFrame([data])[feature_names]
    scaled_input = scaler.transform(input_df)

    # Predict
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    st.markdown("<hr style='margin-top: 1rem; margin-bottom: 0.5rem;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #0f172a; margin-top: 0;'>Analysis Result</h3>", unsafe_allow_html=True)

    res_col1, res_col2, res_col3 = st.columns([1, 2, 1])
    with res_col2:
        if prediction == 1:
            st.success(f"### 🎉 Loan Approved\n**Approval Confidence:** {probability * 100:.2f}%")
        else:
            st.error(f"### 🛑 Loan Rejected\n**Approval Confidence:** {probability * 100:.2f}%")
        
        # Custom Progress Bar
        bar_color = "linear-gradient(90deg, #10b981, #34d399)" if prediction == 1 else "linear-gradient(90deg, #ef4444, #f87171)"
        st.markdown(
            f"""
            <div style="width: 100%; background-color: rgba(0,0,0,0.05); border-radius: 8px; margin-top: 15px; overflow: hidden; height: 12px; border: 1px solid rgba(0,0,0,0.1);">
                <div style="width: {probability * 100:.2f}%; background: {bar_color}; height: 100%; border-radius: 8px; transition: width 1s ease-in-out;"></div>
            </div>
            <div id='result-bottom'></div>
            """,
            unsafe_allow_html=True
        )
    
    # Auto-scroll to the bottom when prediction is complete
    import streamlit.components.v1 as components
    components.html(
        """
        <script>
            setTimeout(function() {
                var doc = window.parent.document;
                var el = doc.getElementById('result-bottom');
                if (el) {
                    el.scrollIntoView({behavior: 'smooth', block: 'center'});
                }
            }, 150);
        </script>
        """,
        height=0,
    )