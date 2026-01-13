#!/usr/bin/env python3
"""
Sysadmin Toolkit CLI
Menu-driven tool combining health check, backup, and network diagnostics
"""

import subprocess
import sys
from pathlib import Path

def health_check():
    subprocess.run(["python3", "../system-health-check/health_check.py"])

def backup():
    subprocess.run(["bash", "../backup-system/backup.sh"])

def network_diag():
    subprocess.run(["python3", "../network-tools/net_diag.py"])

MENU = {
    "1": ("System Health Check", health_check),
    "2": ("Backup System", backup),
    "3": ("Network Diagnostics", network_diag),
    "0": ("Exit", sys.exit)
}

def main():
    while True:
        print("\nSysadmin Toolkit Menu")
        for key, (name, _) in MENU.items():
            print(f"{key}. {name}")
        choice = input("Choose an option: ").strip()
        if choice in MENU:
            MENU[choice][1]()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
