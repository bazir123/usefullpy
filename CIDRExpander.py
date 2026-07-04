import socket
import struct

INPUT_FILE = "input.txt"
OUTPUT_FILE = "expand.txt"

def ip_to_int(ip):
    return struct.unpack("!I", socket.inet_aton(ip))[0]
