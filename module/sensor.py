# Mauro Moureau, 2025

from smbus2 import SMBus
from bme280 import BME280

channel = 1
bus = SMBus(channel)

bme280 = BME280(i2c_dev=bus)

bme280.get_temperature()