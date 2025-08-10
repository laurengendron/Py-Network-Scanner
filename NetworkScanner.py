import socket

import threading   #multithreading for speed



def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        pass

#scan multiple ports in parallel on a given IP address to speed up process
def scan_ports_multithread(ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):   #loop through each port num in range and create a new threat that runs scan_port fx
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan:\n")
    start_port = int(input("Enter start port:\n"))
    end_port = int(input("Enter end port:\n"))
    print(f"Scanning {target_ip} from port {start_port} to port {end_port}...")
    scan_ports_multithread(target_ip, start_port, end_port)
    print("Scan complete.")