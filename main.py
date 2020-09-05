import mvc.controller as controller
import mvc.model as model
import mvc.view as view
import time
from threading import Thread

if __name__ == "__main__":

    class LogSL(Thread):
        
        def __init__(self, sl):
            Thread.__init__(self)
            self.sl = sl
            
        def run(self):
            while True:
                print(SHOPPING_LIST)
                time.sleep(2)
            

    print("DEBUT")
    

    
    # Model
    SHOPPING_LIST = model.Shopping_list()

    # Classe de log
    SLog = LogSL(SHOPPING_LIST)
    SLog.start()
    
    # Controller
    CONTROLLER = controller.Controller(SHOPPING_LIST)
    
 
    # Vue
    VIEW = view.View(CONTROLLER)
    
    # # Link Vue => Controller => Model
    # CONTROLLER._sl = SHOPPING_LIST
    # CONTROLLER.add_product("apple", "fruit", 1, "kg")
    # CONTROLLER.add_product("grapes", "fruit", 2, "kg")
      
    
    # SHOPPING_LIST.name = "frutas"
    # print(SHOPPING_LIST)
    
    VIEW.run()


    SLog.join()