from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        content = int(self.headers.get("Content-Length"))
        body = self.rfile.read(content)
        print(body)
        return self.do_GET()


hostName, PORT = "localhost", 8082
handler = RequestHandler

server = TCPServer((hostName, PORT), handler)
print(f"Server is running: http://{ hostName }:{ PORT }")
server.serve_forever()

