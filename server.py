import socket
import select
import os
import pickle
from threading import Thread
from interfaces import IObserver


from mvc.controller import Controller
import time


class Server(IObserver, Thread):
    
    def __init__(self, model):
        IObserver.__init__(self)
        Thread.__init__(self, name="server_thread")
         
        self._host = ''
        self._port = 12800 
        self._main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._main_connection.setblocking(False)
        # self.main_connection.settimeout(0.05)
        self._connected_clients = []
        
        model.attach(self)
        self._controller = Controller(model)
        
        self._is_running = False

    def _connection(self):
        self._main_connection.bind((self._host, self._port))
        self._main_connection.listen(5)
        print("The server is listening in the port {}".format(self._port))
    
    def _disconnection(self):
        print("Closing the connections")
        for client in self._connected_clients:
            client.close()
         
    def _listen_new_clients(self):
        connection_requests, wlist, xlist = select.select([self._main_connection], [], [], 0.05) 

        for connection in connection_requests: 
            connection_with_client, info_connection = connection.accept()
            self._connected_clients.append(connection_with_client)
               
    def _receive_data(self):
        # connected_clients, wlist, xlist = select.select([self.connected_clients], [], [], 0.05)
        data_received = "" # TODO : direct call inside the lopp when data received
        for client in self._connected_clients:
            try:
                msg_received = client.recv(1024)
            except BlockingIOError as e:
                # print("Problème avec recv : {}".format(e.strerror))
                pass
            except ConnectionResetError: #to handle the error of a client disconnected. It stops brutally the server
                print("The client {} has left the app".format(client))
                client.close()
                self._connected_clients.remove(client)
            else:
                data_received = pickle.loads(msg_received)
                # TODO : make a check or a try/catch
                self._action_on_controller(data_received)
                print("Received: {}".format(data_received))

    def _action_on_controller(self, data_received): 
        
        # data_received = {"action":"add", "name":"apple", "item_type":"fruit", "quantity":3, "unity":"-"}
        
        if data_received["action"] == "add":
            name = data_received["name"] 
            item_type = data_received["item_type"]
            quantity = data_received["quantity"]
            unity = data_received["unity"]
            
            try:
                self._controller.add_product(name, item_type, quantity, unity)
            except ValueError as my_exception:
                self._send_data(my_exception)
        
         # data_received = {"action":"del", "name":"apple"}
        elif data_received["action"] == "del":
            name = data_received["name"]
            
            try:
                self._controller.del_product(name)
            except KeyError as my_exception:
                self._send_data(my_exception)
                    
    def _send_data(self, data):
        for client in self._connected_clients:
            data_to_send = pickle.dumps(data)
            try:
                client.send(data_to_send)
            except BlockingIOError as e:
                print("Problème avec send : {}".format(e.strerror))

    def _do(self):
        self._listen_new_clients()
        self._receive_data()

    def run(self):
        self._connection()
        self._is_running = True
        while self._is_running:
            self._do()
            time.sleep(1)
            
    def stop(self):
        self._is_running = False

    def update(self, subject):
        print("YOUPI OBSERVER CALLED")
        self._send_data(subject)
        
        # data_to_send = {"action":"add", "name":"apple", "item_type":"fruit", "quantity":3, "unity":"-"}
 
    def update_error(self, error: Exception):
        pass