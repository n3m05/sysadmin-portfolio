#!/usr/bin/env python3
"""
Network Diagnostics Toolkit
Ping hosts, check open ports, traceroute, and summarize results.
"""

import subprocess
import socket

HOSTS = ["8.8.8.8", "github.com"]
PORTS = [22, 80, 443]

def ping(host):
    result = subprocess.run(["ping", "-c", "2", host], capture_output=True)
    return result.returncode == 0

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        return s.connect_ex((host, port)) == 0

if __name__ == "__main__":
    for host in HOSTS:
        print(f"Pinging {host}...", "Reachable" if ping(host) else "Unreachable")
        for port in PORTS:
            print(f" Port {port}: {'Open' if check_port(host, port) else 'Closed'}")
