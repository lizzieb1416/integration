import mvc.controller as controller
import mvc.model as model
import mvc.view.main_view as view
import time
from threading import Thread
import client

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

    # # Classe de log
    # SLog = LogSL(MODEL)
    # SLog.start()
    
    # Controller
    CONTROLLER = controller.Controller(MODEL)
    
 
    # Vue
    VIEW = view.MainView(CONTROLLER, MODEL)
    
    # # Link Vue => Controller => Model

    # Client
    CLIENT = client.Client(MODEL)
    CLIENT.start()
    
    VIEW.do()

    # SLog.join()
    