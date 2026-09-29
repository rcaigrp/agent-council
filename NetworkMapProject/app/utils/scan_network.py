import ipaddress

def is_host_up(ip):
    try:
        # Lazy import to allow test monkeypatching of ping3.ping
        from ping3 import ping
        return ping(str(ip), timeout=1) is not None
    except Exception:
        return False

def scan_subnet(cidr):
    """Return list of reachable IPs in the given CIDR subnet."""
    network = ipaddress.ip_network(cidr, strict=False)
    reachable = []
    for ip in network.hosts():
        if is_host_up(ip):
            reachable.append(str(ip))
    return reachable
