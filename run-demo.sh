#!/usr/bin/env bash
set -e

# Build images and start containers
docker-compose up -d --build

# Wait a few seconds for services to initialize
sleep 8

# Run training script inside mlflow container to create a logged run
docker-compose exec -T mlflow python /app/train.py

echo "Demo run complete."

echo "Spark UI: http://localhost:8080"
echo "MLflow UI: http://localhost:5000"
