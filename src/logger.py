import logging
import os
from datetime import datetime

# Creating a logs directory if it doesn't exist
LOGS_DIR = 'logs'
os.makedirs(LOGS_DIR, exist_ok=True)


LOG_FILE= os.path.join(LOGS_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configuring the logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO, # Set to INFO level to capture warnings and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_logger(name):
    """
    Returns a logger with the specified name.
    """
    return logging.getLogger(name)

get_logger(__name__).info(f"{__name__}  -- > Logger initialized")