
---

#  End-to-End MLOps Pipeline – Sentiment Analysis Project

This repository implements a **complete end-to-end MLOps workflow** for **sentiment classification** using a **Logistic Regression model**.
It covers everything from **data ingestion → model training → evaluation → model registry → deployment → monitoring**, all integrated with **MLflow, DVC, Docker, Kubernetes, and Prometheus**.

---

##  Project Overview

This project demonstrates how to:

* Version datasets and code using **DVC**
* Track experiments using **MLflow**
* Automatically register and promote models
* Serve models in production using **Flask + Gunicorn**
* Deploy on **Kubernetes**
* Monitor model and API metrics using **Prometheus**
* Generate developer documentation using **Sphinx**

---

## ⚙️ Tech Stack

| Category                | Tools / Frameworks                  |
| ----------------------- | ----------------------------------- |
| **Language**            | Python 3.11                         |
| **Data Versioning**     | DVC                                 |
| **Experiment Tracking** | MLflow + DAGsHub                    |
| **Modeling**            | Scikit-learn, NLTK                  |
| **Deployment**          | Flask, Gunicorn, Docker, Kubernetes |
| **Monitoring**          | Prometheus                          |
| **Documentation**       | Sphinx                              |
| **Cloud**               | AWS S3, ECR                         |
| **Code Quality**        | Flake8, Tox                         |
| **Automation**          | Makefile, setup.py                  |

---

##  Project Structure

```
.
├── .dvc/                       # DVC metadata
├── .github/                    # CI/CD workflows (if configured)
├── docs/                       # Sphinx documentation
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   ├── Makefile
│   └── make.bat
│
├── flask_app/                  # Model serving API
│   ├── app.py
│   ├── load_model_test.py
│   ├── preprocessing_utility.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
├── models/                     # Trained models and vectorizers
│   └── vectorizer.pkl
│
├── notebooks/                  # Experiments & analysis
│   ├── data.csv
│   ├── IMDB.csv
│   ├── exp1.ipynb
│   ├── exp2_bow_vs_tfidf.py
│   └── exp3_lor_bow_hp.py
│
├── references/                 # Reference documents / data schema
│   └── .gitkeep
│
├── reports/                    # Reports and metrics
│   ├── figures/
│   └── experiment_info.json
│
├── scripts/                    # Automation scripts
│   └── promote_model.py
│
├── src/                        # Core ML pipeline source code
│   ├── connections/            # Database & S3 connectors
│   │   ├── config.json
│   │   ├── s3_connection.py
│   │   └── ssms_connection.py
│   │
│   ├── data/                   # Data ingestion and preprocessing
│   │   ├── data_ingestion.py
│   │   └── data_preprocessing.py
│   │
│   ├── features/               # Feature engineering scripts
│   │   └── feature_engineering.py
│   │
│   ├── logger/                 # Logging setup
│   │   └── __init__.py
│   │
│   └── model/                  # Model building, evaluation, registry
│       ├── model_building.py
│       ├── model_evaluation.py
│       ├── predict_model.py
│       └── register_model.py
│
├── tests/                      # Unit / integration tests
│   └── test_environment.py
│
├── .dvcignore
├── .gitignore
├── Dockerfile
├── deployment.yaml             # Kubernetes Deployment + Service
├── dvc.yaml                    # DVC pipeline definition
├── dvc.lock
├── LICENSE
├── Makefile
├── params.yaml                 # Pipeline parameters (test_size, etc.)
├── projectflow.txt             # Visual project workflow
├── README.md                   # 
├── requirements.txt
├── setup.py
├── test_environment.py
└── tox.ini
```

---

##  MLOps Pipeline Stages

### **1️⃣ Data Ingestion**

* Loads dataset from AWS S3 or CSV.
* Splits into train/test (based on `params.yaml`).
* Stores raw data under `data/raw/`.

### **2️⃣ Data Preprocessing**

* Cleans and normalizes text:

  * Lowercasing
  * Removing punctuation, numbers, URLs
  * Stopword removal
  * Lemmatization
* Outputs processed data to `data/interim/`.

### **3️⃣ Feature Engineering**

* Converts text to numerical features using **CountVectorizer (Bag of Words)**.
* Saves fitted vectorizer to `models/vectorizer.pkl`.
* Stores processed features in `data/processed/`.

### **4️⃣ Model Building**

* Trains **Logistic Regression** on the processed dataset.
* Saves trained model to `models/model.pkl`.

### **5️⃣ Model Evaluation**

* Evaluates metrics: Accuracy, Precision, Recall, AUC.
* Logs metrics and parameters to **MLflow**.
* Saves results in `reports/metrics.json` and `reports/experiment_info.json`.

### **6️⃣ Model Registration & Promotion**

* Registers model in **MLflow Model Registry** via `register_model.py`.
* Promotes best-performing model to **Staging** or **Production** using `promote_model.py`.

### **7️⃣ Deployment (Flask + Gunicorn + K8s)**

* Flask app (`flask_app/app.py`) serves predictions.
* Uses MLflow’s **production model** via registry URI.
* Containerized using Docker → deployed on **Kubernetes** with LoadBalancer.

### **8️⃣ Monitoring (Prometheus Integration)**

* Tracks:

  * Total requests (`app_request_count`)
  * Latency (`app_request_latency_seconds`)
  * Prediction count by class (`model_prediction_count`)
* Metrics exposed at `/metrics`.

### **9️⃣ Documentation (Sphinx)**

* Developer documentation stored in `/docs`.
* Build docs locally:

  ```bash
  sphinx-build -b html docs/ build/
  ```

---

## ⚙️ Configuration Files

| File              | Purpose                                    |
| ----------------- | ------------------------------------------ |
| `params.yaml`     | Hyperparameters & test split configuration |
| `dvc.yaml`        | DVC pipeline stage definitions             |
| `Dockerfile`      | Containerization for production            |
| `deployment.yaml` | Kubernetes deployment config               |
| `setup.py`        | Package configuration                      |
| `.flake8`         | Code quality rules                         |
| `tox.ini`         | Environment testing setup                  |
| `Makefile`        | Simplified pipeline commands               |
| `projectflow.txt` | Flow summary for visualization             |

---

##  MLflow + DAGsHub Setup

**Tracking URI:**

```
https://dagshub.com/vikashdas770/YT-Capstone-Project.mlflow
```

**Environment Variable:**

```bash
export CAPSTONE_TEST=<your_dagshub_token>
```

**MLflow Registered Model:**

* `my_model`
* Automatically transitions from **Staging → Production** based on evaluation metrics.

---

##  Deployment Workflow

### Build Docker Image

```bash
docker build -t flask-app:latest .
```

### Run Locally

```bash
docker run -p 5000:5000 flask-app:latest
```

### Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
```

### Access App

```
http://<external-ip>:5000
```

---

## 📈 Prometheus Metrics

| Metric                        | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `app_request_count`           | Number of API requests by method & endpoint |
| `app_request_latency_seconds` | Request latency                             |
| `model_prediction_count`      | Predictions per sentiment class             |

Endpoint:

```
http://<pod-ip>:5000/metrics
```

---

##  Documentation

Sphinx-based project documentation:

```bash
cd docs
make html
```

Open:
`build/html/index.html`

---

##  Key Highlights

✔ Fully modular DVC pipeline
✔ MLflow + DAGsHub tracking
✔ Automated model registry and promotion
✔ Flask + Gunicorn deployment
✔ Kubernetes orchestration
✔ Prometheus monitoring
✔ Auto-generated developer documentation
✔ Production-grade structure with Makefile & CI-ready setup

---

