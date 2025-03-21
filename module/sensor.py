# Mauro Moureau, 2025

import bme680

try:
    sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except (RuntimeError, IOError):
    sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

def get():
    return sensor.get_sensor_data() and {
        "success": True,
        "temperature": sensor.data.temperature,
        "pressure": sensor.data.pressure,
        "humidity": sensor.data.humidity
    } or {"success": False}
