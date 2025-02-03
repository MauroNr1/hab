# Mauro Moureau, 2025

import os
import time # seconden sinds 1 jan, 1970
import csv

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def create(log_name):
    log_path = os.path.join(LOG_DIR, log_name)

    if not os.path.exists(log_path):
        with open(file=log_path, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time", "temperature", "pressure", "humidity", "gas"])
    else:
        print("\nVerwijder bestaand bestand met deze naam.\n")