import pandas as pd
import yaml
from src.logger import get_logger

logger = get_logger("Data_Preprocessing_Stage")

try:
    # Load parameters from params.yaml
    params = yaml.safe_load(open("params.yaml"))
    
    # Extract file paths for raw and processed data
    raw = params["data"]["raw"]
    processed = params["data"]["processed"]

    # Read raw dataset into a Pandas DataFrame
    df = pd.read_csv(raw)
    logger.info(f"Loaded raw dataset: {raw} with {df.shape[0]} rows")

    # Remove rows containing missing values
    df = df.dropna()

    # Save processed/cleaned data to the specified path
    df.to_csv(processed, index=False)
    logger.info(f"Processed data saved -> {processed}")

except Exception as e:
    # Log any error that occurs and re-raise to stop the pipeline
    logger.error(f"PREPROCESSING FAILED: {e}")
    raise e

