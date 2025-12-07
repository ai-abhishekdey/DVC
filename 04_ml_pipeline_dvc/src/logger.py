import logging
import os
from datetime import datetime

def get_logger(name: str):
    os.makedirs("logs", exist_ok=True)
    
    # Generate a log file name based on the current date
    
    log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d')}.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # File handler  writes logs to a file
    
    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()
    
    # Define a consistent log message format
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

