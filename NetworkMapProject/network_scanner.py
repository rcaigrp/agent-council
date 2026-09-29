from scapy.all import *
import sys

def ping_sweep(network_range):
    """Perform a ping sweep on the given network range."""
    hosts_up = []
    try:
        # Use the correct way to iterate over IP addresses
        for ip in IPNetwork(network_range):
            pkt = IP(dst=str(ip))/ICMP()
            resp = sr1(pkt, timeout=1, verbose=0)
            if resp is not None:
                hosts_up.append(str(ip))
    except Exception as e:
        print(f'Error during ping sweep: {e}')
    return hosts_up

def port_scan(host, ports):
    """Scan specific ports on a given host."""
    open_ports = []
    try:
        for port in ports:
            pkt = IP(dst=host)/TCP(dport=port, flags="S")
            resp = sr1(pkt, timeout=1, verbose=0)
            if resp is not None and resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:
                open_ports.append(port)
    except Exception as e:
        print(f'Error during port scan: {e}')
    return open_ports
