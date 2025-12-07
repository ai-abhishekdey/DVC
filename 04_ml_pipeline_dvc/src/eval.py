import pandas as pd
from sklearn.metrics import accuracy_score
import mlflow
from src.logger import get_logger

# Initialize logger for the evaluation stage
logger = get_logger("Evaluation_Stage")

try:
    # Load predictions generated during the training stage
    df = pd.read_csv("metrics/preds.csv")

    # Compute accuracy using true vs predicted labels
    acc = accuracy_score(df["y_true"], df["y_pred"])

    # Save the evaluation metric to a text file
    with open("metrics/score.txt", "w") as f:
        f.write(f"accuracy: {acc}")

    # Track evaluation results using MLflow
    mlflow.set_experiment("iris_dvc_experiments")
    # nested=True allows logging this run under the parent training run
    with mlflow.start_run(nested=True):
        mlflow.log_metric("accuracy", acc)

    # Log the success message
    logger.info(f"Evaluation completed : accuracy = {acc}")

except Exception as e:
    # Log any errors and stop pipeline execution
    logger.error(f"EVALUATION FAILED: {e}")
    raise e

