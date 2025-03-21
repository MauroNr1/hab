# Mauro Moureau, 2025

import time
import module.log as log
#import module.sensor as sensor
import module.camera as camera

logger = log.Logger(headers=["temperature", "humidity", "pressure", "camera"])

try:
    while True:
        logger.log(["hi"])
except KeyboardInterrupt:
    print("Ended logging.")