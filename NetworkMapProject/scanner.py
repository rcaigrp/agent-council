import scapy.all as scapy
import json

def scan_ports(ip_range):
    results = []
    for ip in ip_range:
        print(f"Scanning {ip}")
        try:
            response = scapy.sr1(scapy.IP(dst=ip)/scapy.TCP(dport=80), timeout=1)
            if response:
                results.append({
                    "ip": ip,
                    "port": 80,
                    "status": "Open"
                })
            response = scapy.sr1(scapy.IP(dst=ip)/scapy.TCP(dport=443), timeout=1)
            if response:
                results.append({
                    "ip": ip,
                    "port": 443,
                    "status": "Open"
                })
        except Exception as e:
            print(f"Error scanning {ip}: {e}")
    return results

if __name__ == "__main__":
    ip_range = [192, 192, 192, 1]  # Example IP range
    scan_results = scan_ports(ip_range)
    with open("results.json", "w") as f:
        json.dump(scan_results, f, indent=4)
