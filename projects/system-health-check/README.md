# System Health Check Script

This Python script collects CPU, memory, disk, and network stats on a Linux/Windows server, logs them, and optionally emails a report.  

## Features
- CPU, memory, disk, and network usage logging
- Logs stored in `system_health.log`
- Optional email report via SMTP
- Cross-platform (Linux/Windows)

## Installation

```bash
git clone https://github.com/n3m05/sysadmin-portfolio.git
cd sysadmin-portfolio/projects/system-health-check
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt

## Usage
python health_check.py

Enable email reports by setting EMAIL_REPORT = True in health_check.py
 and configuring EMAIL_CONFIG

## Example Output

--- System Health Report ---
Time: 2025-12-28 20:30:00
CPU Usage: 12%
Memory Usage: 45%
Disk Usage: 67%
Network Sent: 12.34 MB
Network Received: 56.78 MB

