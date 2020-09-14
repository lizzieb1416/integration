from tkinter import *

class LabelsFrame(Frame):
    
    def __init__(self, master, relief, width, height, bg):
        Frame.__init__(self, master=master, relief=relief, width=width, height=height, bg=bg)
        
        
        self.lb_item = Label(master=self, text="Item: ") 
        self.lb_quantity = Label(master=self, text="Quantity: ")
        self.lb_type = Label(master=self, text="Product type: ")

        self.lb_item.pack(fill=X)
        self.lb_quantity.pack(fill=X)
        self.lb_type.pack(fill=X)