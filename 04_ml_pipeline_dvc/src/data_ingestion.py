import pandas as pd
import yaml
import os
import requests
from src.logger import get_logger

logger = get_logger("Data_Ingestion_Stage")

try:
    # Load key parameters from params.yaml
    params = yaml.safe_load(open("params.yaml"))
    url = params["data"]["url"]        # Remote data source link
    raw = params["data"]["raw"]        # Local file path to save the downloaded dataset

    # Create the raw data directory if it doesn't already exist
    os.makedirs("data/raw", exist_ok=True)

    # Log start of download operation
    logger.info(f"Downloading dataset from {url}")
    
    # Send HTTP request to download the dataset
    r = requests.get(url, timeout=20)

    # If request fails raise an error to stop pipeline
    if r.status_code != 200:
        raise Exception(f"Failed to fetch dataset - HTTP {r.status_code}")

    # Save downloaded content to local file in binary mode
    with open(raw, "wb") as f:
        f.write(r.content)

    # Log success message indicating data was saved
    logger.info(f"Data saved -> {raw}")

except Exception as e:
    # Log error message and re-raise exception so pipeline execution stops
    logger.error(f"DATA INGESTION FAILED: {e}")
    raise e   

