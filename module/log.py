# Mauro Moureau, 2025

import os
import time
import csv

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

class Logger:
    def __init__(self, log_name="flight.csv", headers=[]):
        self.path = os.path.join(LOG_DIR, log_name)
        self.headers = headers

        if not os.path.exists(self.path):
            with open(file=self.path, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.headers)

    def log(self, row):
        with open(file=self.path, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)