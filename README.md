
Distributed Clock Synchronization System using UDP

This project synchronizes client clocks with a master server.

Project Structure
-----------------
server/  -> Runs the master clock server
client/  -> Runs synchronization client
logs/    -> Stores synchronization logs

Setup
-----
1. Find the server IP address (run 'ipconfig' or 'ifconfig').
2. Edit client/config.py and replace:

SERVER_IP = "CHANGE_TO_SERVER_IP"

with the server computer IP.

Run Server
----------
cd server
python server.py

Run Client
----------
cd client
python client.py

Output
------
Client will display:
- Server address
- Offset between clocks
- Network delay
- Corrected synchronized time

Logs
----
Server automatically logs client requests in logs/sync_log.txt
