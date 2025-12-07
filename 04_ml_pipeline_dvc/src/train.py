import os
import pandas as pd
import yaml
import pickle
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from src.logger import get_logger

# Initialize logger for the model training stage
logger = get_logger("Model_Training_Stage")

try:
    # Load model/training configuration values from params.yaml
    params = yaml.safe_load(open("params.yaml"))
    features = params["data"]["features"]      # Path to the engineered features dataset
    target = params["model"]["target"]         # Name of the label column

    # Load the features dataset from disk
    df = pd.read_csv(features)
    X = df.drop(columns=[target])   # Training inputs
    y = df[target]                  # Training labels

    # Log dataset split step
    logger.info("Splitting dataset")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=params["model"]["test_size"],          # Percentage of test data
        random_state=params["model"]["random_state"],    # Ensures reproducible splits
    )

    # Define MLflow experiment name
    mlflow.set_experiment("iris_dvc_experiments")

    # Record this training run in MLflow
    with mlflow.start_run():
        logger.info("Training model...")

        # Create and train the RandomForest model using hyperparameters from params.yaml
        model = RandomForestClassifier(
            n_estimators=params["model"]["n_estimators"],
            random_state=params["model"]["random_state"]
        )
        model.fit(X_train, y_train)

        # Predict on the test set and save predictions
        os.makedirs("metrics", exist_ok=True)
        preds = model.predict(X_test)
        pd.DataFrame({"y_true": y_test, "y_pred": preds}).to_csv("metrics/preds.csv", index=False)

        # Save the trained model as a .pkl file
        os.makedirs("models", exist_ok=True)
        pickle.dump(model, open("models/model.pkl", "wb"))

        # Log hyperparameters and the trained model artifact to MLflow
        mlflow.log_params(params["model"])
        mlflow.sklearn.log_model(model, "rf_model")

        logger.info("Model training completed")  # Final log once successful

except Exception as e:
    # Log any exception and re-raise to stop the pipeline
    logger.error(f"TRAINING FAILED: {e}")
    raise e

