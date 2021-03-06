<div align="center">
    <h1>Sistemas distribuídos</h1>
</div>

### Importante

Antes de iniciar verifique o IP da sua máquina dentro da sua rede:

```bash
$ ifconfig
```

Navegue até o arquivo `TCPClient.Dockerfile` e altere o endereço de `HOST_TCP_SERVER` para seu IP, linha  7.

Faça o mesmo para o arquivo `UDPClient.Dockerfile` e altere o endereço de `HOST_UDP_SERVER` para o seu IP, linha 7.

## TCP

Aqui será explicado como executar o servidor e o cliente TCP.

<br>

#### TCP Server

Para iniciar o container que será responsável por executar o servidor, execute os seguintes comandos:

```console
sd@sd:~$ cd tcp/
sd@sd:~$ docker build -t tcp-server -f TCPServer.Dockerfile .
sd@sd:~$ docker run -d -p 12345:12345 tcp-server:latest
```

* A opção `-d` fará com que o container seja executado em modo `detached`.
* A opção `-p 12345:12345:` faz o docker expôr a porta `12345` do container para seu computador, assim o serviço ficará visível por outras interfaces de rede dentro da sua máquina.

#### TCP Client

Para iniciar o container que será responsável por executar o papel de client, execute os seguintes comandos:

```console
sd@sd:~$ cd tcp/
sd@sd:~$ docker build -t tcp-client -f TCPClient.Dockerfile .
sd@sd:~$ docker run tcp-client:latest
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

## UDP

Aqui será explicado como executar o servidor e o cliente UDP.

<br>

#### UDP Server

Para iniciar o container que será responsável por executar o servidor, execute os seguintes comandos:

```console
sd@sd:~$ cd udp/
sd@sd:~$ docker build -t udp-server -f UDPServer.Dockerfile .
sd@sd:~$ docker run -d -p 54321:54321/udp udp-server:latest
```

* A opção `-d` fará com que o container seja executado em modo `detached`.
* A opção `-p 54321:54321/udp` faz o docker expôr a porta `54321` do container para seu computador, assim o serviço ficará visível por outras interfaces de rede dentro da sua máquina.
* Note que em `-p 54321:54321/udp`, utilizamos  um `/udp`, isso é necessário porque, por padrão o docker mantém uma comunicação `TCP` e nesse caso precisamos que seja uma comunicação `UDP`.

#### UDP Client

Para iniciar o container que será responsável por executar o papel de client, execute os seguintes comandos:

```console
sd@sd:~$ cd udp/
sd@sd:~$ docker build -t udp-client -f UDPClient.Dockerfile .
sd@sd:~$ docker run udp-client:latest
```

* Aqui não tivemos as opção de mapeamento de porta porque o `client` irá apenas conectar-se ao nosso server executado anteriormente, não iŕa expôr nenhum recurso. E pôr não expôr nenhum recurso, não há nenhuma porta sendo exposta por esse container.

Quando executado, esse container deverá produzir uma saída parecida com a seguinte:

```console
From server: Hi, Client. Ok!
Time: 0.174 m/s
From server: Hi, Client. Ok!
Time: 0.116 m/s
From server: Hi, Client. Ok!
Time: 0.086 m/s
From server: Hi, Client. Ok!
Time: 0.080 m/s
From server: Hi, Client. Ok!
Time: 0.074 m/s
From server: Hi, Client. Ok!
Time: 0.091 m/s
From server: Hi, Client. Ok!
Time: 0.065 m/s
From server: Hi, Client. Ok!
Time: 0.098 m/s
From server: Hi, Client. Ok!
Time: 0.081 m/s
From server: Hi, Client. Ok!
Time: 0.107 m/s


Tempo médio: 0.097 m/s
Desvio padrão: 0.031 
Tempo máximo: 0.174 m/s 
Tempo mínimo: 0.065 m/s
```