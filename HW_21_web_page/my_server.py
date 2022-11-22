import socket


def first_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.88.1', 5010))
    server.listen()

    while True:
        print('Working...')
        client, client_addres = server.accept()
        print(f'Connection from {client_addres}')

        while True:
            print('Before .recv()')
            request = client.recv(4096)

            if not request:
                client.close()
                break

            response = f'Hello, {client_addres}'.encode()
            client.send(response)

        print('Out of .recv()')


if __name__ == '__main__':
    first_server()
