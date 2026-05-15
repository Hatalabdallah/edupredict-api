# ============================================
# SECTION 1: IMPORTS AND PAGE CONFIGURATION
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from sklearn.ensemble import GradientBoostingClassifier

# Page configuration - this MUST be the first Streamlit command
st.set_page_config(
    page_title="EduPredict - Student Success Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)





# ============================================
# SECTION 2: LOAD THE TRAINED MODEL AND FEATURES
# ============================================

@st.cache_resource
def load_model():
    """Load the trained Gradient Boosting model from disk."""
    model = joblib.load('student_dropout_model.pkl')
    return model

@st.cache_data
def load_features():
    """Load the feature list from disk."""
    with open('class_features.json', 'r') as f:
        features = json.load(f)
    return features

# Load model and features
model = load_model()
feature_list = load_features()




# ============================================
# SECTION 3: SIDEBAR - USER INPUT FORM
# ============================================

st.sidebar.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=80)
st.sidebar.title("🎓 EduPredict")
st.sidebar.markdown("---")
st.sidebar.subheader("📋 Student Information")

# --- Personal Details ---
st.sidebar.markdown("### 👤 Personal Details")
age = st.sidebar.number_input(
    "Age at Enrollment",
    min_value=17,
    max_value=70,
    value=20,
    step=1,
    help="Student's age when they enrolled"
)

gender = st.sidebar.selectbox(
    "Gender",
    options=["Female", "Male"],
    index=0,
    help="Select the student's gender"
)
# Convert gender to numeric (0=Female, 1=Male) to match training data
gender_numeric = 0 if gender == "Female" else 1

# --- Financial Information ---
st.sidebar.markdown("### 💰 Financial Information")
scholarship = st.sidebar.selectbox(
    "Scholarship Holder",
    options=["No", "Yes"],
    index=0,
    help="Does the student have a scholarship?"
)
scholarship_numeric = 1 if scholarship == "Yes" else 0

tuition = st.sidebar.selectbox(
    "Tuition Fees Up to Date",
    options=["No", "Yes"],
    index=1,
    help="Are tuition fees fully paid?"
)
tuition_numeric = 1 if tuition == "Yes" else 0

debtor = st.sidebar.selectbox(
    "Debtor Status",
    options=["No", "Yes"],
    index=0,
    help="Is the student a debtor from previous school?"
)
debtor_numeric = 1 if debtor == "Yes" else 0

# --- Academic Performance ---
st.sidebar.markdown("### 📚 Academic Performance")

sem1_approved = st.sidebar.slider(
    "1st Semester - Units Approved",
    min_value=0,
    max_value=20,
    value=5,
    step=1,
    help="Number of curricular units the student passed in the first semester"
)

sem1_grade = st.sidebar.slider(
    "1st Semester - Average Grade",
    min_value=0.0,
    max_value=20.0,
    value=12.0,
    step=0.1,
    help="Average grade in the first semester (0-20 scale)"
)

sem2_approved = st.sidebar.slider(
    "2nd Semester - Units Approved",
    min_value=0,
    max_value=20,
    value=5,
    step=1,
    help="Number of curricular units the student passed in the second semester"
)

sem2_grade = st.sidebar.slider(
    "2nd Semester - Average Grade",
    min_value=0.0,
    max_value=20.0,
    value=12.0,
    step=0.1,
    help="Average grade in the second semester (0-20 scale)"
)

st.sidebar.markdown("---")





# ============================================
# SECTION 4: MAIN DASHBOARD AREA
# ============================================

# --- Header ---
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=100)
with col2:
    st.title("EduPredict: Student Success Analytics")
    st.markdown("*An AI-powered early warning system for student dropout prevention*")

st.markdown("---")

# --- Welcome / Instructions ---
st.markdown("""
### 📊 How to Use This Tool
1. **Enter student details** using the sidebar form on the left.
2. **Click the 'Predict Student Status' button** below.
3. **View the AI prediction** and risk assessment instantly.
""")

st.markdown("---")

# --- Prediction Button ---
st.markdown("### 🔮 Make a Prediction")
predict_button = st.button(
    "Predict Student Status",
    type="primary",
    use_container_width=True
)

# --- Prediction Logic ---
if predict_button:
    # Create input array in the exact order of feature_list
    input_data = pd.DataFrame([[
        age,
        gender_numeric,
        scholarship_numeric,
        tuition_numeric,
        debtor_numeric,
        sem1_approved,
        sem1_grade,
        sem2_approved,
        sem2_grade
    ]], columns=feature_list)
    
    # Show a spinner while processing
    with st.spinner("🧠 AI Analyzing Student Profile..."):
        # Get prediction
        prediction = model.predict(input_data)[0]
        # Get probabilities
        probabilities = model.predict_proba(input_data)[0]
    
    # Create a mapping for display
    status_map = {
        "Graduate": "✅ Graduate — Low Risk",
        "Dropout": "🚨 Dropout — High Risk — Intervention Required",
        "Enrolled": "⚠️ Enrolled — Monitor Status"
    }
    
    color_map = {
        "Graduate": "#10B981",  # Green
        "Dropout": "#EF4444",   # Red
        "Enrolled": "#F59E0B"   # Amber
    }
    
    emoji_map = {
        "Graduate": "✅",
        "Dropout": "🚨",
        "Enrolled": "⚠️"
    }
    
    # Display result with colored card
    st.markdown("---")
    st.markdown("### 📋 Prediction Result")
    
    # Create three columns for the result card
    result_col1, result_col2, result_col3 = st.columns([1, 2, 1])
    
    with result_col2:
        # Colored card using custom HTML
        color = color_map[prediction]
        emoji = emoji_map[prediction]
        
        st.markdown(f"""
        <div style="
            background-color: {color}15;
            border: 2px solid {color};
            border-radius: 16px;
            padding: 30px;
            text-align: center;
            margin: 10px 0;
        ">
            <h1 style="margin: 0; font-size: 60px;">{emoji}</h1>
            <h2 style="color: {color}; margin: 10px 0;">{status_map[prediction]}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # --- Probability Breakdown ---
    st.markdown("### 📊 Prediction Confidence")
    
    prob_col1, prob_col2, prob_col3 = st.columns(3)
    
    classes = model.classes_
    prob_dict = dict(zip(classes, probabilities))
    
    with prob_col1:
        st.metric(
            label="Graduate",
            value=f"{prob_dict.get('Graduate', 0):.1%}",
            delta=None
        )
    with prob_col2:
        st.metric(
            label="Dropout",
            value=f"{prob_dict.get('Dropout', 0):.1%}",
            delta=None
        )
    with prob_col3:
        st.metric(
            label="Enrolled",
            value=f"{prob_dict.get('Enrolled', 0):.1%}",
            delta=None
        )
    
    st.markdown("")
    st.info("💡 The model assigns a probability to each possible outcome. The highest probability determines the final prediction.")

else:
    # Shown when the button hasn't been clicked yet
    st.markdown("""
    <div style="
        background-color: #1E293B;
        border: 2px dashed #475569;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        margin: 20px 0;
    ">
        <h3 style="color: #94A3B8;">👈 Enter student details in the sidebar and click 'Predict Student Status' to see results here</h3>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("### 🔍 Model Insights: Top Predictors of Student Success")
st.markdown("Based on feature importance analysis from the trained Gradient Boosting model:")

# Get feature importance from the model
importances = model.feature_importances_
importance_df = pd.DataFrame({
    'Feature': feature_list,
    'Importance': importances
}).sort_values('Importance', ascending=False)

# Display as a horizontal bar chart
st.bar_chart(importance_df.set_index('Feature'))

st.markdown("---")
st.caption("© 2026 EduPredict | Built with Streamlit & scikit-learn | YMCA Institute Uganda")
st.caption(f"Model: Gradient Boosting Classifier | Features used: {len(feature_list)} | Training samples: 3,539")