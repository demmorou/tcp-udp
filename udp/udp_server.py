import socket # importacao da lib socket para trabalhar com web sockets
import os # importacao da lib os para tratar variáveis de ambiente


def get_env():
    '''
    Obtem as variaveis de host e port onde o servidor ira executar

    return: Tupla com host e porta
    '''

    ENV_HOST = os.environ.get("HOST_UDP_SERVER") # Obtém o host da variável HOST_UDP_SERVER
    ENV_PORT = int(os.environ.get("PORT_UDP_SERVER")) # Obtém a porta da variável PORT_UDP_SERVER

    if ENV_HOST is None or ENV_PORT is None: # Caso nao tenha variaveis de ambiente definidas
        return "127.0.0.1", 54321 # retorna host e porta padrões

    return ENV_HOST, ENV_PORT # caso exista, retorna os valores encontrados
    

HOST, PORT = get_env() # obtem host e porta onde irá executar o servidor


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria uma instancia do servidor com SOCK_STREAM para utilizar protocolo UDP
server.bind((HOST, PORT)) # associa o host e porta ao server criado
print(f'Listening on {HOST}:{PORT}') # mostra informacao de host e porta onde o server está executando


# inicia um loop infinito e mantem o server sempre ouvindo a rede
while True:
    message, addr = server.recvfrom(1024) # recebe as informacoes que chegam dos clients

    print(f'Message from: {addr}') # imprime na tela as informacoes recebidas

    server.sendto(message, addr) # envia de volta para o mesmo client
