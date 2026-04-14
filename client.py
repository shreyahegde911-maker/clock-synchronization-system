import socket
import time
import struct
import config
import os
import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ADD: timeout so client does not wait forever
client_socket.settimeout(3)

# Client send time
T1 = time.time()

message = f"{T1}|{config.SECRET_KEY}"

client_socket.sendto(message.encode(), (config.SERVER_IP, config.PORT))

try:
    data, address = client_socket.recvfrom(1024)

    # Client receive time
    T4 = time.time()

    T1, T2, T3 = struct.unpack("ddd", data)

    offset = ((T2 - T1) + (T3 - T4)) / 2
    delay = (T4 - T1) - (T3 - T2)

    corrected_time = time.time() + offset

    print("\n---- Clock Synchronization Result ----")
    print("Server Address:", address)
    print("Local Time Before Sync :", time.ctime())
    print("Offset:", offset, "seconds")
    print("Network Delay:", delay, "seconds")
    print("Corrected Time From Server:", time.ctime(corrected_time))

    print("\n---- Configuration ----")
    print("Server IP:", config.SERVER_IP)
    print("Server Port:", config.PORT)
    print("Client Secret Key:", config.SECRET_KEY)

    # Convert corrected time
    dt = datetime.datetime.fromtimestamp(corrected_time)

    date_cmd = dt.strftime("%m-%d-%y")
    time_cmd = dt.strftime("%H:%M:%S")

    # Update system clock
    os.system(f"date {date_cmd}")
    os.system(f"time {time_cmd}")

    print("\nClient system clock updated to server time.")

# ADD: if authentication fails or server doesn't respond
except socket.timeout:
    print("\nAccess denied: Authentication failed or server did not respond.")
    print("Please check SECRET_KEY or server status.")