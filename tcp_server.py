import socket
import threading


HOST = '127.0.0.1'
PORT = 12345


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))
server.listen()
print(f'Listening on {HOST}:{PORT}')


def handle_client_connection(client: socket.socket):
    while True:
        data = client.recv(1024)
        print(f"Received data: {data}")

        if not data:
            print(f'\nClosed connection with {addr[0]}:{addr[1]}')
            break
        client.send(data)


while True:
    connection, addr = server.accept()

    print(f'Accepted connection from {addr[0]}:{addr[1]}')
    client_thread = threading.Thread(
        target=handle_client_connection,
        args=(connection,)
    )
    client_thread.start()
    
