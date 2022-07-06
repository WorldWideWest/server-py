from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from urllib.parse import parse_qs

from constants import Constants

constants = Constants

class RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.path = "index.html"
        return SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        postvars = parse_qs(self.rfile.read(length).decode("utf-8"), keep_blank_values = 1)
        
        print(postvars.get("taskName")) 
        return self.do_GET()


handler = RequestHandler

server = TCPServer((constants.HOST_NAME.value, constants.PORT.value), handler)
print(f"Server is running: http://{ constants.HOST_NAME.value }:{ constants.PORT.value }")
server.serve_forever()

