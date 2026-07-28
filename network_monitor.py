import socket
import psutil

def get_network_info():
    hostname = socket.gethostname()
    interfaces = psutil.net_if_addrs()
    ip_address = "Not Found"

    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if (
                address.family == socket.AF_INET
                and not interface_name.startswith("docker")
                and interface_name != "lo"
                and not interface_name.startswith("tailscale")
            ):
                ip_address = address.address
                break

    network = psutil.net_io_counters()

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "bytes_sent": network.bytes_sent,
        "bytes_recv": network.bytes_recv
    }