from tkinter import *

class CreateListFrame(Frame):
    
    def __init__(self, master, relief, width, height, bg):
        Frame.__init__(self, master=master, relief=relief, width=width, height=height, bg=bg)
        
        self.btn_create = Button(text="Create List")
        self.btn_create.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        
        
# este Frame deberia permitir:
# *Permitir el acceso a la frame del ingreso de datos
# *ingresar el titulo de la lista
