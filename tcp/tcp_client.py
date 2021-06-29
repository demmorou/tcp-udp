import socket
from statistics import mean, stdev
from time import sleep, time
import os


def get_env():
    ENV_HOST = os.environ.get("HOST_TCP_SERVER")
    ENV_PORT = int(os.environ.get("PORT_TCP_SERVER"))

    if ENV_HOST is None or ENV_PORT is None:
        return "127.0.0.1", 12345

    return ENV_HOST, ENV_PORT


HOST, PORT = get_env()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    response_times = []

    for i in range(10):
        start = time()

        client.send(b"Hello world")
        data = client.recv(1024)

        end = time()
        diff = (end - start) * 1000
        response_times.append(diff)
        print("Time: %.3f m/s" % diff)
        sleep(1)

    print('\n')
    print("Tempo médio: %.3f m/s" % mean(response_times))
    print("Desvio padrão: %.3f " % stdev(response_times))
    print("Tempo máximo: %.3f m/s " % max(response_times))
    print("Tempo mínimo: %.3f m/s " % min(response_times))
