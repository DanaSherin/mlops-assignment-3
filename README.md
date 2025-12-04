# MLOps Demo — Spark + MLflow (lightweight, cloud-friendly)

## Goal
Start a minimal Apache Spark cluster (1 master + 3 workers) and an MLflow server using Docker Compose, run a tiny ML pipeline that logs an experiment to MLflow, and capture the required assignment screenshots:

1. Spark Master UI (http://localhost:8080) showing 3 workers connected.
2. MLflow UI (http://localhost:5000) showing 1 experiment run with parameters, metrics, and artifact link.

This repo is designed to run inside GitHub Codespaces or Gitpod, so you don't need to install anything on your laptop.

---

## Repo structure

    .
    ├── docker-compose.yml
    ├── mlflow/
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   └── train.py
    ├── run-demo.sh
    └── diagrams/
        └── architecture-ascii.txt

---

## Quick start (GitHub Codespaces / Gitpod)

### 1. Open the repo in a Codespace
- On GitHub click: Code → Codespaces → Create codespace on main

### 2. Make the demo script executable

    chmod +x run-demo.sh

### 3. Run the demo

    ./run-demo.sh

This will:
- Build the MLflow container
- Start Spark Master + 3 Worker containers
- Start MLflow server
- Run the training script inside the MLflow container
- Log a run with parameters, metrics, and model artifact

### 4. Open the interfaces (forward ports in Codespaces)
- Spark UI → http://localhost:8080
- MLflow UI → http://localhost:5000

---

## Required Screenshots (Submit These)

### 1. Spark Master UI (http://localhost:8080)
Must show:
- Spark Master
- 3 connected workers
- Worker IDs, cores, and memory

### 2. MLflow UI (http://localhost:5000)
Must show:
- Default experiment
- One run
- Parameters
- Metrics
- Model artifact

---

## If Codespaces/Gitpod cannot run Docker
Use a small Ubuntu VM:

    sudo apt update
    sudo apt install -y docker.io docker-compose
    sudo usermod -aG docker $USER
    chmod +x run-demo.sh
    ./run-demo.sh

---

## What each file does

- docker-compose.yml — Runs Spark Master, 3 Workers, and MLflow server.
- mlflow/Dockerfile — Lightweight image that runs the MLflow server.
- mlflow/requirements.txt — Dependencies for MLflow + scikit-learn.
- mlflow/train.py — Simple LogisticRegression model logged to MLflow.
- run-demo.sh — Builds containers, starts environment, runs training.
- diagrams/architecture-ascii.txt — ASCII diagram of the platform.

---

## Manageability & scalability

### Manageability:
- All services run in isolated containers.
- MLflow centralizes experiment tracking.
- Docker Compose simplifies deployment.

### Scalability:
- Spark demonstrates horizontal scaling with 3 workers.
- Production recommendations:
  - Kubernetes orchestration
  - Postgres MLflow backend
  - S3/MinIO artifact storage
  - Autoscaling Spark workers

---

## Troubleshooting

If something is not running:

    docker-compose ps
    docker-compose logs spark-master
    docker-compose logs mlflow

If UIs do not load, re-forward ports in Codespaces.
