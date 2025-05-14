import os
import time

from picamera2 import Picamera2

PIC_DIR = "pics"
os.makedirs(PIC_DIR, exist_ok=True)

class Camera:
    def __init__(self):
        self.camera = Picamera2()
        config = self.camera.create_still_configuration()
        self.camera.configure(config)

    def get(self, file_name):
        self.camera.start()
        time.sleep(2)
        self.camera.capture_file(os.path.join(PIC_DIR, file_name))
        self.camera.stop()