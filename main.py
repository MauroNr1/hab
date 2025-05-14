# Mauro Moureau, 2025

import time
import threading

import wrappers.LogWrapper as LogWrapper
import wrappers.SensorWrapper as SensorWrapper
import wrappers.CameraWrapper as CameraWrapper

logger = LogWrapper.Logger()
sensor = SensorWrapper.Sensor()
camera = CameraWrapper.Camera()

def log(now):
    sensorResult = sensor.get()

    logger.log([now, sensorResult.temperature, sensorResult.pressure, sensorResult.humidity])

def pic(now):
    camera.get(f"img_{now}.jpg")

next_time = time.time()
next_pic = time.time()

try:
    while True:
        now = time.time()
        if now < next_time:
            time.sleep(next_time - now)
        else:
            next_time = now

        if now >= next_pic:
            threading.Thread(target=pic, args=[next_time], daemon=True).start()
            next_pic += 30

        threading.Thread(target=log, args=[next_time], daemon=True).start()
        next_time += 10
except KeyboardInterrupt:
    pass