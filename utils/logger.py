import logging
import os


os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("AutomationFramework")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler = logging.FileHandler(
    "logs/automation.log"
)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)