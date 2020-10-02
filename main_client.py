import mvc.controller as controller
import mvc.model as model
import mvc.view.main_view as view
import time
# from threading import Thread
from client import Client
# from web_server.html_creator import HTMLCreator
# # from web_server.web_server import WebServer

if __name__ == "__main__":
    
    ## Client in local 
    # MODEL = model.Shopping_list()
    # CONTROLLER = controller.Controller(MODEL)

    #Client in remote
    CONTROLLER = Client()
    CONTROLLER.start()
    
    VIEW = view.MainView(CONTROLLER)
    VIEW.run()
    

    
    
    
    
    
    
    
    
    ## Model
    # MODEL = model.Shopping_list()
    
    # # Controller
    # CONTROLLER = controller.Controller(MODEL)

    # # Vue
    # VIEW = view.MainView(CONTROLLER, MODEL)
    
    # # # Link Vue => Controller => Model

    # # Client
    # CLIENT = client.Client(MODEL)
    # CLIENT.start()

    # VIEW.do()
    

    
    
    
    # CONTROLLER.add_product("banane", "fruit", 5, "-")
    # CONTROLLER.add_product("apple", "fruit", 10, "-")
    # CONTROLLER.add_product("onion", "vegetable", 4, "-")
    # print(MODEL)
    
    # CONTROLLER.del_product("apple")
    # CONTROLLER.del_product("onion")
    # print(MODEL)