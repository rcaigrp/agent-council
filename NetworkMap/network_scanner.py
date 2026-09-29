import subprocess

def scan_network(ip_range):
    try:
        result = subprocess.run(['ping', ip_range], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"{ip_range} is reachable.")
            return True
        else:
            print(f"{ip_range} is not reachable.")
            return False
    except subprocess.TimeoutExpired:
        print(f"Timeout scanning {ip_range}")
        return False

if __name__ == '__main__':
    scan_network('192.168.1.1/24')