# Mauro Moureau, 2025

import time
import threading

import wrappers.LogWrapper as LogWrapper
import wrappers.SensorWrapper as SensorWrapper
import wrappers.CameraWrapper as CameraWrapper

logger = LogWrapper.Logger()
sensor = SensorWrapper.Sensor()
camera = CameraWrapper.Camera()

def log():
    now = time.time()

    threading.Timer(interval=10, function=log).start()

    sensorResult = sensor.get()
    logger.log([now, sensorResult.temperature, sensorResult.pressure, sensorResult.humidity])

def pic():
    now = time.time()
    
    threading.Timer(interval=30, function=pic).start()
    
    camera.get(f"img_{now}.jpg")

try:
    log()
    pic()
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    pass