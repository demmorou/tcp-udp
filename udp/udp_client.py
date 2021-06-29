import socket
from time import time
from statistics import mean, stdev
import os


def get_env():
    ENV_HOST = os.environ.get("HOST_UDP_SERVER")
    ENV_PORT = int(os.environ.get("PORT_UDP_SERVER"))

    if ENV_HOST is None or ENV_PORT is None:
        return "127.0.0.1", 54321

    return ENV_HOST, ENV_PORT
    

HOST, PORT = get_env()


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    response_times = []

    for i in range(10):
        start = time()

        client.sendto("Hello World".encode(), (SERVER_HOST, SERVER_PORT))

        end = time()
        diff = (end - start) * 1000
        response_times.append(diff)
        print("Time: %.3f m/s" % diff)
    
    print('\n')
    print("Tempo médio: %.3f m/s" % mean(response_times))
    print("Desvio padrão: %.3f " % stdev(response_times))
    print("Tempo máximo: %.3f m/s " % max(response_times))
    print("Tempo mínimo: %.3f m/s " % min(response_times))