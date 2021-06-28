import socket


HOST = '127.0.0.1'
PORT = 12345


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))
server.listen()
print(f'Listening on {HOST}:{PORT}')


while True:
    connection, addr = server.accept()

    with connection:
        print(f'Accepted connection from {addr[0]}:{addr[1]}')

        while True:
            data = connection.recv(1024)
            if not data:
                print(f'Closed connection with {addr[0]}:{addr[1]}')
                break
            connection.sendall(data)
    