# Mauro Moureau, 2025

import os
import csv
import time

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

FIELDNAMES = ['timestamp', 'key', 'value']

def create(log_name="flight.csv"):
    log_path = os.path.join(LOG_DIR, log_name)

    if not os.path.exists(log_path):
        with open(log_path, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
    else:
        print(f'Log {log_name} already exists')

    return log_path


def write(log_path, data: dict):
    if not os.path.exists(log_path):
        return print(f'Log {log_path} does not exist')
    
    now = time.time()

    with open(log_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        
        for key, value in data.items():
            writer.writerow([now, key, value])