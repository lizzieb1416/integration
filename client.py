import socket
# # import pylogging
# import os
from mvc.model import Shopping_list 
from threading import Thread
import pickle
import time
from interfaces import ISubject, IController


class Client(ISubject, IController, Thread):
    
    def __init__(self):
        Thread.__init__(self, name="client_thread")
        
        self.host = "192.168.1.47"
        self.port = 12800
        
        self.connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_with_server.setblocking(False)
        self.connection_with_server.settimeout(10)

        self.model = None
        self._is_running = False
        
        self.observer_list = []

    def _connection(self):
        try:
            self.connection_with_server.connect((self.host, self.port)) 
        except ConnectionRefusedError:
            self.notify_error(ConnectionResetError("There is no server to connect to"))
        else:
            print("Established connection with server in port {}".format(self.port))

    def _send_data(self, data):
        data_to_send = pickle.dumps(data)
        try:
            self.connection_with_server.send(data_to_send)
        except BlockingIOError as e:
            print("Problème avec send : {}".format(e.strerror))
        # except Exception:
        #     print("Timeout avec recv")       
        
    def _receive_data(self):
        try:
            msg_received = self.connection_with_server.recv(1024)
        except BlockingIOError as e:
            print("Problème avec recv : {}".format(e.strerror))
        except ConnectionResetError:
            self.notify_error(ConnectionResetError("SERVER DECO"))
            self._disconnection()
        except Exception:
            # print("Timeout avec recv")         # TODO WARNING THERE IS A TIMEOUT EXCEPTION cause by settimeout
            pass
        else:
            data_received = pickle.loads(msg_received)
            if isinstance(data_received, Exception):
                self.notify_error(data_received)
            elif isinstance(data_received, Shopping_list):
                self.model = data_received
                self.notify()
                print("Received: {}".format(data_received))     
            else:
                raise Exception
    
    def notify_error(self, error):
        for observer in self.observer_list:
            observer.update_error(error)
              
    def _disconnection(self):
        print("Closing the connection")
        self.connection_with_server.close()

    def _do(self):
        self._receive_data()
        
    def run(self):
        self._connection()
        self._is_running = True
        while self._is_running:
            self._do()
            time.sleep(1)


  
    # Implement IController interface (goal is to have a Proxy Controller) 

    def add_product(self, name, item_type, quantity, unity):
        
        data_to_send = {}
        
        data_to_send["action"] = "add"
        data_to_send["name"] = name
        data_to_send["item_type"] = item_type
        data_to_send["quantity"] = quantity
        data_to_send["unity"] = unity
        
        self._send_data(data_to_send)
    
    def del_product(self, name):
              
        data_to_send = {}
        
        data_to_send["action"] = "del"
        data_to_send["name"] = name
        
        self._send_data(data_to_send)
    
    def subscribe_to_model(self, observer): # Controller is not an observable but is a bridge to attach to the model
        self.attach(observer)
    
    def unsubscribe_to_model(self, observer):
        self.detach(observer)


    # Implement IObserver interface

    def attach(self, observer):
        self.observer_list.append(observer)
    
    def detach(self, observer):
        self.observer_list.remove(observer)

    def notify(self):
        for observer in self.observer_list:
            observer.update(self.model)
            