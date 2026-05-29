# auto_logger.py — Week 2 Integration Lab
# Writes a timestamped JSON entry each time it runs
import datetime
import json
import os

def log_entry():
    now = datetime.datetime.now()
    entry = {
        "timestamp": str(now),
        "message": "Week 2 auto-log: Python + cron working",
        "week": 2,
        "day": "Friday"
    }
    log_path = "/Users/adebolashopeju/auto-log.json"
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"Log entry written at {now}")

log_entry()

