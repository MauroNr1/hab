import os
import csv

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def generatePath(iter):
    return os.path.join(LOG_DIR, f"log_{iter}.csv")

class Logger:
    def __init__(self):
        _i = 1

        try:
            while True:
                if _i > 100: # meer als 100 logs dus moet opgekuist worden
                    raise Exception("TooManyAttempts")

                self.path = generatePath(_i)

                if not os.path.exists(self.path):
                    self.file = open(file=self.path, mode="a", newline="", encoding="utf-8")
                    break

                _i += 1
        except Exception as e:
            self.path = generatePath("exception")
            self.file = open(file=self.path, mode="a", newline="", encoding="utf-8")
        
        self.writer = csv.writer(self.file)
        self.writer.writerow(["time", "temperature", "pressure", "humidity"])
    def log(self, row: iter):
        self.writer.writerow(row)
        self.file.flush()