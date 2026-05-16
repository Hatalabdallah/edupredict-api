# 🎓 EduPredict — Student Success Analytics

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Status-Production%20Ready-10B981?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/Accuracy-73.22%25-4F46E5?style=for-the-badge" alt="Accuracy" />
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.136-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Streamlit-1.57-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/scikit--learn-1.7.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Deployed-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white" alt="Railway" />
  <img src="https://img.shields.io/badge/Frontend-Lovable-7C3AED?style=for-the-badge&logo=lovable&logoColor=white" alt="Lovable" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <img src="https://img.icons8.com/fluency/96/graduation-cap.png" alt="EduPredict Logo" width="120" />
</p>

<h1 align="center">EduPredict: Student Success Analytics</h1>
<h3 align="center">🚀 An AI-Powered Early Warning System for Student Dropout Prevention</h3>

<p align="center">
  <a href="https://student-star-guardian.lovable.app"><strong>🌐 Live Demo</strong></a> •
  <a href="https://edupredict-api-production.up.railway.app"><strong>🔗 API Endpoint</strong></a> •
  <a href="https://edupredict-api-production.up.railway.app/docs"><strong>📚 API Docs</strong></a> •
  <a href="#-quick-start"><strong>⚡ Quick Start</strong></a>
</p>



## 📖 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Model Performance](#-model-performance)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [Project Structure](#-project-structure)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)



## 📋 Overview

**EduPredict** is a production-grade machine learning application that predicts student dropout risk in higher education. Built for **YMCA Institute Uganda** as part of the **BIT3203 Machine Learning Application Development** semester project, it combines supervised learning, unsupervised learning, and ensemble methods into a fully deployed system.

### 🎯 The Problem
High dropout rates cost institutions revenue and students their futures. Traditional intervention is **reactive** — EduPredict makes it **proactive**.

### 💡 The Solution
An AI system that:
- 🔮 **Predicts** student outcomes (Graduate / Dropout / Enrolled) with **73.22% accuracy**
- 📊 **Identifies** key risk factors via feature importance analysis
- 🎨 **Visualizes** results through multiple professional interfaces
- 🌐 **Deploys** as a publicly accessible web application



## 🏗️ Architecture

```
┌─────────────────────────┐         HTTP POST/GET         ┌──────────────────────────┐
│   🎨 Lovable Frontend   │ ◄───────────────────────────► │   ⚡ FastAPI Backend      │
│   (React + TypeScript)  │                               │   (Python 3.13)          │
│                         │                               │                          │
│   • Glassmorphic UI     │                               │   • Model Inference      │
│   • Form Validation     │                               │   • /predict endpoint    │
│   • API Health Check    │                               │   • / health check       │
│   • Responsive Design   │                               │   • CORS Enabled         │
└─────────────────────────┘                               └──────────────────────────┘
                                                                      │
                                                                      │ Loads
                                                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           🧠 Trained ML Model                                │
│                                                                             │
│   • Algorithm: Gradient Boosting Classifier (100 estimators)                │
│   • Accuracy: 73.22%  |  Dropout Precision: 80%  |  Recall: 73%            │
│   • Features: 9 (Demographic + Financial + Academic)                        │
│   • Training Samples: 3,539  |  Dataset: UCI Repository (4,424 records)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🖥️ Local Prototypes
Additionally, the project includes:
- **🐍 Python Script** — `predict_student_status()` function for inline inference
- **🎯 Streamlit Dashboard** — Interactive local web app at `http://localhost:8501`
- **📓 Jupyter Notebook** — Full EDA, model training, and evaluation pipeline



## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-|--||
| **ML Core** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) | Model training, evaluation, data processing |
| **Backend API** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) ![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?logo=uvicorn&logoColor=white) ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white) | REST API, request validation, model serving |
| **Frontend** | ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) ![Lovable](https://img.shields.io/badge/Lovable-7C3AED) | Web dashboard, AI-generated UI |
| **Local App** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) | Interactive local dashboard |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB) | EDA charts, feature importance plots |
| **Deployment** | ![Railway](https://img.shields.io/badge/Railway-0B0D0E?logo=railway&logoColor=white) ![Lovable Cloud](https://img.shields.io/badge/Lovable_Cloud-7C3AED) | Backend hosting, frontend hosting |
| **Version Control** | ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) | Source code management |
| **Environment** | ![Venv](https://img.shields.io/badge/venv-3776AB?logo=python&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?logo=visual-studio-code&logoColor=white) | Development environment |



## ✨ Key Features

### 🤖 Machine Learning
- ✅ **Regression**: Linear Regression predicting Admission Grade (R²=0.36)
- ✅ **Classification**: Random Forest predicting Dropout/Graduate/Enrolled (73.22% accuracy)
- ✅ **Unsupervised Learning**: K-Means Clustering (3 student profiles via Elbow Method)
- ✅ **Ensemble Methods**: Random Forest (Bagging) + Gradient Boosting (Boosting)
- ✅ **Feature Importance**: 2nd Semester Approved Units identified as #1 predictor

### 🎨 User Interfaces
- 🌐 **Public Web App**: Lovable-built React frontend with glassmorphic dark UI
- 🖥️ **Local Dashboard**: Streamlit app with interactive sidebar inputs
- 📓 **Development Notebook**: Full Jupyter Notebook with all models and visualizations
- 🧪 **API Playground**: Auto-generated FastAPI docs at `/docs`

### 🔧 Engineering
- 🔄 **Auto-Deploy**: GitHub push triggers automatic Railway redeployment
- 🌍 **CORS Enabled**: API accessible from any domain
- 🩺 **Health Check**: Real-time API status monitoring
- ✅ **Input Validation**: Form-level validation before API calls
- 📊 **Probability Display**: Confidence scores for all three outcome classes



## 📊 Model Performance

### Classification Report (Random Forest — 100 Estimators)

| Class | Precision | Recall | F1-Score | Support |
|-|--|--|-||
| **Dropout** | 0.80 | 0.73 | 0.76 | 316 |
| **Enrolled** | 0.44 | 0.28 | 0.35 | 151 |
| **Graduate** | 0.75 | 0.89 | 0.82 | 418 |
| **Accuracy** | | | **73.22%** | 885 |
| **Macro Avg** | 0.66 | 0.64 | 0.64 | 885 |
| **Weighted Avg** | 0.71 | 0.73 | 0.72 | 885 |

### Key Insights
- 🎯 **Dropout Detection Precision: 80%** — When the model flags a student, it's right 4 out of 5 times
- 🛡️ **Graduate Detection Recall: 89%** — Excellent at confirming successful students
- ⚠️ **Enrolled Class F1: 0.35** — Transitional students are inherently harder to classify

### Top 5 Predictors of Student Outcome
1. 🥇 **2nd Semester Units Approved** (Highest)
2. 🥈 **1st Semester Units Approved**
3. 🥉 **2nd Semester Grade**
4. **1st Semester Grade**
5. **Tuition Fees Up to Date**

> 💡 **Academic momentum is the dominant factor.** By the end of the second semester, a student's trajectory is largely determined.



## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- Git
- GitHub account

### Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/Hatalabdallah/edupredict-api.git
cd edupredict-api

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py

# OR run the FastAPI server
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Test the API Locally

```bash
# Health check
curl http://localhost:8000/

# Prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 20,
    "gender": 0,
    "scholarship": 1,
    "tuition_up_to_date": 1,
    "debtor": 0,
    "sem1_approved": 5,
    "sem1_grade": 12.0,
    "sem2_approved": 6,
    "sem2_grade": 13.0
  }'
```



## 🚀 Deployment

### Production URLs

| Resource | URL | Status |
|-|--|--|
| 🌐 **Lovable Frontend** | [student-star-guardian.lovable.app](https://student-star-guardian.lovable.app) | 🟢 Live |
| ⚡ **FastAPI Backend** | [edupredict-api-production.up.railway.app](https://edupredict-api-production.up.railway.app) | 🟢 Live |
| 📚 **API Documentation** | [Swagger UI](https://edupredict-api-production.up.railway.app/docs) | 🟢 Auto-Generated |
| 📦 **GitHub Repository** | [Hatalabdallah/edupredict-api](https://github.com/Hatalabdallah/edupredict-api) | 📦 Public |

### Deployment Architecture
- **Backend**: Railway (auto-deploys from `main` branch on push)
- **Frontend**: Lovable Cloud (connected to API endpoint)
- **CI/CD**: GitHub → Railway automatic deployment pipeline



## 📁 Project Structure

```
edupredict-api/
│
├── 🧠 ML Models & Data
│   ├── Student_Dropout_Analysis.ipynb    # Jupyter Notebook (EDA + all models)
│   ├── student_dropout_model.pkl         # Trained Gradient Boosting model
│   ├── class_features.json               # Feature list for input ordering
│   └── data.csv                          # UCI Repository dataset (4,424 records)
│
├── 🔧 Backend
│   ├── api.py                            # FastAPI server with /predict endpoint
│   └── requirements.txt                  # Python dependencies
│
├── 🎨 Frontend & Local Apps
│   ├── app.py                            # Streamlit dashboard
│   └── (Lovable frontend)                # Deployed separately on Lovable Cloud
│
├── 🚀 Deployment
│   └── Procfile                          # Railway deployment configuration
│
└── 📄 Documentation
    ├── README.md                         # You are here! 👋
    ├── LICENSE                           # MIT License
    └── CONTRIBUTING.md                   # Contribution guidelines
```



## 📡 API Reference

### Base URL
```
https://edupredict-api-production.up.railway.app
```

### Endpoints

#### `GET /` — Health Check
Returns API status and model information.

**Response:**
```json
{
  "message": "EduPredict API is running",
  "model": "Gradient Boosting Classifier",
  "features_used": 9,
  "training_samples": 3539,
  "accuracy": "73.22%"
}
```

#### `POST /predict` — Predict Student Outcome
Accepts student data and returns prediction with probabilities.

**Request Body:**
```json
{
  "age": 20,
  "gender": 0,
  "scholarship": 1,
  "tuition_up_to_date": 1,
  "debtor": 0,
  "sem1_approved": 5,
  "sem1_grade": 12.0,
  "sem2_approved": 6,
  "sem2_grade": 13.0
}
```

**Response:**
```json
{
  "prediction": "Graduate",
  "probabilities": {
    "Graduate": 0.7906,
    "Dropout": 0.0411,
    "Enrolled": 0.1682
  },
  "status": "success"
}
```

**Full API Documentation:** [Swagger UI](https://edupredict-api-production.up.railway.app/docs)



## 👥 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Steps
1. 🍴 Fork the repository
2. 🌿 Create a feature branch: `git checkout -b feature/amazing-feature`
3. 💾 Commit changes: `git commit -m 'Add amazing feature'`
4. 📤 Push to branch: `git push origin feature/amazing-feature`
5. 🔄 Open a Pull Request



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.



## 📞 Contact

### 👨‍💻 Developer

**Ddumba Abdallah Kato**

<p align="left">
  <a href="https://ddumba.kyakabi.com"><img src="https://img.shields.io/badge/Portfolio-ddumba.kyakabi.com-4F46E5?style=flat-square&logo=safari&logoColor=white" alt="Portfolio" /></a>
  <a href="https://github.com/Hatalabdallah"><img src="https://img.shields.io/badge/GitHub-Hatalabdallah-181717?style=flat-square&logo=github" alt="GitHub" /></a>
  <a href="https://x.com/Hatalabdallah"><img src="https://img.shields.io/badge/Twitter-@Hatalabdallah-1DA1F2?style=flat-square&logo=twitter&logoColor=white" alt="Twitter" /></a>
  <a href="https://www.linkedin.com/in/ddumbaka/"><img src="https://img.shields.io/badge/LinkedIn-ddumbaka-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://wa.me/256701019242"><img src="https://img.shields.io/badge/WhatsApp-+256701019242-25D366?style=flat-square&logo=whatsapp&logoColor=white" alt="WhatsApp" /></a>
</p>

### 🏢 Company

**Kyakabi Group** — [kyakabi.com](https://kyakabi.com)

> *"We offer end-to-end software and website solutions for various businesses and clients. We provide custom software solutions, professional website designs, ERP software development, web application development, e-commerce website development, mobile app development and high-end corporate training services."*

### 👤 Professional Profile

**AI Platform Engineer | Production AI & Infrastructure**

I build the **"Engines"** that allow AI to survive in production. While much of the industry focuses on prompt engineering, I focus on the **"Day 2" reality**: inference cost optimization, RAG pipeline latency, Kubernetes cluster scaling for agentic workloads.

**Focus Areas:**
- 🏗️ **AI Infrastructure**: Auto-scaling clusters for GPU-intensive workloads
- ⚡ **Inference Efficiency**: vLLM and TensorRT-LLM for token cost optimization
- 🔍 **High-Fidelity RAG**: Hybrid search systems for accurate retrieval
- 🛡️ **Automated Governance**: Guardrails and observability in CI/CD pipelines
- ☁️ **Platform Engineering**: AWS (EKS, Bedrock), Kubernetes, Terraform, ArgoCD



## 🙏 Acknowledgments

- 📊 **Dataset**: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Predict+students%27+dropout+and+academic+success) — Realinho, V., Vieira Martins, M., et al. (2021)
- 🧠 **ML Framework**: [scikit-learn](https://scikit-learn.org/)
- ⚡ **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- 🎨 **Frontend Builder**: [Lovable](https://lovable.dev/)
- 🚀 **Backend Hosting**: [Railway](https://railway.com/)
- 🖥️ **Local Dashboard**: [Streamlit](https://streamlit.io/)
- 🏫 **Academic Context**: YMCA Institute Uganda — BIT3203 Machine Learning Application Development
- 📈 **Visualization**: [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)



<p align="center">
  <sub>Built with ❤️ by <a href="https://github.com/Hatalabdallah">Ddumba Abdallah Kato</a> — AI Platform Engineer at <a href="https://kyakabi.com">Kyakabi Group</a></sub>
</p>

<p align="center">
  <sub>© 2026 EduPredict. All rights reserved.</sub>
</p>

<!-- HASHTAGS -->
<p align="center">
  <sub>
    #MachineLearning #AI #StudentSuccess #DropoutPrevention #FastAPI #Streamlit #Python #scikit-learn #Education #EdTech #DataScience #MLOps #Railway #Lovable #React #TypeScript #Uganda #YMCA #HigherEducation #PredictiveAnalytics #GradientBoosting #RandomForest #KMeans #Clustering #EDA #JupyterNotebook #API #FullStack #CloudDeployment
  </sub>
</p>
```
