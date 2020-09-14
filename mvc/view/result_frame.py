from tkinter import *
from interface.IObserver import IObserver

class ResultFrame(Frame, IObserver):
    
    def __init__(self, master, relief, width, height, bg, is_pack=True):
        Frame.__init__(self, master=master, relief=relief, width=width, height=height, bg=bg)
        
        if is_pack:
            self.pack(fill=X)
        
        
        self.label_list = []
        
        
    def update(self, shopping_list):
        # self.label_list.clear()  
        i = 0
        for key in shopping_list.keys(): 
            elt = shopping_list[key]
            elt_label = Label(master=self, text="{} / {}".format(elt.name, elt.quantity))

            self.label_list.append(elt_label)
            elt_label.pack(fill=X)
            
            i +=1
            

# TODO: pasar los botones y los labels de main_view a aqui
        

