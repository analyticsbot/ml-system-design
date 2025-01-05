FROM bitnami/spark:latest

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Set working directory
WORKDIR /app

# Copy the application files
COPY main.py config.py /app/

# Entrypoint
ENTRYPOINT ["spark-submit", "/app/main.py"]
