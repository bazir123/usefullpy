import socket
import struct

INPUT_FILE = "input.txt"
OUTPUT_FILE = "expand.txt"

def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]

def int_to_ip(n):
    return socket.inet_ntoa(struct.pack("!I", n))

with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w", buffering=1024*1024) as outfile:
    for line in infile:
        line = line.strip()
        if not line or "/" not in line:
            continue
        ip, prefix = line.split("/")
        prefix = int(prefix)
        
        ip_int = ip_to_int(ip)
        mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
        network = ip_int & mask
        broadcast = network | (~mask & 0xFFFFFFFF)
        chunk = []
        for n in range(network, broadcast + 1):
            chunk.append(int_to_ip(n) + "\n")
