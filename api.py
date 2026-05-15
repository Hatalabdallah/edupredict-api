# ============================================
# SECTION 1: IMPORTS
# ============================================

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import uvicorn

# ============================================
# SECTION 2: LOAD MODEL AND FEATURES
# ============================================

# Load the trained model
model = joblib.load('student_dropout_model.pkl')

# Load the feature list
with open('class_features.json', 'r') as f:
    feature_list = json.load(f)

print(f"✅ Model loaded successfully. Features: {len(feature_list)}")
print(f"   Model classes: {model.classes_}")

# ============================================
# SECTION 3: DEFINE REQUEST STRUCTURE
# ============================================

class StudentData(BaseModel):
    age: int
    gender: int
    scholarship: int
    tuition_up_to_date: int
    debtor: int
    sem1_approved: int
    sem1_grade: float
    sem2_approved: int
    sem2_grade: float

# ============================================
# SECTION 4: CREATE THE API APP
# ============================================

app = FastAPI(
    title="EduPredict API",
    description="Student Dropout Prediction API - YMCA Institute Uganda",
    version="1.0.0"
)

# ============================================
# SECTION 5: DEFINE THE PREDICTION ENDPOINT
# ============================================

@app.post("/predict")
def predict(student: StudentData):
    """
    Predict student outcome based on demographic, financial, and academic data.
    Returns the predicted status and probabilities for each class.
    """
    # Convert input to DataFrame in the exact order of feature_list
    input_data = pd.DataFrame([[
        student.age,
        student.gender,
        student.scholarship,
        student.tuition_up_to_date,
        student.debtor,
        student.sem1_approved,
        student.sem1_grade,
        student.sem2_approved,
        student.sem2_grade
    ]], columns=feature_list)
    
    # Get prediction
    prediction = model.predict(input_data)[0]
    
    # Get probabilities
    probabilities = model.predict_proba(input_data)[0]
    prob_dict = dict(zip(model.classes_, probabilities.tolist()))
    
    # Return as JSON
    return {
        "prediction": prediction,
        "probabilities": {
            "Graduate": prob_dict.get("Graduate", 0),
            "Dropout": prob_dict.get("Dropout", 0),
            "Enrolled": prob_dict.get("Enrolled", 0)
        },
        "status": "success"
    }

# ============================================
# SECTION 6: HEALTH CHECK ENDPOINT
# ============================================

@app.get("/")
def root():
    return {
        "message": "EduPredict API is running",
        "model": "Gradient Boosting Classifier",
        "features_used": len(feature_list),
        "training_samples": 3539,
        "accuracy": "73.22%"
    }

# ============================================
# SECTION 7: RUN THE SERVER
# ============================================

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)