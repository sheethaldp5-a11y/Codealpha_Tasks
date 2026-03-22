import json
import datetime

def log_json(filename, destination):
    log_entry = {
        "time": str(datetime.datetime.now()),
        "file": filename,
        "destination": destination
    }

    with open("log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")