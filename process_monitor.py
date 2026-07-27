import psutil

def get_processes():
    return list(psutil.process_iter(['pid', 'name']))