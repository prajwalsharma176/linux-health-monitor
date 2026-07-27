# Linux Health Monitor

A Python-based Linux Infrastructure Health Monitoring System that automatically monitors system resources, generates health reports, logs system status, and emails reports with attachments.

## Features

- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Network Monitoring
- Process Monitoring
- SSH Service Monitoring
- System Uptime Monitoring
- Health Report Generation
- Logging
- Email Notifications
- Report Attachment
- Cron Automation

## Technologies Used

- Python 3
- Linux (Ubuntu)
- psutil
- python-dotenv
- smtplib
- cron

## Project Structure

```
linux-health-monitor/
│
├── cpu_monitor.py
├── memory_monitor.py
├── disk_monitor.py
├── memory_monitor.py
├── network_monitor.py
├── process_monitor.py
├── service_monitor.py
├── uptime_monitor.py
├── logger.py
├── email_sender.py
├── report.py
├── .env
├── requirements.txt
├── README.md
├── logs/
└── reports/
```

## Installation

```bash
git clone <repository-url>
cd linux-health-monitor

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Run

```bash
python report.py
```

## Automatic Scheduling

The project uses cron to generate and email the report every day automatically.

## Sample Output

- CPU Usage
- Memory Usage
- Disk Usage
- Network Information
- Running Processes
- SSH Status
- Email Report
