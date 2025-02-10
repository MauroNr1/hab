# Mauro Moureau, 2025

import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

def get():
    if sensor.get_sensor_data():
        return {"temperature": sensor.data.temperature}

    return None
