from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import parse_qs

import os

class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        print(postvars)
        return self.do_GET()


hostName, PORT = "localhost", 8001
handler = RequestHandler

server = TCPServer((hostName, PORT), handler)
print(f"Server is running: http://{ hostName }:{ PORT }")
server.serve_forever()

