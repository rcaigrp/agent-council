import subprocess
import ipaddress

def ping(host):
    try:
        subprocess.check_output(['ping', '-c', '1', '-W', '1', host], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_network():
    # Scan common local subnet; adjust as needed
    network = ipaddress.ip_network('192.168.1.0/24', strict=False)
    alive = []
    for ip in network.hosts():
        ip_str = str(ip)
        if ping(ip_str):
            alive.append(ip_str)
    return alive
