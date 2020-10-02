from http.server import HTTPServer, BaseHTTPRequestHandler
import os, os.path
import sys

class WebServer(BaseHTTPRequestHandler):
    
    def do_GET(self):

        try:
            doc = open(os.path.join(sys.path[0], "index.html"), "r")
            file_to_open = doc.read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


# httpd = HTTPServer(('localhost', 8080), WebServer)  #192.168.56.1
# httpd.serve_forever()

