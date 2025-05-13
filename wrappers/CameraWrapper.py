import os
import time

from picamera2 import Picamera2

PIC_DIR = "pics"
os.makedirs(PIC_DIR, exist_ok=True)

class Camera:
    def __init__(self):
        self.camera = Picamera2()

    def get(self, file_name):
        try:
            self.camera.start_and_capture_file(os.path.join(PIC_DIR, file_name)) #gebruik gwn de high level ez
        except Exception:
            self.camera.start_and_capture_file(os.path.join(PIC_DIR, f"failsafe_{time.time()}.jpg"))