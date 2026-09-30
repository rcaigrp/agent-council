# Logging Configuration
import logging
import os

LOG_LEVEL = logging.INFO
LOG_FILE = 'scan.log'

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE) if os.path.dirname(LOG_FILE) else '.', exist_ok=True)

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
