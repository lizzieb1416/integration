# import mvc.controller as controller
from threading import Thread
from server import Server

from web_server.html_creator import HTMLCreator
from web_server.web_server import WebServer
from http.server import HTTPServer, BaseHTTPRequestHandler
from mvc.model import Shopping_list

if __name__ == "__main__":

    MODEL = Shopping_list()
    
    SERVER = Server(MODEL)
    SERVER.start()
    
        
    HTMLCREATOR = HTMLCreator(SERVER)
    HTMLCREATOR.start()
    
    WEBSERVER = HTTPServer(('localhost', 8080), WebServer)
    WEBSERVER.serve_forever()
    
    

    
    
    
    