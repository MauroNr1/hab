# Mauro Moureau, 2025

import os
import time
import json


def generate_path_name(date: time.struct_time):
    return f"logs/log_{date.tm_year}-{date.tm_mon}-{date.tm_mday}_{date.tm_hour}-{date.tm_min}-{date.tm_sec}.json"


def create(content="Empty log"):
    os.makedirs("logs", exist_ok=True)

    secs = time.time()
    date = time.gmtime(secs)

    name = generate_path_name(date)

    with open(name, "w") as f:
        f.write(json.dumps({"time": secs, "content": content}))
