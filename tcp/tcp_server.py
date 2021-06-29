import socket # importacao da lib socket para trabalhar com web sockets
import threading # importacao da lib threading para lidar com as threads
import os # importacao da lib os para tratar variáveis de ambiente


def get_env():
    '''
    Obtem as variaveis de host e port onde o servidor ira executar

    return: Tupla com host e porta
    '''

    ENV_HOST = os.environ.get("HOST_TCP_SERVER") # Obtém o host da variável HOST_TCP_SERVER
    ENV_PORT = int(os.environ.get("PORT_TCP_SERVER")) # Obtém a porta da variável PORT_TCP_SERVER

    if ENV_HOST is None or ENV_PORT is None: # Caso nao tenha variaveis de ambiente definidas
        return "127.0.0.1", 12345 # retorna host e porta padrões

    return ENV_HOST, ENV_PORT # caso exista, retorna os valores encontrados
    

HOST, PORT = get_env() # obtem host e porta onde irá executar o servidor


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria uma instancia do servidor com SOCK_STREAM para utilizar protocolo TCP
server.bind((HOST, PORT)) # associa o host e porta ao server criado
server.listen() # faz com que o server esteja ouvindo a rede
print(f'Listening on {HOST}:{PORT}') # mostra informacao de host e porta onde o server está executando


def handle_client_connection(client: socket.socket):
    '''
    Metodo para lidar com as requisicoes vindas de um determinado client

    param: client - Client socket connected
    '''

    while True: # mantem ele ativo enquanto o client estiver mandando algo
        data = client.recv(1024) # recebe os dados enviados pelo client
        print(f"Received data: {data}") # imprime os dados enviados

        # caso nao tenha dados, informa-se que a conexao foi encerrada
        if not data:
            print(f'\nClosed connection with {addr[0]}:{addr[1]}')
            break
        client.send(data) # envia os dados de volta ao client


# Mantem essa execucao e permite que o server fique ouvindo a rede
while True:
    connection, addr = server.accept() # identifica e aceita uma nova conexao

    print(f'Accepted connection from {addr[0]}:{addr[1]}') # imprime na tela as informacoes do host que acabou de se conectar
    
    # cria uma nova thread para esse novo host e o mantem por meio do metodo handle_client_connection
    # passando a conexao em questao
    client_thread = threading.Thread(
        target=handle_client_connection,
        args=(connection,)
    )

    # dá inicio a nova thread criada
    client_thread.start()
    
