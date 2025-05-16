import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_path = os.path.join(log_dir, "test.log")

logging.basicConfig(
    filename=log_path,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger()
