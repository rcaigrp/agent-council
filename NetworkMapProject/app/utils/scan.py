import ipaddress
from ping3 import ping

def _is_alive(ip: str) -> bool:
    try:
        # Use non‑privileged mode to avoid raw socket requirement inside container
        return ping(ip, timeout=1, privileged=False) is not None
    except Exception:
        return False

def scan_subnet(subnet: str) -> list:
    """Return a list of IP strings that responded to ping within the given subnet.
    subnet: CIDR notation, e.g., '192.168.1.0/24'
    """
    net = ipaddress.ip_network(subnet, strict=False)
    alive = []
    for ip in net.hosts():
        ip_str = str(ip)
        if _is_alive(ip_str):
            alive.append(ip_str)
    return alive
