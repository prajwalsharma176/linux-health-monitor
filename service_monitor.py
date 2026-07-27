import psutil

def is_process_running(process_name):
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return False