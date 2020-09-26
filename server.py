import socket
import select
import os
import pickle
from threading import Thread

from mvc.model import Shopping_list


class Server(Thread):
    
    def __init__(self, imodel):
        Thread.__init__(self, name="server_thread")
         
        self.hoste = ''
        self.port = 12800 
        self.main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected_clients = []
        self.model = imodel

    def connection(self):
        self.main_connection.bind((self.hoste, self.port))
        self.main_connection.listen(5)
        print("The server is listening in the port {}".format(self.port))
        
    def receive_model(self):
        server_launch = True
        
        while server_launch:
            connection_requests, wlist, xlist = select.select([self.main_connection], [], [], 0.05) 

            for connection in connection_requests: 
                connection_with_client, info_connection = connection.accept()
                self.connected_clients.append(connection_with_client)
            
            clients_to_read = []

            try:
                clients_to_read, wlist, xlist = select.select(self.connected_clients, [], [], 0.05)
            except select.error:
                pass
            else:
                for client in clients_to_read:
                    msg_received = client.recv(1024)
                    data_received = pickle.loads(msg_received)
                    # if not isinstance(msg_received, Shopping_list):
                    #     raise ConnectionError
             
                    self.model = data_received
                    print("Received: {}".format(data_received))


    def disconnection(self):
        print("Closing the connections")
        for client in self.connected_clients:
            client.close()
 
    
    def run(self):
        self.connection()
        self.receive_model()
     

# server = Server()
# server.run()

