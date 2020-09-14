from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from threading import Thread

from mvc.view.result_frame import ResultFrame
from mvc.view.create_list_frame import CreateListFrame
from mvc.view.labels_frame import LabelsFrame
from mvc.view.entries_frame import EntriesFrame

class MainView(Tk):
    
    
    def __init__(self, controller, model):
        Tk.__init__(self)
        
        
        self.title("Babylove's Shopping List")
    
        self.columnconfigure([0, 1, 2, 3], minsize=100)
        self.rowconfigure(0, minsize=100)
        
        # CreateListFrame
        self.create_list_frame = CreateListFrame(master=self, relief=RAISED, width=50, height=300, bg="floral white")

        # LabelsFrame
        self.labels_frame = LabelsFrame(master=self, relief=RAISED, width=200, height=300, bg="antique white")
        
        # EntriesFrame
        self.entries_frame = EntriesFrame(master=self, controller=controller, relief=RAISED, width=200, height=300, bg="antique white")
       
        # ResultFrame
        self.shopping_list_frame = ResultFrame(master=self, relief=RAISED, width=400, height=300, bg="bisque", is_pack=False)
        model.attach(self.shopping_list_frame)
        
        

        self.create_list_frame.grid(row=0, sticky="nsew", column=0)
        self.labels_frame.grid(row=0, sticky="nsew", column=1)
        self.entries_frame.grid(row=0, sticky="nsew", column=2)
        self.shopping_list_frame.grid(row=0, sticky="nsew", column=3)
        

        
    def do(self):
        self.mainloop()
                









    