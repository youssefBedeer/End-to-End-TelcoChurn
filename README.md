# 📞 Telco Customer Churn Prediction - End-to-End ML Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-0194E2?logo=mlflow)](https://mlflow.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Optimized-orange)](https://xgboost.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **A production-ready machine learning system for predicting customer churn in telecommunications using XGBoost, MLflow experiment tracking, and modular pipeline architecture.**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Project Architecture](#-project-architecture)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [ML Pipeline Stages](#-ml-pipeline-stages)
- [MLflow Integration](#-mlflow-integration)
- [API Deployment](#-api-deployment)
- [AWS Deployment](#-aws-deployment)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project implements an **end-to-end machine learning solution** to predict customer churn for a telecommunications company. The system uses advanced ML techniques including hyperparameter optimization with Optuna, experiment tracking with MLflow, and a modular pipeline architecture for production deployment.

### Business Problem
Customer churn is a critical metric for telecom companies. Identifying customers likely to churn enables proactive retention strategies, reducing revenue loss and improving customer lifetime value.

### Solution
A production-grade ML pipeline that:
- Processes customer data through automated validation and transformation
- Trains optimized XGBoost models using Bayesian hyperparameter tuning
- Tracks experiments and model versions with MLflow
- Provides REST API endpoints for real-time predictions
- Supports deployment on AWS with CI/CD automation

---

## ✨ Key Features

- **🔄 Modular Pipeline Architecture**: Separate stages for ingestion, validation, transformation, and training
- **🎯 Advanced Model Optimization**: Optuna-based hyperparameter tuning for XGBoost
- **📊 Experiment Tracking**: MLflow integration for model versioning and metrics logging
- **✅ Data Validation**: Schema validation to ensure data quality
- **🔧 Configuration Management**: YAML-based configuration for easy customization
- **🚀 Multiple Deployment Options**: Flask, FastAPI, Streamlit, and Gradio support
- **☁️ Cloud Ready**: AWS deployment with Docker and GitHub Actions CI/CD
- **📈 Model Monitoring**: Comprehensive evaluation metrics and logging

---

## 🏗️ Project Architecture

```
┌─────────────────┐
│  Data Source    │
│   (CSV/API)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Ingestion  │ ──► Download & Extract Data
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Data Validation │ ──► Schema & Quality Checks
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Transformation  │ ──► Preprocessing & Feature Engineering
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Training  │ ──► XGBoost + Optuna Optimization
│   + MLflow      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Model Registry  │ ──► Versioned Models
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  API Service    │ ──► FastAPI/Flask Endpoints
│  (Prediction)   │
└─────────────────┘
```

---

## 🛠️ Tech Stack

### Machine Learning & Data Science
- **scikit-learn** `>=1.3.0` - ML utilities and preprocessing
- **XGBoost** `>=1.7.5` - Gradient boosting framework
- **LightGBM** `>=4.3.0` - Alternative gradient boosting
- **TensorFlow** `>=2.19.0` - Deep learning framework
- **Optuna** `>=3.4.0` - Hyperparameter optimization
- **pandas** `>=2.0.0` - Data manipulation
- **numpy** `>=1.25.0` - Numerical computing

### MLOps & Tracking
- **MLflow** `>=2.2.2` - Experiment tracking and model registry
- **DVC** `>=2.50.0` - Data version control
- **DagsHub** - Remote MLflow tracking server

### Web Frameworks & APIs
- **FastAPI** `>=0.110.0` - Modern async API framework *(Planned)*
- **Flask** `>=2.3.0` - Lightweight web framework
- **Uvicorn** `>=0.29.0` - ASGI server for FastAPI
- **Streamlit** `>=1.36.0` - Interactive dashboards
- **Gradio** `>=4.29.0` - ML model interfaces

### DevOps & Deployment
- **Docker** - Containerization
- **GitHub Actions** - CI/CD automation
- **AWS EC2** - Cloud compute
- **AWS ECR** - Container registry

---

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- Git
- (Optional) Conda for environment management

### Step 1: Clone the Repository

```bash
git clone https://github.com/youssefBedeer/End-to-End-TelcoChurn.git
cd End-to-End-TelcoChurn
```

### Step 2: Create Virtual Environment

**Option A: Using Conda**
```bash
conda create -n telco-churn python=3.8 -y
conda activate telco-churn
```

**Option B: Using venv**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Training the Model

Run the complete ML pipeline:

```bash
python main.py
```

This executes all pipeline stages:
1. **Data Ingestion** - Downloads and extracts the dataset
2. **Data Validation** - Validates schema and data quality
3. **Data Transformation** - Preprocesses features and splits data
4. **Model Training** - Trains XGBoost with hyperparameter optimization

### Running the Web Application

**Flask Application** (Current)
```bash
python app.py
```

**FastAPI Application** (Planned)
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Streamlit Dashboard**
```bash
streamlit run app.py
```

**Gradio Interface**
```bash
python app.py  # If using Gradio
```

### Making Predictions

Once the API is running, send POST requests with customer data:

```python
import requests

# Example customer data
customer_data = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": "1397.475"
}

response = requests.post("http://localhost:8000/predict", json=customer_data)
print(response.json())
```

---

## 📁 Project Structure

```
End-to-End-TelcoChurn/
│
├── artifacts/                      # Generated artifacts (models, data, etc.)
│   ├── data_ingestion/            # Raw and extracted data
│   ├── data_validation/           # Validation reports
│   ├── data_transformation/       # Preprocessed data and transformers
│   └── model_trainer/             # Trained models
│
├── config/                         # Configuration files
│   └── config.yaml                # Main configuration
│
├── src/                           # Source code
│   ├── components/                # Pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/                  # Pipeline stages
│   │   ├── stage_01_data_ingestion.py
│   │   ├── stage_02_data_validation.py
│   │   ├── stage_03_data_transformation.py
│   │   └── stage_04_model_trainer.py
│   │
│   ├── config/                    # Configuration manager
│   ├── entity/                    # Data classes and entities
│   ├── utils/                     # Utility functions
│   └── __init__.py               # Logging and exception handling
│
├── research/                      # Jupyter notebooks for experimentation
├── templates/                     # HTML templates for web UI
├── logs/                         # Application logs
│
├── main.py                       # Main training pipeline
├── app.py                        # Web application (Flask/FastAPI)
├── params.yaml                   # Hyperparameter search space
├── schema.yaml                   # Data schema definition
├── best_params.yaml              # Optimized hyperparameters
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker configuration
├── setup.py                      # Package setup
└── README.md                     # This file
```

---

## 🔄 ML Pipeline Stages

### 1️⃣ Data Ingestion
- Downloads dataset from remote source
- Extracts and stores raw data
- **Output**: `artifacts/data_ingestion/Telco-Customer-Churn.csv`

### 2️⃣ Data Validation
- Validates column names and data types against schema
- Checks for data quality issues
- **Output**: `artifacts/data_validation/status.txt`

### 3️⃣ Data Transformation
- Handles missing values and outliers
- Encodes categorical features
- Scales numerical features
- Splits data into train/test sets
- **Output**: Preprocessor, train/test arrays

### 4️⃣ Model Training
- Hyperparameter optimization using Optuna
- Trains XGBoost classifier
- Logs metrics and parameters to MLflow
- Saves best model
- **Output**: `artifacts/model_trainer/model.joblib`

---

## 📊 MLflow Integration

### Local MLflow UI

Start the MLflow tracking UI:

```bash
mlflow ui
```

Access at: `http://localhost:5000`

### Remote Tracking with DagsHub

Set environment variables for remote tracking:

**Windows (CMD)**
```cmd
set MLFLOW_TRACKING_URI=https://dagshub.com/youssefBedeer/End-to-End-TelcoChurn.mlflow
set MLFLOW_TRACKING_USERNAME=youssefBedeer
set MLFLOW_TRACKING_PASSWORD=your_token_here
```

**Linux/Mac**
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/youssefBedeer/End-to-End-TelcoChurn.mlflow
export MLFLOW_TRACKING_USERNAME=youssefBedeer
export MLFLOW_TRACKING_PASSWORD=your_token_here
```

### MLflow Features Used
- **Experiment Tracking**: Log parameters, metrics, and artifacts
- **Model Registry**: Version control for trained models
- **Artifact Storage**: Store models, plots, and data
- **Comparison**: Compare multiple runs and experiments

---

## 🌐 API Deployment

### FastAPI Implementation (Planned)

The project will support FastAPI for production-grade API deployment:

**Features:**
- ✅ Async request handling
- ✅ Automatic API documentation (Swagger/ReDoc)
- ✅ Data validation with Pydantic
- ✅ High performance with Uvicorn
- ✅ CORS support for web integration

**Endpoints:**
- `GET /` - Health check
- `POST /predict` - Single prediction
- `POST /predict/batch` - Batch predictions
- `GET /model/info` - Model metadata

**Example FastAPI Structure:**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Telco Churn Prediction API")

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    # ... other features

@app.post("/predict")
async def predict_churn(customer: CustomerData):
    # Load model and make prediction
    return {"churn_probability": 0.75, "will_churn": True}
```

---

## ☁️ AWS Deployment

### Prerequisites
1. AWS Account
2. AWS CLI configured
3. Docker installed

### Deployment Steps

#### 1. Create IAM User
Create an IAM user with the following policies:
- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`

#### 2. Create ECR Repository
```bash
aws ecr create-repository --repository-name telco-churn
```

Save the repository URI (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com/telco-churn`)

#### 3. Launch EC2 Instance
- Choose Ubuntu AMI
- Instance type: t2.medium or larger
- Configure security groups (open ports 22, 80, 8000)

#### 4. Install Docker on EC2
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

#### 5. Configure GitHub Secrets
Add the following secrets to your GitHub repository:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g., `us-east-1`)
- `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
- `ECR_REPOSITORY_NAME` (e.g., `telco-churn`)

#### 6. Setup Self-Hosted Runner
In GitHub repository:
1. Go to Settings → Actions → Runners
2. Click "New self-hosted runner"
3. Follow instructions to configure on EC2

#### 7. Deploy via GitHub Actions
Push to main branch to trigger automatic deployment:
```bash
git push origin main
```

---

## ⚙️ Configuration

### config.yaml
Main configuration file for pipeline stages:
```yaml
artifacts_root: artifacts

data_ingestion:
  root_dir: artifacts/data_ingestion
  source_url: <data_source_url>
  
model_trainer:
  root_dir: artifacts/model_trainer
  THRESHOLD: 0.30  # Classification threshold
```

### params.yaml
Hyperparameter search space for Optuna:
```yaml
xgboost_params:
  n_estimators:
    type: int
    low: 300
    high: 800
  learning_rate:
    type: float
    low: 0.01
    high: 0.2
  max_depth:
    type: int
    low: 3
    high: 10
```

### schema.yaml
Data schema validation:
```yaml
COLUMNS:
  gender: object
  SeniorCitizen: int64
  tenure: int64
  MonthlyCharges: float64
  Churn: object

TARGET_COLUMN:
  name: Churn
```

---

## 🔍 Model Performance

The model is optimized using Optuna with the following metrics:
- **Accuracy**: Overall prediction accuracy
- **Precision**: Precision for churn class
- **Recall**: Recall for churn class
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Area under the ROC curve
- **Log Loss**: Logarithmic loss

Custom threshold (default: 0.30) is used to optimize for business objectives.

---

## 🧪 Testing

Run tests (when implemented):
```bash
pytest tests/
```

---

## 📝 Development Workflow

1. **Update Configuration**: Modify `config.yaml`, `schema.yaml`, `params.yaml`
2. **Update Entities**: Define data classes in `src/entity/`
3. **Update Config Manager**: Modify `src/config/configuration.py`
4. **Update Components**: Implement logic in `src/components/`
5. **Update Pipelines**: Create pipeline stages in `src/pipeline/`
6. **Update Main**: Integrate stages in `main.py`
7. **Update App**: Add API endpoints in `app.py`

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Youssef Bedeer**
- GitHub: [@youssefBedeer](https://github.com/youssefBedeer)
- DagsHub: [youssefBedeer](https://dagshub.com/youssefBedeer)

---

## 🙏 Acknowledgments

- Dataset: Telco Customer Churn Dataset
- MLflow for experiment tracking
- Optuna for hyperparameter optimization
- XGBoost team for the excellent gradient boosting library

---

## 📚 Additional Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Optuna Documentation](https://optuna.readthedocs.io/)

---

## 🗺️ Roadmap

- [x] Basic ML pipeline implementation
- [x] MLflow integration
- [x] Hyperparameter optimization with Optuna
- [x] Docker containerization
- [x] AWS deployment setup
- [ ] **FastAPI implementation** *(In Progress)*
- [ ] Batch prediction endpoints
- [ ] Model monitoring dashboard
- [ ] A/B testing framework
- [ ] Automated retraining pipeline
- [ ] Feature importance visualization
- [ ] SHAP values for model interpretability

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ by Youssef Bedeer

</div>