import socket


HOST = '127.0.0.1'
PORT = 54321


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))
print(f'Listening on {HOST}:{PORT}')


while True:
    message, addr = server.recvfrom(1024)

    print(f'Message from: {addr}')

    server.sendto(message, addr)
