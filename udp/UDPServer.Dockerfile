FROM python:3.8-alpine

WORKDIR /app

COPY udp_server.py .

ENV HOST_UDP_SERVER=0.0.0.0
ENV PORT_UDP_SERVER=54321

EXPOSE 54321

CMD ["python3", "udp_server.py"]
