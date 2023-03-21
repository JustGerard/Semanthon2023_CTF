import socket


# Define socket host and port
FLAG = 'flag{8Ut_1_L0V3_1T}'
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    response = 'HTTP/1.0 200 OK\n\n'
    method = request.split(' ')[0]
    if method == 'FLAG':
        response += f'FLAG? I love it! Here is your flag: {FLAG}'
    else:
        response += f'I can\'t feel your {method}!'

    # Send HTTP response
    client_connection.sendall(response.encode())
    client_connection.close()
