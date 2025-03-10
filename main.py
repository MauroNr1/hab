# Mauro Moureau, 2025

import time
import module.log as log
import module.sensor as sensor
import module.camera as camera

logger = log.Logger(headers=["timestamp", "message"])

try:
    while True:
        date = time.time()

        result = sensor.get()
        print(f"Temp: {result.temperature}, Hum: {result.humidity}, Pres: {result.pressure}")

        time.sleep(1)
except KeyboardInterrupt:
    print("Ended logging.")