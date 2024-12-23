import socket

def scan_website(url):
    try:
        ip = socket.gethostbyname(url)
        print(f"[+] The IP address of {url} is: {ip}")
        return ip
    except socket.gaierror:
        print("[-] Could not resolve hostname.")
        return None

def scan_ports(ip, ports=[80, 443, 22, 21, 25, 110, 143, 3389]):
    print(f"[+] Scanning ports on {ip}...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
            else:
                print(f"[-] Port {port} is closed")

if __name__ == "__main__":
    target_url = input("Enter the website URL (e.g., example.com): ")
    target_ip = scan_website(target_url)
    if target_ip:
        scan_ports(target_ip)
