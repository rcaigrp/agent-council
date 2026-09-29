import scapy.all as scapy
import json

def scan_network(ip_prefix): 
    arp_packets = scapy.ARP(pdst=ip_prefix + '/*', broadcast=True) 
    answered_list = scapy.srp(arp_packets, timeout=1)
    result = []
    for i in answered_list[1]:
        result.append({'ip': i[1].psrc, 'mac': i[1].hwsrc})
    return result


with open('results.json', 'w') as f:
    json.dump({'scanned_hosts': scan_network('192.168.1.')}, f, indent=4)