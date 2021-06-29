<div align="center">
    <h1>Sistemas distribuídos</h1>
</div>

## TCP

Aqui será explicado como executar o servidor e o cliente TCP.

#### TCP Server

Para iniciar o container que será responsável por executar o servidor, execute os seguintes comandos:

```console
sd@sd:~$ cd tcp/
sd@sd:~$ docker build -t tcp-server -f TCPServer.Dockerfile .
sd@sd:~$ docker run -d --name tcp-server -p 12345:12345 tcp-server:latest
```

* A opção `-d` fará com que o container seja executado em modo `detached`.
* A opção `-p 12345:12345:` faz o docker expôr a porta `12345` do container para seu computador, assim o serviço ficará visível por outras interfaces de rede dentro da sua máquina.

#### TCP Client

Antes de iniciar verifique o IP da sua máquina dentro da sua rede:

```bash
$ ifconfig
```

Navegue até o arquivo `TCPClient.Dockerfile` e altere o endereço de `HOST_TCP_SERVER` para seu IP, linha  7.

Para iniciar o container que será responsável por executar o servidor, execute os seguintes comandos:

```console
sd@sd:~$ cd tcp/
sd@sd:~$ docker build -t tcp-client -f TCPClient.Dockerfile .
sd@sd:~$ docker run --name tcp-client tcp-client:latest
```

* Aqui não tivemos as opção de mapeamento de porta porque o `client` irá apenas conectar-se ao nosso server executado anteriormente, não iŕa expôr nenhum recurso. E pôr não expôr nenhum recurso, não há nenhuma porta sendo exposta por esse container.

Quando executado, esse container deverá produzir uma saída parecida com a seguinte:

```console
Time: 0.735 m/s
Time: 0.208 m/s
Time: 0.278 m/s
Time: 0.210 m/s
Time: 0.311 m/s
Time: 0.221 m/s
Time: 0.271 m/s
Time: 0.225 m/s
Time: 0.106 m/s
Time: 0.173 m/s


Tempo médio: 0.274 m/s
Desvio padrão: 0.172 
Tempo máximo: 0.735 m/s 
Tempo mínimo: 0.106 m/s
```