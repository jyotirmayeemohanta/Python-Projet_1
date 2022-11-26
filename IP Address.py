# FIND IP ADDRESS**

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your IP Address is:"+IPAddr)