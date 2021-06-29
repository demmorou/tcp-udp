import socket # importacao da lib socket para trabalhar com web sockets
from statistics import mean, stdev # importacao das libs mean e stdev para calcular a media e o desvio padrao
from time import sleep, time # importacao da lib sleep para dar um tempo ate a proxima instrucao e da lib time para pegar o timestamp exato
import os # importacao da lib os para tratar variáveis de ambiente
 

def get_env():
    '''
    Obtem as variaveis de host e port onde o servidor está executando

    return: Tupla com host e porta
    '''

    ENV_HOST = os.environ.get("HOST_TCP_SERVER") # Obtém o host da variável HOST_TCP_SERVER
    ENV_PORT = os.environ.get("PORT_TCP_SERVER") # Obtém a porta da variável PORT_TCP_SERVER

    if ENV_HOST is None or ENV_PORT is None: # Caso nao tenha variaveis de ambiente definidas
        return "127.0.0.1", 12345 # retorna host e porta padrões

    return ENV_HOST, ENV_PORT # caso exista, retorna os valores encontrados


HOST, PORT = get_env() # obtem host e porta onde está executando o servidor

# abre uma conexao com o web socket utilizando o protocolo TCP
# com a conexao aberta realiza algumas acoes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT)) # conecta-se ao servidor

    response_times = [] # cria um array vazio para armazenar informacoes posteriormente

    # inici um loop (10 voltas) com a estrutura de repeticao for
    for i in range(10):
        start = time() # pega o momento onde a requisicao será feita

        client.send(b"Hello world") # envia dados para o servidor
        data = client.recv(1024) # recebe as informacoes do servidor

        end = time() # pega o momento onde a requisicao se encerra

        diff = (end - start) * 1000 # pega a diferenca do fim e inicio da requisicao enviada em ms
        response_times.append(diff) # adiciona ao array
        print("Time: %.3f m/s" % diff) # imprime na tela o tempo gasto durante a requisicao
        sleep(1) # espera 1 segundo até enviar novamente outra requisicao

    print('\n') # imprime uma quebra de linha
    print("Tempo médio: %.3f m/s" % mean(response_times)) # imprime o valor da media de tempo
    print("Desvio padrão: %.3f " % stdev(response_times)) # imprime o valor do desvio padrao
    print("Tempo máximo: %.3f m/s " % max(response_times)) # imprime o valor do tempo maximo
    print("Tempo mínimo: %.3f m/s " % min(response_times)) # imprime o valor do tempo minimo
