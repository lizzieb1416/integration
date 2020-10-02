from tkinter import *
from interfaces import IObserver
from tkinter import messagebox

class ResultFrame(Frame, IObserver):
    
    def __init__(self, master, relief, width, height, bg, is_pack=True):
        Frame.__init__(self, master=master, relief=relief, width=width, height=height, bg=bg)
        
        if is_pack:
            self.pack(fill=X)
        
        
        self.label_list = []
        
    def clean_label_list(self):
        for label in self.label_list:
            label.destroy()
        
        self.label_list.clear()
    
    def update(self, shopping_list):
        self.clean_label_list() 
        i = 0
        for key in shopping_list.keys(): 
            elt = shopping_list[key]
            elt_label = Label(master=self, text="{} / {}".format(elt.name, elt.quantity))

            self.label_list.append(elt_label)
            elt_label.pack(fill=X)
            
            i +=1
    
    def update_error(self, error):
        messagebox.showerror("Warning", error.args[0])

# TODO: pasar los botones y los labels de main_view a aqui
        

