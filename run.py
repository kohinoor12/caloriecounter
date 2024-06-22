import socket
import subprocess
import os

# x = socket.gethostbyaddr(socket.gethostname())

# x = socket.gethostbyname(socket.gethostname())
# x = str(x)
# print(x)
x = '127.0.0.1:5000'
os.system(f'manage.py runserver {x}')