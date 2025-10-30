# End-to-End MLOps Pipeline – Sentiment Analysis Project

*Production-Ready Deployment on AWS EKS with Monitoring & Alerting*

This project demonstrates a **complete MLOps lifecycle** — from data ingestion to model deployment and monitoring — built around a **Sentiment Analysis model**.
It integrates **DVC**, **MLflow**, **Docker**, **AWS ECR/EKS**, **Prometheus**, **Grafana**, and **GitHub Actions**, creating a real-world **CI/CD-enabled MLOps system**.

---

## 📋 Project Overview

This pipeline automates:

* **Data → Model → Deployment → Monitoring**
* Continuous integration (CI) with **GitHub Actions**
* Continuous delivery (CD) to **AWS EKS**
* Real-time monitoring via **Prometheus & Grafana**

### 🎯 Key Goals

✅ Reproducible ML workflow using **DVC & MLflow**  
✅ Model versioning and automatic promotion via **MLflow Registry**  
✅ Seamless containerization and deployment on **AWS EKS**  
✅ Scalable model monitoring with **Prometheus + Grafana Alerts**

---

## 🛠 Tech Stack

| Category                  | Tools / Frameworks                     |
| ------------------------- | -------------------------------------- |
| **Language**              | Python 3.11                            |
| **Modeling**              | Scikit-learn, NLTK                     |
| **Experiment Tracking**   | MLflow + DagsHub                       |
| **Data Versioning**       | DVC                                    |
| **Deployment**            | Flask, Gunicorn, Docker, AWS ECR + EKS |
| **CI/CD**                 | GitHub Actions                         |
| **Monitoring & Alerting** | Prometheus, Grafana                    |
| **Cloud Infra**           | AWS (ECR, EKS, IAM, CloudFormation)    |

---

## 🏗 Architecture Overview

```
        ┌──────────────────────┐
        │      Developer       │
        │   (Push to GitHub)   │
        └──────────┬───────────┘
                   │
                   ▼
         ┌───────────────────┐
         │ GitHub Actions CI │───► Runs DVC + MLflow + Tests
         └──────────┬────────┘
                    ▼
         ┌───────────────────┐
         │ Docker Build +    │
         │ Push to AWS ECR   │
         └──────────┬────────┘
                    ▼
         ┌───────────────────┐
         │ Deploy on EKS     │
         │ via kubectl apply │
         └──────────┬────────┘
                    ▼
         ┌───────────────────┐
         │ Prometheus &      │
         │ Grafana Monitor   │
         └───────────────────┘
```

---

## 🖼 Screenshots

### 🔹 MLOps Project Architecture
Overall workflow showing data flow, CI/CD, model registry, deployment, and monitoring.

![MLOps Architecture](https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/MLOps_Architecture.png)

*End-to-end MLOps architecture showing data flow from ingestion to monitoring.*

---

### 🔹 ECR Image Repository
Docker images stored securely in AWS ECR.

![ECR Screenshot](https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/ecr.png)

*✅ Container image successfully pushed to Amazon Elastic Container Registry (ECR).*

---

### 🔹 EKS Deployment
Application successfully deployed on AWS EKS via LoadBalancer.

![EKS Deployment](https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/eks.png)

*🚀 Flask app deployed on AWS EKS cluster using LoadBalancer service.*

---

### 🔹 Prometheus Metrics
Live metrics being scraped from `/metrics` endpoint — tracking API latency, request count, and predictions.

![Prometheus Screenshot](https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/prometheus.png)

*📈 Prometheus scraping real-time metrics from Flask app endpoint.*

---

### 🔹 Grafana Dashboard
Real-time visualization of API requests and model performance metrics integrated with Prometheus.

![Grafana Dashboard](https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/grafana.png)

*📊 Grafana dashboard showing live API and model monitoring charts.*

---

## 🔄 CI/CD Pipeline (GitHub Actions)

Automated workflow from training to deployment:

1. **Run DVC pipeline & unit tests**
2. **Promote best model to MLflow Production**
3. **Build & push Docker image to AWS ECR**
4. **Update EKS cluster via kubectl**

```yaml
on: push
jobs:
  project-testing:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install & Test
        run: |
          pip install -r requirements.txt
          dvc repro
          python -m unittest tests/test_model.py
      - name: Build & Push Docker
        run: |
          docker build -t capstone-proj .
          docker push <ECR_REPO_URL>
      - name: Deploy on EKS
        run: kubectl apply -f deployment.yaml
```

**Result:** On every Git push, your app gets retrained, tested, re-deployed, and monitored automatically.

---

## 🐳 Containerization

**Dockerfile Summary:**

* Uses `python:3.11-slim`
* Installs dependencies + NLTK data
* Runs Flask API via **Gunicorn** for production

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
```

---

## ☁️ Deployment on AWS EKS

**Deployment Highlights:**

* 2 replicas for high availability
* Resource limits ensure efficient scaling
* Secure ECR pull via imagePullSecrets
* Secrets managed with Kubernetes Secret
* LoadBalancer exposes API externally on port 5000

```bash
kubectl apply -f deployment.yaml
kubectl get svc
```

---

## 📊 Monitoring & Alerting (Prometheus + Grafana)

**Custom Metrics exposed via Flask app:**

| Metric                        | Description                     |
| ----------------------------- | ------------------------------- |
| `app_request_count`           | Number of API requests          |
| `app_request_latency_seconds` | Request latency per endpoint    |
| `model_prediction_count`      | Predictions per sentiment class |

**Prometheus Scrapes Endpoint:**

```
http://<pod-ip>:5000/metrics
```

**Grafana Dashboards:**
Visualize metrics like request load, latency, and model prediction frequency.

---

## 🔑 Key Highlights

✔ Fully modular DVC pipeline  
✔ MLflow + DAGsHub tracking  
✔ Automated model registry and promotion  
✔ Flask + Gunicorn deployment  
✔ Kubernetes orchestration  
✔ Prometheus + Grafana monitoring  
✔ Auto-generated developer documentation  
✔ Production-grade structure with Makefile & CI-ready setup

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker
- AWS CLI configured
- kubectl installed
- Access to AWS ECR and EKS

### Local Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd MLOps-end-to-end-Project

# Install dependencies
pip install -r requirements.txt

# Run DVC pipeline
dvc repro

# Start Flask app locally
python app.py
```

### Deploy to AWS EKS

```bash
# Build and push Docker image
docker build -t <your-ecr-repo> .
docker push <your-ecr-repo>

# Deploy to EKS
kubectl apply -f deployment.yaml

# Check deployment status
kubectl get pods
kubectl get svc
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📧 Contact

For questions or feedback, please reach out via GitHub issues.
