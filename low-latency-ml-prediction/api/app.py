from flask import Flask, request, jsonify
import mlflow.pyfunc
import pandas as pd

app = Flask(__name__)

# Load model from MLflow model registry
MODEL_NAME = "IrisClassifier"
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}/Production")

@app.route("/predict", methods=["POST"])
def predict():
    # Parse JSON request and convert to DataFrame
    input_data = request.json
    input_df = pd.DataFrame([input_data])

    # Generate predictions
    predictions = model.predict(input_df)

    # Send back prediction results
    return jsonify({"prediction": predictions[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
