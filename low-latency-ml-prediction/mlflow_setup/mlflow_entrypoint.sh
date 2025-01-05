#!/bin/bash
sudo chmod 755 -R /mlflow_setup/mlruns

# Start MLflow server
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root /mlflow_setup/mlruns \
  --host 0.0.0.0 \
  --port 5000 \
  --file-store /mlflow_setup/mlruns/
