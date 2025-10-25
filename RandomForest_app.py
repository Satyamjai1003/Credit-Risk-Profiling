# # import streamlit as st
# # import numpy as np
# # import pandas as pd
# # import joblib
# # import pickle

# # # Load model and columns
# # model = joblib.load("random_forest_model.joblib")
# # with open("credit_columns.pkl", "rb") as f:
# #     model_columns = pickle.load(f)

# # st.title("💳 Credit Score Predictor")
# # st.write("Enter your details to predict your credit score category.")

# # # 🧾 Input Fields
# # age = st.number_input("Age", min_value=18, max_value=100, value=30)
# # monthly_income = st.number_input("Monthly Income", min_value=0.0, value=30000.0)
# # credit_utilization_ratio = st.slider("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
# # total_credit_limit = st.number_input("Total Credit Limit", min_value=1000.0, value=50000.0)
# # late_payments_6m = st.number_input("Late Payments (Last 6 Months)", min_value=0, value=0)
# # transaction_frequency = st.slider("Transaction Frequency", 0.0, 60.0, 5.0)
# # average_transaction_amount = st.number_input("Average Transaction Amount", min_value=0.0, value=1500.0)
# # login_frequency = st.slider("Login Frequency", 0.0, 30.0, 10.0)
# # credit_score_checks = st.slider("Credit Score Checks", 0, 20, 3)
# # luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
# # savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
# # debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)

# # # Categorical Inputs
# # gender = st.selectbox("Gender", ["Female", "Male", "Other"])
# # education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
# # employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])

# # # 📦 Create input dictionary
# # input_dict = {
# #     'age': age,
# #     'monthly_income': monthly_income,
# #     'credit_utilization_ratio': credit_utilization_ratio,
# #     'total_credit_limit': total_credit_limit,
# #     'late_payments_6m': late_payments_6m,
# #     'transaction_frequency': transaction_frequency,
# #     'average_transaction_amount': average_transaction_amount,
# #     'login_frequency': login_frequency,
# #     'credit_score_checks': credit_score_checks,
# #     'luxury_purchase_ratio': luxury_purchase_ratio,
# #     'savings_rate': savings_rate,
# #     'debt_to_income': debt_to_income,
# #     'gender_Male': 1 if gender == "Male" else 0,
# #     'gender_Other': 1 if gender == "Other" else 0,
# #     'education_level_High School': 1 if education == "High School" else 0,
# #     'education_level_Master': 1 if education == "Master" else 0,
# #     'education_level_PhD': 1 if education == "PhD" else 0,
# #     'employment_status_Retired': 1 if employment == "Retired" else 0,
# #     'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
# #     'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
# # }

# # # ⚙️ Convert to DataFrame and align with model columns
# # input_df = pd.DataFrame([input_dict])
# # input_df = input_df.reindex(columns=model_columns, fill_value=0)

# # # 🚀 Predict
# # if st.button("Predict Credit Score"):
# #     prediction = model.predict(input_df)[0]
# #     st.success(f"✅ Predicted Credit Score Category: **{prediction}**")





# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib
# import pickle
# import plotly.express as px

# # Set page configuration
# st.set_page_config(
#     page_title="Credit Score Predictor",
#     page_icon="💳",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Load model and columns
# model = joblib.load("random_forest_model.joblib")
# with open("credit_columns.pkl", "rb") as f:
#     model_columns = pickle.load(f)

# # Custom CSS for enhanced UI and theme support
# st.markdown("""
#     <style>
#     /* General Styling */
#     .main {
#         font-family: 'Arial', sans-serif;
#         padding: 20px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-size: 16px;
#         font-weight: bold;
#         transition: all 0.3s ease;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#         transform: scale(1.05);
#     }
#     .stSlider .st-bx {
#         background-color: #f0f2f6;
#         border-radius: 8px;
#     }
#     .stNumberInput input {
#         border-radius: 8px;
#         padding: 8px;
#     }
#     .stSelectbox div[data-baseweb="select"] {
#         border-radius: 8px;
#     }
#     /* Sidebar Styling */
#     .sidebar .sidebar-content {
#         background-color: #f8f9fa;
#         border-radius: 10px;
#         padding: 20px;
#     }
#     /* Light Theme */
#     [data-theme='light'] {
#         background-color: #ffffff;
#         color: #333333;
#     }
#     [data-theme='light'] .sidebar .sidebar-content {
#         background-color: #f8f9fa;
#     }
#     [data-theme='light'] .card {
#         background-color: #ffffff;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     /* Dark Theme */
#     [data-theme='dark'] {
#         background-color: #1e1e1e;
#         color: #ffffff;
#     }
#     [data-theme='dark'] .sidebar .sidebar-content {
#         background-color: #2c2c2c;
#     }
#     [data-theme='dark'] .stButton>button {
#         background-color: #2196F3;
#     }
#     [data-theme='dark'] .stButton>button:hover {
#         background-color: #1976D2;
#     }
#     [data-theme='dark'] .card {
#         background-color: #2c2c2c;
#         box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
#     }
#     /* Card Styling */
#     .card {
#         border-radius: 10px;
#         padding: 20px;
#         margin-bottom: 20px;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#     }
#     /* Social Links */
#     .social-link {
#         color: #4CAF50;
#         text-decoration: none;
#         font-size: 16px;
#         margin-right: 15px;
#     }
#     [data-theme='dark'] .social-link {
#         color: #2196F3;
#     }
#     /* Expander Styling */
#     .stExpander {
#         border-radius: 8px;
#         border: 1px solid #e0e0e0;
#     }
#     [data-theme='dark'] .stExpander {
#         border: 1px solid #444444;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Sidebar content
# with st.sidebar:
#     st.markdown("""
#         <div class='card'>
#             <h3>💳 Credit Score Predictor</h3>
#             <p>A machine learning-powered app to predict your credit score category based on financial and demographic inputs.</p>
#             <h4>📋 Project Workflow</h4>
#             <ul>
#                 <li><b>Data Input</b>: Enter personal and financial details.</li>
#                 <li><b>Preprocessing</b>: Inputs are formatted and aligned with model requirements.</li>
#                 <li><b>Prediction</b>: Random Forest model predicts credit score category.</li>
#                 <li><b>Visualization</b>: Results displayed with interactive visuals.</li>
#             </ul>
#             <h4>🔗 Connect</h4>
#             <p>
#                 <a href="https://www.linkedin.com" target="_blank" class="social-link">LinkedIn</a>
#                 <a href="https://www.github.com" target="_blank" class="social-link">GitHub</a>
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Theme toggle
#     theme = st.selectbox("Select Theme", ["Light", "Dark"])
#     st.markdown(f"""
#         <script>
#             document.documentElement.setAttribute('data-theme', '{theme.lower()}');
#         </script>
#     """, unsafe_allow_html=True)

# # Main content
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.title("💳 Credit Score Predictor")
# st.write("Enter your details to predict your credit score category.")
# st.markdown("</div>", unsafe_allow_html=True)

# # Input sections
# with st.expander("👤 Personal Information", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", min_value=18, max_value=100, value=30)
#         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
#         education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
#         employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])
#     with col2:
#         # st.image("C:\Users\asus\Videos\Machine Learning\20945443.jpg", caption="Personal Info")
#         st.image(r"C:\Users\asus\Videos\Machine Learning\Data_security_05.jpg", caption="Personal Info")

# with st.expander("💰 Financial Details", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         monthly_income = st.number_input("Monthly Income", min_value=0.0, value=30000.0)
#         total_credit_limit = st.number_input("Total Credit Limit", min_value=1000.0, value=50000.0)
#         average_transaction_amount = st.number_input("Average Transaction Amount", min_value=0.0, value=1500.0)
#     with col2:
#         credit_utilization_ratio = st.slider("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
#         late_payments_6m = st.number_input("Late Payments (Last 6 Months)", min_value=0, value=0)
#         transaction_frequency = st.slider("Transaction Frequency", 0.0, 60.0, 5.0)

# with st.expander("📊 Behavioral Data", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         login_frequency = st.slider("Login Frequency", 0.0, 30.0, 10.0)
#         credit_score_checks = st.slider("Credit Score Checks", 0, 20, 3)
#     with col2:
#         luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
#         savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
#         debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)

# # Create input dictionary
# input_dict = {
#     'age': age,
#     'monthly_income': monthly_income,
#     'credit_utilization_ratio': credit_utilization_ratio,
#     'total_credit_limit': total_credit_limit,
#     'late_payments_6m': late_payments_6m,
#     'transaction_frequency': transaction_frequency,
#     'average_transaction_amount': average_transaction_amount,
#     'login_frequency': login_frequency,
#     'credit_score_checks': credit_score_checks,
#     'luxury_purchase_ratio': luxury_purchase_ratio,
#     'savings_rate': savings_rate,
#     'debt_to_income': debt_to_income,
#     'gender_Male': 1 if gender == "Male" else 0,
#     'gender_Other': 1 if gender == "Other" else 0,
#     'education_level_High School': 1 if education == "High School" else 0,
#     'education_level_Master': 1 if education == "Master" else 0,
#     'education_level_PhD': 1 if education == "PhD" else 0,
#     'employment_status_Retired': 1 if employment == "Retired" else 0,
#     'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
#     'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
# }

# # Convert to DataFrame and align with model columns
# input_df = pd.DataFrame([input_dict])
# input_df = input_df.reindex(columns=model_columns, fill_value=0)

# # Predict and display result
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# if st.button("🚀 Predict Credit Score"):
#     prediction = model.predict(input_df)[0]
#     st.success(f"✅ Predicted Credit Score Category: **{prediction}**")
    
#     # Visualize prediction
#     fig = px.bar(
#         x=["Credit Score Category"],
#         y=[1],
#         text=[prediction],
#         title="Prediction Result",
#         color_discrete_sequence=["#4CAF50" if theme == "Light" else "#2196F3"]
#     )
#     fig.update_layout(showlegend=False, height=300)
#     st.plotly_chart(fig, use_container_width=True)
# st.markdown("</div>", unsafe_allow_html=True)





# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib
# import pickle
# import plotly.express as px
# # Set page configuration
# st.set_page_config(
#     page_title="Credit Risk Predictor",
#     page_icon="💳",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
# # Initialize session state for theme
# if "theme" not in st.session_state:
#     st.session_state.theme = "Light"
# # Custom CSS for enhanced UI and theme support
# st.markdown("""
#     <style>
#     /* General Styling */
#     .main {
#         font-family: 'Arial', sans-serif;
#         padding: 20px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border-radius: 8px;
#         padding: 12px 24px;
#         font-size: 16px;
#         font-weight: bold;
#         transition: all 0.3s ease;
#         border: none;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#         transform: scale(1.05);
#     }
#     .stSlider .st-bx {
#         border-radius: 8px;
#     }
#     .stNumberInput input {
#         border-radius: 8px;
#         padding: 8px;
#         border: 1px solid #e0e0e0;
#     }
#     .stSelectbox div[data-baseweb="select"] {
#         border-radius: 8px;
#         border: 1px solid #e0e0e0;
#     }
#     /* Sidebar Styling */
#     .css-1lcbmhc, .css-1v3fvcr {  /* Sidebar container */
#         border-radius: 10px;
#         padding: 20px;
#     }
#     /* Light Theme */
#     [data-theme='light'] {
#         background-color: #ffffff;
#         color: #333333;
#     }
#     [data-theme='light'] .css-1lcbmhc, [data-theme='light'] .css-1v3fvcr {
#         background-color: #f8f9fa;
#     }
#     [data-theme='light'] .card {
#         background-color: #ffffff;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#     }
#     [data-theme='light'] .stNumberInput input, [data-theme='light'] .stSelectbox div[data-baseweb="select"] {
#         background-color: #f0f2f6;
#     }
#     [data-theme='light'] .stSlider .st-bx {
#         background-color: #f0f2f6;
#     }
#     [data-theme='light'] .stExpander {
#         border: 1px solid #e0e0e0;
#         background-color: #ffffff;
#     }
#     /* Dark Theme */
#     [data-theme='dark'] {
#         background-color: #1e1e1e;
#         color: #ffffff;
#     }
#     [data-theme='dark'] .css-1lcbmhc, [data-theme='dark'] .css-1v3fvcr {
#         background-color: #2c2c2c;
#     }
#     [data-theme='dark'] .stButton>button {
#         background-color: #2196F3;
#     }
#     [data-theme='dark'] .stButton>button:hover {
#         background-color: #1976D2;
#     }
#     [data-theme='dark'] .card {
#         background-color: #2c2c2c;
#         box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1);
#     }
#     [data-theme='dark'] .stNumberInput input, [data-theme='dark'] .stSelectbox div[data-baseweb="select"] {
#         background-color: #333333;
#         color: #ffffff;
#         border: 1px solid #444444;
#     }
#     [data-theme='dark'] .stSlider .st-bx {
#         background-color: #333333;
#     }
#     [data-theme='dark'] .stExpander {
#         border: 1px solid #444444;
#         background-color: #2c2c2c;
#     }
#     [data-theme='dark'] .stMarkdown, [data-theme='dark'] .stSuccess {
#         color: #ffffff;
#     }
#     /* Card Styling */
#     .card {
#         border-radius: 10px;
#         padding: 20px;
#         margin-bottom: 20px;
#         transition: all 0.3s ease;
#     }
#     .card:hover {
#         transform: translateY(-5px);
#     }
#     /* Social Links */
#     .social-link {
#         color: #4CAF50;
#         text-decoration: none;
#         font-size: 16px;
#         margin-right: 15px;
#     }
#     [data-theme='dark'] .social-link {
#         color: #2196F3;
#     }
#     </style>
# """, unsafe_allow_html=True)
# # Apply theme to document
# st.markdown(f"""
#     <script>
#         document.documentElement.setAttribute('data-theme', '{st.session_state.theme.lower()}');
#     </script>
# """, unsafe_allow_html=True)
# # Sidebar content
# with st.sidebar:
#     st.markdown("""
#         <div class='card'>
#             <h3>💳 Credit Score Predictor</h3>
#             <p>A machine learning-powered app to predict your credit score category based on financial and demographic inputs.</p>
#             <h4>📋 Project Workflow</h4>
#             <ul>
#                 <li><b>Data Input</b>: Enter personal and financial details.</li>
#                 <li><b>Preprocessing</b>: Inputs are formatted and aligned with model requirements.</li>
#                 <li><b>Prediction</b>: Random Forest model predicts credit score category.</li>
#                 <li><b>Visualization</b>: Results displayed with interactive visuals.</li>
#             </ul>
#             <h4>🔗 Connect</h4>
#             <p>
#                 <a href="https://www.linkedin.com" target="_blank" class="social-link">LinkedIn</a>
#                 <a href="https://www.github.com" target="_blank" class="social-link">GitHub</a>
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Theme toggle
#     theme = st.selectbox("Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)
#     if theme != st.session_state.theme:
#         st.session_state.theme = theme
#         st.experimental_rerun()
# # Load model and columns
# model = joblib.load("random_forest_model.joblib")
# with open("credit_columns.pkl", "rb") as f:
#     model_columns = pickle.load(f)
# # Main content
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.title("💳 Credit Score Predictor")
# st.write("Enter your details to predict your credit score category.")
# st.markdown("</div>", unsafe_allow_html=True)
# # Input sections
# with st.expander("👤 Personal Information", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", min_value=18, max_value=100, value=30)
#         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
#         education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
#         employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])
#     with col2:
#         st.image(r"C:\Users\ASUS\Music\Summer_Training_Project\LPU_Project_File\Data_security_05.jpg", caption="Personal Info")
# with st.expander("💰 Financial Details", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         monthly_income = st.number_input("Monthly Income", min_value=0.0, value=30000.0)
#         total_credit_limit = st.number_input("Total Credit Limit", min_value=1000.0, value=50000.0)
#         average_transaction_amount = st.number_input("Average Transaction Amount", min_value=0.0, value=1500.0)
#     with col2:
#         credit_utilization_ratio = st.slider("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
#         late_payments_6m = st.number_input("Late Payments (Last 6 Months)", min_value=0, value=0)
#         transaction_frequency = st.slider("Transaction Frequency", 0.0, 60.0, 5.0)
# with st.expander("📊 Behavioral Data", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         login_frequency = st.slider("Login Frequency", 0.0, 30.0, 10.0)
#         credit_score_checks = st.slider("Credit Score Checks", 0, 20, 3)
#     with col2:
#         luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
#         savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
#         debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)
# # Create input dictionary
# input_dict = {
#     'age': age,
#     'monthly_income': monthly_income,
#     'credit_utilization_ratio': credit_utilization_ratio,
#     'total_credit_limit': total_credit_limit,
#     'late_payments_6m': late_payments_6m,
#     'transaction_frequency': transaction_frequency,
#     'average_transaction_amount': average_transaction_amount,
#     'login_frequency': login_frequency,
#     'credit_score_checks': credit_score_checks,
#     'luxury_purchase_ratio': luxury_purchase_ratio,
#     'savings_rate': savings_rate,
#     'debt_to_income': debt_to_income,
#     'gender_Male': 1 if gender == "Male" else 0,
#     'gender_Other': 1 if gender == "Other" else 0,
#     'education_level_High School': 1 if education == "High School" else 0,
#     'education_level_Master': 1 if education == "Master" else 0,
#     'education_level_PhD': 1 if education == "PhD" else 0,
#     'employment_status_Retired': 1 if employment == "Retired" else 0,
#     'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
#     'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
# }
# # Convert to DataFrame and align with model columns
# input_df = pd.DataFrame([input_dict])
# input_df = input_df.reindex(columns=model_columns, fill_value=0)
# # Predict and display result
# st.markdown("<div class='card'>", unsafe_allow_html=True)
# if st.button("🚀 Predict Credit Score"):
#     prediction = model.predict(input_df)[0]
#     st.success(f"✅ Predicted Credit Score Category: **{prediction}**")
    
#     # Visualize prediction
#     fig = px.bar(
#         x=["Credit Score Category"],
#         y=[1],
#         text=[prediction],
#         title="Prediction Result",
#         color_discrete_sequence=["#4CAF50" if st.session_state.theme == "Light" else "#2196F3"]
#     )
#     fig.update_layout(showlegend=False, height=300)
#     st.plotly_chart(fig, use_container_width=True)
# st.markdown("</div>", unsafe_allow_html=True)


# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib
# import pickle
# import plotly.express as px
# import os

# # --- Page Configuration (set once at the top) ---
# st.set_page_config(
#     page_title="Credit Risk Predictor",
#     page_icon="💳",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- Robust File Loading with Caching ---
# # Caching ensures the model is loaded only once, improving performance.
# @st.cache_resource
# def load_model_and_columns():
#     """Loads the ML model and column list, with error handling."""
#     model_path = "random_forest_model.joblib"
#     columns_path = "credit_columns.pkl"
    
#     # Check if files exist before trying to load them
#     if not os.path.exists(model_path) or not os.path.exists(columns_path):
#         st.error(
#             "Model or column file not found. "
#             "Please ensure 'random_forest_model.joblib' and 'credit_columns.pkl' "
#             "are in the same directory as this script."
#         )
#         # Stop the app execution if files are missing
#         st.stop()
        
#     try:
#         model = joblib.load(model_path)
#         with open(columns_path, "rb") as f:
#             model_columns = pickle.load(f)
#         return model, model_columns
#     except Exception as e:
#         st.error(f"An error occurred while loading the necessary files: {e}")
#         st.stop()

# # Load the files
# model, model_columns = load_model_and_columns()

# # --- Dynamic Full-Page Theming ---
# # Initialize session state for the theme
# if "theme" not in st.session_state:
#     st.session_state.theme = "Light"

# def get_theme_css(theme):
#     """
#     Generates a CSS string for the entire app based on the selected theme.
#     This is the most robust way to apply custom themes in Streamlit.
#     """
#     # Base styles common to both themes
#     base_css = """
#         <style>
#             /* General Styling for custom elements */
#             .stButton>button {
#                 border-radius: 8px; padding: 12px 24px; font-size: 16px;
#                 font-weight: bold; transition: all 0.3s ease; border: none;
#             }
#             .stButton>button:hover {
#                 transform: scale(1.05);
#             }
#             .card {
#                 border-radius: 10px; padding: 20px; margin-bottom: 20px;
#                 transition: all 0.3s ease;
#             }
#             .card:hover {
#                 transform: translateY(-5px);
#             }
#             .social-link {
#                 text-decoration: none; font-size: 16px; margin-right: 15px;
#             }
#     """
    
#     # Append theme-specific styles
#     if theme == "Dark":
#         dark_css = """
#             /* --- Dark Theme --- */
#             [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
#                 background-color: #1e1e1e;
#             }
#             .stMarkdown, .stExpander, h1, h2, h3, p, li, label {
#                 color: #ffffff;
#             }
#             .stButton>button { background-color: #2196F3; color: white; }
#             .stButton>button:hover { background-color: #1976D2; }
#             .card, .stExpander {
#                 background-color: #2c2c2c;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
#                 border: 1px solid #444444;
#             }
#             .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
#                 background-color: #333333; color: #ffffff; border: 1px solid #555555;
#             }
#             .social-link { color: #2196F3; }
#         </style>
#         """
#         return base_css + dark_css
#     else: # Light Theme
#         light_css = """
#             /* --- Light Theme --- */
#             [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
#                 background-color: #f0f2f6;
#             }
#             .stMarkdown, .stExpander, h1, h2, h3, p, li, label {
#                 color: #333333;
#             }
#             .stButton>button { background-color: #4CAF50; color: white; }
#             .stButton>button:hover { background-color: #45a049; }
#             .card, .stExpander {
#                 background-color: #ffffff;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#                 border: 1px solid #e0e0e0;
#             }
#             .social-link { color: #4CAF50; }
#         </style>
#         """
#         return base_css + light_css

# # Apply the generated CSS
# st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

# # --- Sidebar Content ---
# with st.sidebar:
#     # Place the theme toggle at the top for easy access
#     theme = st.selectbox("Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)
#     if theme != st.session_state.theme:
#         st.session_state.theme = theme
#         st.rerun() # Use the modern, standard function to rerun the app
        
#     st.markdown("""
#         <div class='card'>
#             <h3>💳 Credit Score Predictor</h3>
#             <p>An interactive tool to predict credit score categories using a machine learning model.</p>
#             <h4>📋 Project Workflow</h4>
#             <ul>
#                 <li><b>Data Input</b>: Enter personal and financial details.</li>
#                 <li><b>Prediction</b>: A Random Forest model predicts the category.</li>
#                 <li><b>Visualization</b>: Results displayed with an interactive chart.</li>
#             </ul>
#             <h4>🔗 Connect</h4>
#             <p>
#                 <a href="https://www.linkedin.com" target="_blank" class="social-link">LinkedIn</a>
#                 <a href="https://www.github.com" target="_blank" class="social-link">GitHub</a>
#             </p>
#         </div>
#     """, unsafe_allow_html=True)

# # --- Main App Body ---
# # st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.title("Credit Score Predictor")
# st.write("Enter your details in the sections below to get a credit score category prediction.")
# st.markdown("</div>", unsafe_allow_html=True)

# # --- Input Sections ---
# with st.expander("👤 Personal Information", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", min_value=18, max_value=100, value=30)
#         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
#         education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
#         employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])
#     with col2:
#         # FIX: Use a relative path. The image file must be in the same folder as the script.
#         image_path = "Data_security_05.jpg"
#         if os.path.exists(image_path):
#             st.image(image_path, caption="Secure Financial Data")
#         else:
#             st.warning("Image file not found. Please place 'Data_security_05.jpg' in the project directory.")

# with st.expander("💰 Financial Details", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         monthly_income = st.number_input("Monthly Income", min_value=0.0, value=30000.0)
#         total_credit_limit = st.number_input("Total Credit Limit", min_value=1000.0, value=50000.0)
#         average_transaction_amount = st.number_input("Average Transaction Amount", min_value=0.0, value=1500.0)
#     with col2:
#         credit_utilization_ratio = st.slider("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
#         late_payments_6m = st.number_input("Late Payments (Last 6 Months)", min_value=0, value=0)
#         transaction_frequency = st.slider("Transaction Frequency", 0.0, 60.0, 5.0)

# with st.expander("📊 Behavioral Data", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         login_frequency = st.slider("Login Frequency", 0.0, 30.0, 10.0)
#         credit_score_checks = st.slider("Credit Score Checks", 0, 20, 3)
#     with col2:
#         luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
#         savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
#         debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)
        
# # --- Prediction Logic and Output ---
# if st.button("🚀 Predict Credit Score"):
#     input_dict = {
#         'age': age, 'monthly_income': monthly_income, 'credit_utilization_ratio': credit_utilization_ratio,
#         'total_credit_limit': total_credit_limit, 'late_payments_6m': late_payments_6m,
#         'transaction_frequency': transaction_frequency, 'average_transaction_amount': average_transaction_amount,
#         'login_frequency': login_frequency, 'credit_score_checks': credit_score_checks,
#         'luxury_purchase_ratio': luxury_purchase_ratio, 'savings_rate': savings_rate, 'debt_to_income': debt_to_income,
#         'gender_Male': 1 if gender == "Male" else 0, 'gender_Other': 1 if gender == "Other" else 0,
#         'education_level_High School': 1 if education == "High School" else 0,
#         'education_level_Master': 1 if education == "Master" else 0, 'education_level_PhD': 1 if education == "PhD" else 0,
#         'employment_status_Retired': 1 if employment == "Retired" else 0,
#         'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
#         'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
#     }
    
#     input_df = pd.DataFrame([input_dict]).reindex(columns=model_columns, fill_value=0)
#     prediction = model.predict(input_df)[0]
    
#     # st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.success(f"✅ Predicted Credit Score Category: **{prediction}**")
    
#     # Visualization
#     fig = px.bar(
#         x=[prediction], y=[1], text=[prediction], title="Prediction Result",
#         color_discrete_sequence=["#4CAF50" if st.session_state.theme == "Light" else "#2196F3"]
#     )
#     fig.update_layout(showlegend=False, height=300, yaxis_visible=False)
#     st.plotly_chart(fig, use_container_width=True)
#     st.markdown("</div>", unsafe_allow_html=True)




# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib
# import pickle
# import plotly.express as px
# import os
# from datetime import datetime

# # --- Page Configuration (set once at the top) ---
# st.set_page_config(
#     page_title="Credit Risk Predictor",
#     page_icon="💳",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # --- Robust File Loading with Caching ---
# @st.cache_resource
# def load_model_and_columns():
#     """Loads the ML model and column list, with error handling."""
#     model_path = "random_forest_model.joblib"
#     columns_path = "credit_columns.pkl"
    
#     if not os.path.exists(model_path) or not os.path.exists(columns_path):
#         st.error(
#             "Model or column file not found. "
#             "Please ensure 'random_forest_model.joblib' and 'credit_columns.pkl' "
#             "are in the same directory as this script."
#         )
#         st.stop()
        
#     try:
#         model = joblib.load(model_path)
#         with open(columns_path, "rb") as f:
#             model_columns = pickle.load(f)
#         return model, model_columns
#     except Exception as e:
#         st.error(f"An error occurred while loading the necessary files: {e}")
#         st.stop()

# model, model_columns = load_model_and_columns()

# # --- Dynamic Full-Page Theming ---
# if "theme" not in st.session_state:
#     st.session_state.theme = "Light"

# def get_theme_css(theme):
#     """Generates a CSS string for the entire app based on the selected theme."""
#     base_css = """
#         <style>
#             /* General Styling for custom elements */
#             .stButton>button {
#                 border-radius: 8px; padding: 12px 24px; font-size: 16px;
#                 font-weight: bold; transition: all 0.3s ease; border: none;
#             }
#             .stButton>button:hover {
#                 transform: scale(1.05);
#                 box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
#             }
#             .card {
#                 border-radius: 10px; padding: 20px; margin-bottom: 20px;
#                 transition: all 0.3s ease;
#             }
#             .card:hover {
#                 transform: translateY(-5px);
#             }
#             .social-link {
#                 text-decoration: none; font-size: 24px; margin: 0 10px;
#                 transition: color 0.3s;
#             }
#             .footer {
#                 text-align: center;
#                 padding: 20px 0;
#                 margin-top: 40px;
#                 border-top: 1px solid #e0e0e0;
#             }
#     """
    
#     if theme == "Dark":
#         dark_css = """
#             /* --- Dark Theme --- */
#             [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
#                 background-color: #1e1e1e;
#             }
#             .stMarkdown, .stExpander, h1, h2, h3, p, li, label { color: #ffffff; }
#             .stButton>button { background-color: #2196F3; color: white; }
#             .stButton>button:hover { background-color: #1976D2; }
#             .card, .stExpander {
#                 background-color: #2c2c2c;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
#                 border: 1px solid #444444;
#             }
#             .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
#                 background-color: #333333; color: #ffffff; border: 1px solid #555555;
#             }
#             .social-link { color: #2196F3; }
#             .social-link:hover { color: #64b5f6; }
#             .footer { border-top: 1px solid #444444; }
#         </style>
#         """
#         return base_css + dark_css
#     else: # Light Theme
#         light_css = """
#             /* --- Light Theme --- */
#             [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
#                 background-color: #f0f2f6;
#             }
#             .stMarkdown, .stExpander, h1, h2, h3, p, li, label { color: #333333; }
#             .stButton>button { background-color: #4CAF50; color: white; }
#             .stButton>button:hover { background-color: #45a049; }
#             .card, .stExpander {
#                 background-color: #ffffff;
#                 box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#                 border: 1px solid #e0e0e0;
#             }
#             .social-link { color: #4CAF50; }
#             .social-link:hover { color: #81c784; }
#         </style>
#         """
#         return base_css + light_css

# st.markdown(get_theme_css(st.session_state.theme), unsafe_allow_html=True)

# # --- Sidebar ---
# with st.sidebar:
#     theme = st.selectbox("Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)
#     if theme != st.session_state.theme:
#         st.session_state.theme = theme
#         st.rerun()
        
#     # st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.markdown("<h3>About the App</h3>", unsafe_allow_html=True)
#     st.markdown("<p>This interactive tool uses a Random Forest model to predict credit score categories (Good, Standard, Poor) based on your financial and personal data.</p>", unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)
    
# # --- Header ---
# # st.markdown("<div class='card'>", unsafe_allow_html=True)
# st.title("💳 Interactive Credit Risk Predictor")
# st.markdown("<p>Enter your details in the sections below to receive an instant credit score category prediction from our machine learning model.</p>", unsafe_allow_html=True)
# st.markdown("</div>", unsafe_allow_html=True)

# # --- Main Content: Input Forms ---
# st.header("Enter Applicant Details")

# with st.expander("👤 Personal Information", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", min_value=18, max_value=100, value=30)
#         gender = st.selectbox("Gender", ["Female", "Male", "Other"])
#         education = st.selectbox("Education Level", ["Bachelor", "High School", "Master", "PhD"])
#         employment = st.selectbox("Employment Status", ["Employed", "Retired", "Self-Employed", "Unemployed"])
#     with col2:
#         image_path = "Data_security_05.jpg"
#         if os.path.exists(image_path):
#             st.image(image_path, caption="Your Data is Secure")
#         else:
#             st.info("ℹ️ Image file 'Data_security_05.jpg' not found, skipping display.")

# with st.expander("💰 Financial Details", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         monthly_income = st.number_input("Monthly Income ($)", min_value=0.0, value=30000.0, step=1000.0, format="%.2f")
#         total_credit_limit = st.number_input("Total Credit Limit ($)", min_value=1000.0, value=50000.0, step=1000.0, format="%.2f")
#         average_transaction_amount = st.number_input("Average Transaction Amount ($)", min_value=0.0, value=1500.0, step=100.0, format="%.2f")
#     with col2:
#         credit_utilization_ratio = st.slider("Credit Utilization Ratio (%)", 0.0, 100.0, 30.0)
#         late_payments_6m = st.number_input("Late Payments (Last 6 Months)", min_value=0, value=0, step=1)
#         transaction_frequency = st.slider("Monthly Transaction Frequency", 0.0, 60.0, 5.0)

# with st.expander("📊 Behavioral Data", expanded=True):
#     col1, col2 = st.columns(2)
#     with col1:
#         login_frequency = st.slider("Monthly Login Frequency", 0.0, 30.0, 10.0)
#         credit_score_checks = st.slider("Yearly Credit Score Checks", 0, 20, 3)
#     with col2:
#         luxury_purchase_ratio = st.slider("Luxury Purchase Ratio", 0.0, 1.0, 0.1)
#         savings_rate = st.slider("Savings Rate", 0.0, 1.0, 0.2)
#         debt_to_income = st.slider("Debt to Income Ratio", 0.0, 2.0, 0.5)
        
# # --- Prediction Logic and Output ---
# if st.button("🚀 Predict Credit Score"):
#     input_dict = {
#         'age': age, 'monthly_income': monthly_income, 'credit_utilization_ratio': credit_utilization_ratio,
#         'total_credit_limit': total_credit_limit, 'late_payments_6m': late_payments_6m,
#         'transaction_frequency': transaction_frequency, 'average_transaction_amount': average_transaction_amount,
#         'login_frequency': login_frequency, 'credit_score_checks': credit_score_checks,
#         'luxury_purchase_ratio': luxury_purchase_ratio, 'savings_rate': savings_rate, 'debt_to_income': debt_to_income,
#         'gender_Male': 1 if gender == "Male" else 0, 'gender_Other': 1 if gender == "Other" else 0,
#         'education_level_High School': 1 if education == "High School" else 0,
#         'education_level_Master': 1 if education == "Master" else 0, 'education_level_PhD': 1 if education == "PhD" else 0,
#         'employment_status_Retired': 1 if employment == "Retired" else 0,
#         'employment_status_Self-Employed': 1 if employment == "Self-Employed" else 0,
#         'employment_status_Unemployed': 1 if employment == "Unemployed" else 0
#     }
    
#     input_df = pd.DataFrame([input_dict]).reindex(columns=model_columns, fill_value=0)
#     prediction = model.predict(input_df)[0]
    
#     # st.markdown("<div class='card'>", unsafe_allow_html=True)
#     st.subheader("Prediction Result")
#     st.success(f"✅ Predicted Credit Score Category: **{prediction}**")
    
#     fig = px.bar(
#         x=[prediction], y=[1], text=[prediction], title="Visualization of Prediction",
#         color_discrete_sequence=["#4CAF50" if st.session_state.theme == "Light" else "#2196F3"]
#     )
#     fig.update_layout(showlegend=False, height=250, yaxis_visible=False, title_x=0.5)
#     st.plotly_chart(fig, use_container_width=True)
#     st.markdown("</div>", unsafe_allow_html=True)

# # --- Footer ---
# st.markdown("<div class='footer'>", unsafe_allow_html=True)
# st.markdown(
#     """
#     <p>Connect with the developer:</p>
#     <a href="https://www.linkedin.com" target="_blank" class="social-link">
#         <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn" width="32" height="32">
#     </a>
#     <a href="https://www.github.com" target="_blank" class="social-link">
#         <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="32" height="32" style="filter: invert(1);">
#     </a>
#     <p style="margin-top: 15px;">© """ + str(datetime.now().year) + """ Credit Risk Predictor. All rights reserved.</p>
#     """,
#     unsafe_allow_html=True
# )
# st.markdown("</div>", unsafe_allow_html=True)




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
    page_title="Credit Risk Predictor",
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
st.title("💳 Interactive Credit Risk Predictor")
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