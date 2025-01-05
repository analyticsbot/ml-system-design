FROM python:3.8-slim

# Install MLflow and dependencies
RUN pip install mlflow boto3

# Expose MLflow port
EXPOSE 5000

# Copy entrypoint script
COPY mlflow_entrypoint.sh /mlflow_entrypoint.sh
RUN chmod +x /mlflow_entrypoint.sh
RUN echo /mlflow_setup/mlruns/ > test.txt
# Set entrypoint for MLflow
# ENTRYPOINT ["/mlflow_entrypoint.sh"]

CMD mlflow server \
    --backend-store-uri /mlflow_setup/mlruns/tracking \
    --default-artifact-root /mlflow_setup/mlruns/artifacts \
    --host 0.0.0.0 \
    --port 5000
