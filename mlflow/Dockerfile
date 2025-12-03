FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

COPY train.py /app/train.py

EXPOSE 5000

CMD ["bash", "-lc", "mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root /mlflow/artifacts --host 0.0.0.0 --port 5000 & tail -f /dev/null"]
