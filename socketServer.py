from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from getter import quoteGetter

def accepting_new():
    while True:
        client, client_address = SERVER.accept()
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()

def handle_client(client):
    quote = client.recv(BUFSIZ).decode("utf8")
    print(quoteGetter(stock=quote.upper()))
    while True:
        client.send(bytes(str(quoteGetter(stock=quote)), 'utf8'))


HOST = '127.0.0.1'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)


addresses = {}
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    ACCEPT_THREAD = Thread(target=accepting_new)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
