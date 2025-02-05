# Mauro Moureau, 2025

import os
import time
import csv

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

class Logger:
    def __init__(self, log_name):
        log_path = os.path.join(LOG_DIR, log_name)

        if not os.path.exists(log_path):
            with open(file=log_path, mode="w", newline="") as f:
                writer = csv.writer(f)
        else:
            raise FileExistsError