
---

# End-to-End MLOps Pipeline – Sentiment Analysis Project

**Production-Ready Deployment on AWS EKS with Monitoring & Alerting**

This project demonstrates a **complete MLOps lifecycle** — from data ingestion to model deployment and monitoring — built around a **Sentiment Analysis model**.
It integrates **DVC**, **MLflow**, **Docker**, **AWS ECR/EKS**, **Prometheus**, **Grafana**, and **GitHub Actions**, creating a real-world **CI/CD-enabled MLOps system**.

---

## Project Overview

This pipeline automates:

* **Data → Model → Deployment → Monitoring**
* Continuous integration (CI) with **GitHub Actions**
* Continuous delivery (CD) to **AWS EKS**
* Real-time monitoring via **Prometheus & Grafana**

###  Key Goals

 Reproducible ML workflow using **DVC & MLflow**
 Model versioning and automatic promotion via **MLflow Registry**
 Seamless containerization and deployment on **AWS EKS**
 Scalable model monitoring with **Prometheus + Grafana Alerts**

---

##  Tech Stack

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

##  Architecture Overview

```text
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

##  CI/CD Pipeline (GitHub Actions)

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

 **Result:**
On every Git push, your app gets retrained, tested, re-deployed, and monitored automatically.

---

##  Containerization

**Dockerfile Summary:**

* Uses `python:3.11-slim`
* Installs dependencies + NLTK data
* Runs Flask API via **Gunicorn** for production

```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
```

---

##  Deployment on AWS EKS

**Deployment Highlights:**

* 2 replicas for high availability
* Resource limits ensure efficient scaling
* Secure ECR pull via `imagePullSecrets`
* Secrets managed with Kubernetes Secret
* LoadBalancer exposes API externally on port `5000`

```bash
kubectl apply -f deployment.yaml
kubectl get svc
```

---

##  Monitoring & Alerting (Prometheus + Grafana)

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

## 🖼️ Screenshots

Below are snapshots demonstrating the full MLOps pipeline deployment, monitoring, and observability across AWS and open-source tools.

---

### 🔹 MLOps Project Architecture
Overall workflow showing data flow, CI/CD, model registry, deployment, and monitoring.  
<div align="center">
  <img src="https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/MLOps_Architecture.png" 
       alt="MLOps Architecture" width="750"/>
  <br/>
  <em>End-to-end MLOps architecture showing data flow from ingestion to monitoring.</em>
</div>

---

### 🔹 ECR Image Repository
Docker images stored securely in AWS ECR.  
<div align="center">
  <img src="https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/ecr.png" 
       alt="ECR Screenshot" width="600"/>
  <br/>
  <em>✅ Container image successfully pushed to Amazon Elastic Container Registry (ECR).</em>
</div>

---

### 🔹 EKS Deployment (kubectl output)
Application successfully deployed on AWS EKS via LoadBalancer.  
<div align="center">
  <img src="https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/eks.png" 
       alt="EKS Deployment" width="600"/>
  <br/>
  <em>🚀 Flask app deployed on AWS EKS cluster using LoadBalancer service.</em>
</div>

---

### 🔹 Prometheus Metrics
Live metrics being scraped from `/metrics` endpoint — tracking API latency, request count, and predictions.  
<div align="center">
  <img src="https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/prometheus.png" 
       alt="Prometheus Screenshot" width="600"/>
  <br/>
  <em>📈 Prometheus scraping real-time metrics from Flask app endpoint.</em>
</div>

---

### 🔹 Grafana Dashboard
Real-time visualization of API requests and model performance metrics integrated with Prometheus.  
<div align="center">
  <img src="https://raw.githubusercontent.com/Gaurav9693089415/MLOps-end-to-end-Project/main/screenshots/grafana.png" 
       alt="Grafana Dashboard" width="600"/>
  <br/>
  <em>📊 Grafana dashboard showing live API and model monitoring charts.</em>
</div>

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
