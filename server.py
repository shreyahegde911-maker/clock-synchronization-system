
import socket
import time
import struct
import config

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", config.PORT))

print("Clock Sync Server Running on Port", config.PORT)

while True:
    data, addr = server_socket.recvfrom(1024)

    message = data.decode()

    try:
        T1_str, key = message.split("|")
        T1 = float(T1_str)
    except:
        continue

    if key != config.SECRET_KEY:
        print("Unauthorized request from", addr)
        continue

    T2 = time.time()
    T3 = time.time()

    response = struct.pack("ddd", T1, T2, T3)
    server_socket.sendto(response, addr)

    log = f"{time.ctime()} Request from {addr}\n"

    with open(config.LOG_FILE, "a") as f:
        f.write(log)

    print("Served client:", addr)
