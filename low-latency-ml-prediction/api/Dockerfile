FROM python:3.8-slim

# Install Flask and MLflow dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app code
COPY app.py /app/app.py

# Expose the API port
EXPOSE 5001

# Run the Flask app
ENTRYPOINT ["python", "/app/app.py"]
