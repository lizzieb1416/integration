import socket
# # import pylogging
# import os
from mvc.model import Shopping_list 
from threading import Thread
import pickle
import time


class Client(Thread):
    
    def __init__(self, model):
        Thread.__init__(self, name="client_thread")
        
        self.hoste = "192.168.1.47"
        self.port = 12800
        
        self.connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.model = model 
        
    def connection(self):
        self.connection_with_server.connect((self.hoste, self.port)) 
        print("Established connection with server in port {}".format(self.port))

    
    def send_data(self):
       
        msg_to_send = pickle.dumps(self.model) 
        print("CLIENT msg encode : {}".format(msg_to_send))
        self.connection_with_server.send(msg_to_send)
        

    def disconnection(self):
        print("Closing the connection")
        self.connection_with_server.close()

        
    def run(self):
        self.connection()
        while True:
            time.sleep(1)
            self.send_data()
        # self.send_data()