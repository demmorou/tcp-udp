import socket
import os

def get_env():
    ENV_HOST = os.environ.get("HOST_UDP_SERVER")
    ENV_PORT = int(os.environ.get("PORT_UDP_SERVER"))

    if ENV_HOST is None or ENV_PORT is None:
        return "127.0.0.1", 54321

    return ENV_HOST, ENV_PORT
    

HOST, PORT = get_env()


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f'Listening on {HOST}:{PORT}')


while True:
    message, addr = server.recvfrom(1024)

    print(f'Message from: {addr}')

    server.sendto(message, addr)
