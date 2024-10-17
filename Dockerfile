FROM python:latest
WORKDIR /app
RUN pip install flask
COPY src/ src/
ENTRYPOINT [ "python", "/app/src/start_server.py" ]