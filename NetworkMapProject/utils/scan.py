import ipaddress
from ping3 import ping

def scan_subnet(subnet: str):
    """Scan the given subnet (e.g., '192.168.1.0/24') and return a list of alive hosts.
    Each host is represented as a dict with 'ip' and 'latency' (ms).
    """
    net = ipaddress.ip_network(subnet, strict=False)
    alive = []
    for ip in net.hosts():
        try:
            latency = ping(str(ip), timeout=0.5, unit='ms')
            if latency is not None:
                alive.append({"ip": str(ip), "latency": round(latency, 2)})
        except Exception:
            # ignore unreachable or permission errors
            continue
    return alive
