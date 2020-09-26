import mvc.controller as controller
import mvc.model as model
import mvc.view.main_view as view
import time
from threading import Thread
import client
# from web_server.html_creator import HTMLCreator
# # from web_server.web_server import WebServer

if __name__ == "__main__":

    class LogSL(Thread):
        
        def __init__(self, sl):
            Thread.__init__(self)
            self.sl = sl
            
        def run(self):
            while True:
                print(MODEL)
                time.sleep(2)
            

    print("DEBUT")
    

    # Model
    MODEL = model.Shopping_list()
    
    # Controller
    CONTROLLER = controller.Controller(MODEL)

    # Vue
    VIEW = view.MainView(CONTROLLER, MODEL)
    
    # # Link Vue => Controller => Model

    # Client
    CLIENT = client.Client(MODEL)
    CLIENT.start()
    
    # HTMLFILE = HTMLCreator(MODEL)
    # HTMLFILE.start()

    VIEW.do()
    

    