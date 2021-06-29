import socket
import threading
import os


def get_env():
    ENV_HOST = os.environ.get("HOST_TCP_SERVER")
    ENV_PORT = int(os.environ.get("PORT_TCP_SERVER"))

    if ENV_HOST is None or ENV_PORT is None:
        return "127.0.0.1", 12345

    return ENV_HOST, ENV_PORT
    

HOST, PORT = get_env()


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
    
