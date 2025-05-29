from loguru import logger
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Remove the default logger to avoid double output
logger.remove()

# Add a file sink with desired format
logger.add(
    LOG_FILE,
    format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
    level="INFO",
    rotation="00:00",  # Optional: rotate daily
    retention="7 days"  # Optional: keep logs for 7 days
)

# Optional: mimic `get_logger(name)` if needed
def get_logger(name=None):
    if name:
        return logger.bind(logger_name=name)
    return logger
