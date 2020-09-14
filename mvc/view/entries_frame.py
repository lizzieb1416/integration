from tkinter import *
from tkinter import messagebox

class EntriesFrame(Frame):
    
    def __init__(self, controller, master, relief, width, height, bg):
        Frame.__init__(self, master=master, relief=relief, width=width, height=height, bg=bg)
        
        self.controller = controller
        
        self.entry_item = Entry(master=self)
        self.entry_quantity = Entry(master=self)
        self.entry_type = Entry(master=self)
        
        self.entry_item.pack(fill=X)
        self.entry_quantity.pack(fill=X)
        self.entry_type.pack(fill=X)
        
        btn_add = Button(text="Add item", command=self.on_btn_add_clicked)
        btn_add.grid(row=0, column=2)


    def on_btn_add_clicked(self):
            
        try:
            # self.controller.prout()
            self.controller.add_product(self.entry_item.get(),
                                    self.entry_type.get(),
                                    int(self.entry_quantity.get()), "")
        except ValueError:
            err = "Make sure that Item and Product Type are string and Quantity is an integer."
            messagebox.showerror("Warning", err)
        

        self.entry_item.delete(0, END)
        self.entry_type.delete(0, END)
        self.entry_quantity.delete(0, END)