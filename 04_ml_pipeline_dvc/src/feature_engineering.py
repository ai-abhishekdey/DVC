import os
import pandas as pd
import yaml
from src.logger import get_logger

logger = get_logger("Feature_Engineering_Stage")

try:
    # Load configuration values from params.yaml
    params = yaml.safe_load(open("params.yaml"))

    # Retrieve file paths for processed data and engineered feature data
    processed = params["data"]["processed"]
    features = params["data"]["features"]

    # Retrieve the target column name for the model
    target = params["model"]["target"]

    # Load the cleaned/processed dataset
    df = pd.read_csv(processed)
    logger.info(f"Loaded processed dataset: {processed}")

    # Ensure that the target column exists; if missing, stop pipeline
    if target not in df.columns:
        raise Exception(f"Target column '{target}' not found in dataset")

    # Separate input features (X) by removing target column
    X = df.drop(columns=[target])

    # Add the target column back for simplicity, preserving both features + labels
    X[target] = df[target]

    # Save engineered feature dataset to the specified path
    os.makedirs("data/features", exist_ok=True)
    X.to_csv(features, index=False)
    logger.info(f"Feature dataset saved -> {features}")

except Exception as e:
    # Log error message and re-raise to stop subsequent pipeline stages
    logger.error(f"FEATURE GENERATION FAILED: {e}")
    raise e

