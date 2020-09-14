import socket
# # import pylogging
# import os
from mvc.model import Shopping_list 
from threading import Thread


class Client(Thread):
    
    def __init__(self, model):
        Thread.__init__(self, name="client_thread")
        
        self.hoste = "192.168.1.103"
        self.port = 12800
        
        self.connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.model = model 
        
    def connection(self):
        self.connection_with_server.connect((self.hoste, self.port)) 
        print("Established connection with server in port {}".format(self.port))

    
    def send_data(self):
       
        msg_to_send = self.model.encode()
        print("CLIENT msg encode : {}".format(msg_to_send))
        self.connection_with_server.send(msg_to_send)
        
        # msg_received = self.connection_with_server.recv(1024)
        # print(msg_received.decode())

    def disconnection(self):
        print("Closing the connection")
        self.connection_with_server.close()

        
    def run(self):
        self.connection()
        while True:
            self.send_data()