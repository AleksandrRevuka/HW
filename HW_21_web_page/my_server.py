import socket


def first_server():
    global server
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.88.1', 5010))
        server.listen()
        while True:
            print('Working...')
            client_socket, client_address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            content = load_page(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Shutdown")


def load_page(request_data):
    try:
        path = request_data.split(' ')[1]
    except IndexError:
        path = '/'
    if path == '/':
        path = '/index.html'
    try:
        with open('my_page' + path, 'rb') as file:
            response = file.read()
        if 'css' in path:
            return HDRS_CSS.encode() + response
        return HDRS_HTML.encode() + response
    except FileNotFoundError:
        return (HDRS_404 + '<h1>Sorry, page is not found<h1>').encode()


HDRS_HTML = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\n\r\n'
HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'

if __name__ == '__main__':
    first_server()
