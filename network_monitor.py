import socket
import psutil

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    network = psutil.net_io_counters()

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "bytes_sent": network.bytes_sent,
        "bytes_recv": network.bytes_recv
    }