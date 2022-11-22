import socket


def first_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.88.1', 5010))
    server.listen()
    while True:
        print('Working...')
        client_socket, client_address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        load_page(data)


def load_page(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    try:
        with open('my_page' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except EOFError:
        return HDRS_404.encode('utf-8')


if __name__ == '__main__':
    first_server()
