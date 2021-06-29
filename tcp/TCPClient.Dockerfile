FROM python:3.8-alpine

WORKDIR /app

COPY tcp_client.py ./

ENV HOST_TCP_SERVER=192.168.1.6
ENV PORT_TCP_SERVER=12345

CMD ["python3", "tcp_client.py"]
