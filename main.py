import time
import module.log as log


try:
    while True:

        time.sleep(10)
except KeyboardInterrupt:
    print("Logging stopped.")