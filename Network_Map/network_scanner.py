# Updated network scanner with improved error handling and logging.
import socket
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_network(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            logging.info(f'Port {port} is open on {ip_address}')
            sock.close()
            return True
        else:
            logging.debug(f'Port {port} is closed on {ip_address}. Error code: {result}')
            sock.close()
            return False
    except socket.error as e:
        logging.error(f'Socket error: {e}')
        return False

# Example usage:
if __name__ == "__main__":
    target_ip = "127.0.0.1"
    ports_to_scan = [21, 22, 80, 443, 8080]  # Example ports

    for port in ports_to_scan:
        if scan_network(target_ip, port):
            print(f"Port {port} is open on {target_ip}")
        else:
            print(f"Port {port} is closed on {target_ip}")
