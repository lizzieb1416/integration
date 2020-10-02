# import mvc.controller as controller
# from threading import Thread
from server import Server

from web_server.html_creator import HTMLCreator
from web_server.web_server import WebServer
from http.server import HTTPServer, BaseHTTPRequestHandler
from mvc.model import Shopping_list
import mvc.controller as controller

if __name__ == "__main__":

    MODEL = Shopping_list()
    # MODEL = {"action":"add", "name":"apple", "item_type":"fruit", "quantity":3, "unity":"-"}
    HTMLCREATOR = HTMLCreator(MODEL)
    SERVER = Server(MODEL)
    
    print(MODEL)
    
    SERVER.start()
    
    WEBSERVER = HTTPServer(('192.168.1.47', 8080), WebServer)
    WEBSERVER.serve_forever()
    
    
    
    
    
    

    
    
