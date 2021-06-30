import socket # importacao da lib socket para trabalhar com web sockets
from time import time, sleep  # importacao da lib sleep para dar um tempo ate a proxima instrucao e da lib time para pegar o timestamp exato
from statistics import mean, stdev # importacao das libs mean e stdev para calcular a media e o desvio padrao
import os # importacao da lib os para tratar variáveis de ambiente


def get_env():
    '''
    Obtem as variaveis de host e port onde o servidor está executando

    return: Tupla com host e porta
    '''

    ENV_HOST = os.environ.get("HOST_UDP_SERVER") # Obtém o host da variável HOST_UDP_SERVER
    ENV_PORT = os.environ.get("PORT_UDP_SERVER") # Obtém a porta da variável PORT_UDP_SERVER

    if ENV_HOST is None or ENV_PORT is None: # Caso nao tenha variaveis de ambiente definidas
        return "127.0.0.1", 54321 # retorna host e porta default

    return ENV_HOST, ENV_PORT # caso exista, retorna os valores encontrados


HOST, PORT = get_env() # obtem host e porta onde está executando o servidor

print(HOST, PORT)

# abre uma conexao com o web socket utilizando o protocolo UDP
# com a conexao aberta realiza algumas acoes
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    response_times = [] # cria um array vazio para armazenar informacoes posteriormente

    # inici um loop (10 voltas) com a estrutura de repeticao for
    for i in range(10):
        start = time() # pega o momento onde a requisicao será feita

        client.sendto("Hi, Server. I'm an UDP Client.".encode(), (HOST, int(PORT))) # envia dados para o servidor especificando host e a porta
        message, addr = client.recvfrom(1024)

        print(f"From server: {message.decode()}")
        # aqui ele deve receber uma mensagem do servidor tipo um ACK

        end = time() # pega o momento onde a requisicao se encerra

        diff = (end - start) * 1000 # pega a diferenca do fim e inicio da requisicao enviada em ms
        response_times.append(diff) # adiciona ao array
        print("Time: %.3f m/s" % diff) # imprime na tela o tempo gasto durante a requisicao
        # sleep(1) # espera 1 segundo até enviar novamente outra requisicao

    print('\n') # imprime uma quebra de linha
    print("Tempo médio: %.3f m/s" % mean(response_times)) # imprime o valor da media de tempo
    print("Desvio padrão: %.3f " % stdev(response_times)) # imprime o valor do desvio padrao
    print("Tempo máximo: %.3f m/s " % max(response_times)) # imprime o valor do tempo maximo
    print("Tempo mínimo: %.3f m/s " % min(response_times)) # imprime o valor do tempo minimo