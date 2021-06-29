FROM python:3.8-alpine

WORKDIR /app

COPY . .

ENV HOST_TCP_SERVER=0.0.0.0
ENV PORT_TCP_SERVER=12345

EXPOSE 12345

CMD ["python3", "tcp_server.py"]
