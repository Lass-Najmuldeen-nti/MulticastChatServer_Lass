import socket
import struct
import sys

message = b'very important data'
multicast_group = ('224.1.1.1', 12345)

# Skapa UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ange time-to-live för meddelandet till 1
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # Skicka data till multicastgruppen
    print(f'sending "{message}" to {multicast_group}')
    sent = sock.sendto(message, multicast_group)

    # Vänta på svar från servern
    print('waiting to receive')
    while True:
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print(f'received "{data}" from {server}')

finally:
    print('closing socket')
    sock.close()
