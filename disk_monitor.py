import psutil

def get_disk():
    return psutil.disk_usage("/")