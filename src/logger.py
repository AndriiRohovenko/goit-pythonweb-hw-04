import logging
from pathlib import Path
from datetime import datetime
import sys

Path("logs").mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"logs/run_{timestamp}.log"

file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
stream_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[file_handler, stream_handler],
)

logger = logging.getLogger(__name__)
