import psutil
from datetime import datetime
import csv
import os
import time
import subprocess

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ping_status, ping_ms = ping_host("8.8.8.8")
    return [now, cpu, memory, disk, ping_status, ping_ms]

def ping_host(host):
    try:
        # TODO: Replace 'ping' command for cross-platform if needed
        output = subprocess.check_output(["ping", "-c", "1", host], stderr=subprocess.DEVNULL).decode()
        ms = parse_ping_time(output)
        return ("UP", ms)
    except:
        return ("DOWN", -1)

def parse_ping_time(output):
    # TODO: Extract ping time from command output
    # For example: "time=21.3 ms"
    for line in output.splitlines():
        if "time=" in line:
            parts = line.split("time=")
            if len(parts) > 1:
                return float(parts[1].split()[0])
    return -1

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk", "Ping_Status", "Ping_ms"])
        writer.writerow(data)

if __name__ == "__main__":
    for _ in range(5):
        row = get_system_info()
        write_log(row)
        print("Logged:", row)
        time.sleep(10)
