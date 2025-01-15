import time
import module.log as log

log_file = log.create('flight.csv')

while True:
    log.write(log_file, {
        'temperature': 5,
        'pressure': 1013
    })
    time.sleep(1)