import psutil
from datetime import datetime
import csv
import os
import time
import socket

def ping_host(host="8.8.8.8", port=53, timeout=2):
    """用 socket 嘗試連線以判斷網路是否可達，回傳 ('UP'/'DOWN', 毫秒或-1)"""
    try:
        start = time.time()
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))     # 連到 DNS 53 port
        s.close()
        ms = round((time.time() - start) * 1000, 2)
        return "UP", ms
    except Exception:
        return "DOWN", -1

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ping_status, ping_ms = ping_host("8.8.8.8")
    return [now, cpu, memory, disk, ping_status, ping_ms]

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline="") as f:
        w = csv.writer(f)
        if not file_exists:
            w.writerow(["Timestamp", "CPU", "Memory", "Disk", "Ping_Status", "Ping_ms"])
        w.writerow(data)

if __name__ == "__main__":
    for i in range(5):
        row = get_system_info()
        print("Logged:", row)
        write_log(row)
        if i < 4:
            time.sleep(10)
