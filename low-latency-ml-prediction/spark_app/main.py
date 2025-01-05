from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
import mlflow.pyfunc
from config import MODEL_NAME, DELTA_LOCATION, CHECKPOINT_LOCATION

# Initialize Spark session
spark = SparkSession.builder.appName("MLFlow_Spark_Streaming").getOrCreate()

# Define the data schema
schema = StructType().add("fixed acidity", StringType()).add("volatile acidity", StringType())  # Complete schema as needed

# Set up MLflow model URI and load model as Spark UDF
model_uri = f"models:/{MODEL_NAME}/Production"
loaded_model = mlflow.pyfunc.spark_udf(spark, model_uri=model_uri, result_type="double")

# Streaming DataFrame
streaming_df = (spark.readStream
    .option("sep", ",")
    .option("header", "true")
    .option("enforceSchema", "true")
    .schema(schema)
    .csv("/app/data/input")  # Directory for input streaming data
)

# Make predictions
prediction_df = streaming_df.withColumn("predictions", loaded_model(struct(*map(col, streaming_df.columns))))

# Write to Delta table
query = (prediction_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", CHECKPOINT_LOCATION)
    .option("path", DELTA_LOCATION)
    .trigger(processingTime="5 minutes")
    .start()
)

query.awaitTermination()
