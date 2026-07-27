import platform
from datetime import datetime
from logger import write_log
from email_sender import send_email

from cpu_monitor import get_cpu_usage
from memory_monitor import get_memory
from disk_monitor import get_disk
from network_monitor import get_network_info
from process_monitor import get_processes
from service_monitor import is_process_running
from uptime_monitor import get_uptime


def main():
    generated_time = datetime.now()

    print("=" * 50)
    print("Linux Health Monitor")
    print("=" * 50)

    print(f"Hostname      : {platform.node()}")
    print(f"Operating Sys : {platform.system()}")
    print(f"OS Release    : {platform.release()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Generated At  : {generated_time}")

    cpu = get_cpu_usage()
    print(f"CPU Usage     : {cpu}%")

    memory = get_memory()
    print(f"Memory Usage  : {memory.percent}%")
    print(f"Total RAM     : {memory.total / (1024**3):.2f} GB")
    print(f"Available RAM : {memory.available / (1024**3):.2f} GB")

    disk = get_disk()
    print(f"Disk Usage    : {disk.percent}%")
    print(f"Total Disk    : {disk.total / (1024**3):.2f} GB")
    print(f"Free Disk     : {disk.free / (1024**3):.2f} GB")

    days, hours, minutes = get_uptime()
    print(f"Uptime        : {days} days {hours} hours {minutes} minutes")

    network = get_network_info()
    print(f"Network Host  : {network['hostname']}")
    print(f"IP Address    : {network['ip_address']}")
    print(f"Bytes Sent    : {network['bytes_sent'] / (1024**2):.2f} MB")
    print(f"Bytes Recv    : {network['bytes_recv'] / (1024**2):.2f} MB")

    processes = get_processes()
    print(f"Running Processes : {len(processes)}")

    print("\nTop 10 Processes:")
    for process in processes[:10]:
        pid = process.info.get("pid", process.pid)
        name = process.info.get("name", "Unknown")
        print(f"PID: {pid:<6} Name: {name}")

    if is_process_running("sshd"):
        ssh_status = "RUNNING"
        print("SSH Server    : RUNNING")
    else:
        ssh_status = "NOT RUNNING"
        print("SSH Server    : NOT RUNNING")

    print("=" * 50)

    report = f"""
==================================================
Linux Health Monitor
==================================================

Hostname      : {platform.node()}
Operating Sys : {platform.system()}
OS Release    : {platform.release()}
Python Version: {platform.python_version()}
Generated At  : {generated_time}

CPU Usage     : {cpu}%

Memory Usage  : {memory.percent}%
Total RAM     : {memory.total / (1024**3):.2f} GB
Available RAM : {memory.available / (1024**3):.2f} GB

Disk Usage    : {disk.percent}%
Total Disk    : {disk.total / (1024**3):.2f} GB
Free Disk     : {disk.free / (1024**3):.2f} GB

Uptime        : {days} days {hours} hours {minutes} minutes

Network Host  : {network['hostname']}
IP Address    : {network['ip_address']}
Bytes Sent    : {network['bytes_sent'] / (1024**2):.2f} MB
Bytes Recv    : {network['bytes_recv'] / (1024**2):.2f} MB

Running Processes : {len(processes)}

SSH Server    : {ssh_status}

==================================================
Top 10 Processes
==================================================
"""

    for process in processes[:10]:
        pid = process.info.get("pid", process.pid)
        name = process.info.get("name", "Unknown")
        report += f"PID: {pid:<6} Name: {name}\n"

    with open("reports/health_report.txt", "w") as file:
        file.write(report)

    print("\nReport saved successfully!")
    print("Location: reports/health_report.txt")
    write_log("Health report generated successfully.")
    write_log("Health report generated successfully.")
    send_email(report)



if __name__ == "__main__":
    main()