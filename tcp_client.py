import socket
from statistics import mean, stdev
from time import sleep, time


HOST = "127.0.0.1"
PORT = 12345


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
