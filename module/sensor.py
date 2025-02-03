# Mauro Moureau, 2025

from smbus2 import SMBus
from bme280 import BME280

channel = 1
bus = SMBus(channel)

bme280 = BME280(i2c_dev=bus)


def get_sensor():
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()

    return {"temperature": temperature, "pressure": pressure, "humidity": humidity}
