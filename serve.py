from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)
    

hostName, PORT = "localhost", 8080
handler = RequestHandler

server = TCPServer((hostName, PORT), handler)
print(f"Server is running: http://{ hostName }:{ PORT }")
server.serve_forever()

