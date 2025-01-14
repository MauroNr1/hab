import os
import time
import json


def create(content):
    os.makedirs("logs", exist_ok=True)

    secs = time.time()
    date = time.gmtime()

    name = f"logs/log_{date.tm_year}-{date.tm_mon}-{date.tm_mday}_{date.tm_hour}-{date.tm_min}-{date.tm_sec}.json"

    with open(name, "w") as f:
        f.write(json.dumps({"time": secs, "content": content}))
