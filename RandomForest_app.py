import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
import plotly.express as px
import os
from datetime import datetime

# --- Page Configuration (set once at the top) ---
st.set_page_config(
    page_title="Customer Credit Profiling Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Robust File Loading with Caching ---
@st.cache_resource
def load_model_and_columns():
    """Loads the ML model and column list, with error handling."""
    model_path = "random_forest_model.joblib"
    columns_path = "credit_columns.pkl"
    
    if not os.path.exists(model_path) or not os.path.exists(columns_path):
        st.error(
            "Model or column file not found. "
            "Please ensure 'random_forest_model.joblib' and 'credit_columns.pkl' "
            "are in the same directory as this script."
        )
        st.stop()
        
    try:
        model = joblib.load(model_path)
        with open(columns_path, "rb") as f:
            model_columns = pickle.load(f)
        return model, model_columns
    except Exception as e:
        st.error(f"An error occurred while loading the necessary files: {e}")
        st.stop()

model, model_columns = load_model_and_columns()

# --- Dynamic Full-Page Theming ---
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

def get_theme_css(theme):
    """Generates a CSS string for the entire app based on the selected theme."""
    base_css = """
        <style>
            /* General Styling for custom elements */
            .stButton>button {
                border-radius: 8px; padding: 12px 24px; font-size: 16px;
                font-weight: bold; transition: all 0.3s ease; border: none;
            }
            .stButton>button:hover {
                transform: scale(1.05);
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            }
            .card {
                border-radius: 10px; padding: 20px; margin-bottom: 20px;
                transition: all 0.3s ease;
            }
            .card:hover {
                transform: translateY(-5px);
            }
            .social-link {
                text-decoration: none; font-size: 24px; margin: 0 10px;
                transition: color 0.3s;
            }
            .footer {
                text-align: center;
                padding: 20px 0;
                margin-top: 40px;
                border-top: 1px solid #e0e0e0;
            }
    """
    
    if theme == "Dark":
        dark_css = """
            /* --- Dark Theme --- */
            [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
                background-color: #1e1e1e;
            }
            .stMarkdown, .stExpander, h1, h2, h3, p, li, label, li b { color: #ffffff; }
            .stButton>button { background-color: #2196F3; color: white; }
            .stButton>button:hover { background-color: #1976D2; }
            .card, .stExpander {
                background-color: #2c2c2c;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
                border: 1px solid #444444;
            }
            .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
                background-color: #333333; color: #ffffff; border: 1px solid #555555;
            }
            .social-link { color: #2196F3; }
            .social-link:hover { color: #64b5f6; }
            .footer { border-top: 1px solid #444444; }
        </style>
        """
        return base_css + dark_css
    else: # Light Theme
        light_css = """
            /* --- Light Theme --- */
            [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
                background-color: #f0f2f6;
            }
            .stMarkdown, .stExpander, h1, h2, h3, p, li, label, li b { color: #333333; }
            .stButton>button { background-color: #4CAF50; color: white; }
            .stButton>button:hover { background-color: #45a049; }
            .card, .stExpander {
                background-color: #ffffff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                border: 1px solid #e0e0e0;
            }
            .social-link { color: #4CAF50; }
            .social-link:hover { color: #81c784; }
        </style>
        """
        return base_css + light_css

st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    theme = st.selectbox("Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        st.rerun()
        
    # --- UPDATED SIDEBAR CONTENT ---
    st.markdown("""
        <div class='card'>
            <h3>💳 Credit Score Predictor</h3>
            <p>A machine learning-powered app to predict your credit score category based on financial and demographic inputs.</p>
            <h4>📋 Project Workflow</h4>
            <ul>
                <li><b>Data Input</b>: Enter personal and financial details.</li>
                <li><b>Preprocessing</b>: Inputs are formatted and aligned with model requirements.</li>
                <li><b>Prediction</b>: Random Forest model predicts credit score category.</li>
                <li><b>Visualization</b>: Results displayed with interactive visuals.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
# --- Header ---
# st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("💳 Customer Credit Profiling Predictor")
st.markdown("<p>Enter your details in the sections below to receive an instant credit score category prediction from our machine learning model.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Main Content: Input Forms ---
st.header("Enter Applicant Details")

with st.expander("👤 Personal Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
        education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
        employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])
    with col2:
        image_path = "Data_security_05.jpg"
        if os.path.exists(image_path):
            st.image(image_path, caption="Your Data is Secure")
        else:
            st.info("ℹ️ Image file 'Data_security_05.jpg' not found, skipping display.")

with st.expander("💰 Financial Details", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        monthly_income = st.number_input("Monthly Income ($)", min_value=0.0, value=30000.0, step=1000.0, format="%.2f")
        total_credit_limit = st.number_input("Total Credit Limit ($)", min_value=1000.0, value=50000.0, step=1000.0, format="%.2f")
        average_transaction_amount = st.number_input("Average Transaction Amount ($)", min_value=0.0, value=1500.0, step=100.0, format="%.2f")
    with col2:
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
        late_payments_6m = st.slider("Late Payments (Last 6 Months)", min_value=0, value=0, step=1)
        # transaction_frequency = st.slider("Monthly Transaction Frequency", 0.0, 60.0, 5.0)
        transaction_frequency = st.slider("Monthly Transaction Frequency", 0, 60, 5, step=1)

with st.expander("📊 Behavioral Data", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        # login_frequency = st.slider("Monthly Login Frequency", 0.0, 30.0, 10.0)
        login_frequency = st.slider("Monthly Login Frequency", 0, 30, 10, step=1)
        credit_score_checks = st.slider("Yearly Credit Score Checks", 0, 20, 3)
    with col2:
        luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
        savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
        debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)
        
# --- Prediction Logic and Output ---
if st.button("🚀 Predict Credit Score"):
    input_dict = {
        'age': age, 'monthly_income': monthly_income, 'credit_utilization_ratio': credit_utilization_ratio,
        'total_credit_limit': total_credit_limit, 'late_payments_6m': late_payments_6m,
        'transaction_frequency': transaction_frequency, 'average_transaction_amount': average_transaction_amount,
        'login_frequency': login_frequency, 'credit_score_checks': credit_score_checks,
        'luxury_purchase_ratio': luxury_purchase_ratio, 'savings_rate': savings_rate, 'debt_to_income': debt_to_income,
        'gender_Male': 1 if gender == "Male" else 0, 'gender_Other': 1 if gender == "Other" else 0,
        'education_level_High School': 1 if education == "High School" else 0,
        'education_level_Master': 1 if education == "Master" else 0, 'education_level_PhD': 1 if education == "PhD" else 0,
        'employment_status_Retired': 1 if employment == "Retired" else 0,
        'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
        'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
    }
    
    input_df = pd.DataFrame([input_dict]).reindex(columns=model_columns, fill_value=0)
    prediction = model.predict(input_df)[0]
    
    # st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Prediction Result")
    st.success(f"✅ Predicted Credit Score Category: **{prediction}**")
    
    fig = px.bar(
        x=[prediction], y=[1], text=[prediction], title="Visualization of Prediction",
        color_discrete_sequence=["#4CAF50" if st.session_state.theme == "Light" else "#2196F3"]
    )
    fig.update_layout(showlegend=False, height=250, yaxis_visible=False, title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown(
    """
    <p>Connect with the developer:</p>
    <a href="https://www.linkedin.com" target="_blank" class="social-link">
        <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn" width="32" height="32">
    </a>
    <a href="https://www.github.com" target="_blank" class="social-link">
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="32" height="32" style="filter: invert(1);">
    </a>
    <p style="margin-top: 15px;">© """ + str(datetime.now().year) + """ Credit Risk Predictor. All rights reserved.</p>
    """,
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)