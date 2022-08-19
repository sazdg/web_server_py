from http.server import HTTPServer, BaseHTTPRequestHandler
from queue import Empty


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.path = '/index.html'
            print("index page")

            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file_to_open = "non trovato"
                self.send_response(404)
            self.end_headers()
            #per scrivere sullo schermo
            self.wfile.write(bytes(file_to_open, 'utf-8'))

        else:
            cookie = self.path.split('/')
            if cookie[1] != 'index.html' and cookie[1] != 'favicon.ico':
                print("cookie ricevuti: " + cookie[1])
                self.send_response(200, self.path)

try:
    server = HTTPServer(('localhost', 8080), Serv)
    print('Started http server')
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    server.socket.close()