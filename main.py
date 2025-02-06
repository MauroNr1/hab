# Mauro Moureau, 2025

import time
import module.log as log
#import module.sensor as sensor
import module.camera as camera

logger = log.Logger(headers=["timestamp", "message"])

try:
    while True:
        date = time.time()

        print("Hi!")

        time.sleep(10)
except KeyboardInterrupt:
    print("Ended logging.")