import bme680

class Sensor:
    def __init__(self):
        try:
            self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except (RuntimeError, IOError):
            self.sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

        self.sensor.set_humidity_oversample(bme680.OS_2X)
        self.sensor.set_pressure_oversample(bme680.OS_8X) #precisie nodig voor hoogte calc
        self.sensor.set_temperature_oversample(bme680.OS_4X)
    
    def get(self):
        if self.sensor.get_sensor_data():
            return self.sensor.data