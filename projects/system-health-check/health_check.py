#!/usr/bin/env python3
"""
System Health Check Script
Collects CPU, memory, disk, and network stats and writes them to a log file.
Optional: send email report (configure SMTP settings).
"""

import psutil
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os

# Configuration
LOG_FILE = "system_health.log"
EMAIL_REPORT = False  # Set True if you want email reports
EMAIL_CONFIG = {
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "username": "user@example.com",
    "password": "password",
    "recipient": "admin@example.com",
}

def collect_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()
    
    report = f"""
--- System Health Report ---
Time: {datetime.now()}
CPU Usage: {cpu}%
Memory Usage: {memory.percent}%
Disk Usage: {disk.percent}%
Network Sent: {net_io.bytes_sent / (1024 * 1024):.2f} MB
Network Received: {net_io.bytes_recv / (1024 * 1024):.2f} MB
"""
    return report

def log_report(report):
    with open(LOG_FILE, 'a') as f:
        f.write(report + '\n')

def send_email(report):
    msg = MIMEText(report)
    msg['Subject'] = 'System Health Report'
    msg['From'] = EMAIL_CONFIG['username']
    msg['To'] = EMAIL_CONFIG['recipient']

    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
        server.starttls()
        server.login(EMAIL_CONFIG['username'], EMAIL_CONFIG['password'])
        server.send_message(msg)

if __name__ == "__main__":
    report = collect_stats()
    log_report(report)
    if EMAIL_REPORT:
        send_email(report)
    print(report)
