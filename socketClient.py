from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while True:
    print(client.recv(2048).decode("utf8"));
    client.send(bytes('WORK', "utf8"))
client.close()
