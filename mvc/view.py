from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class View(Tk):
    
    def __init__(self, controller):
        Tk.__init__(self)
        
        self.controller = controller
        
        self.title("Babylove's Shopping List")
        # self.geometry("600x400")
    
        self.columnconfigure([0, 1, 2, 3], minsize=100)
        self.rowconfigure(0, minsize=100)
        
        self.create_list_frame = Frame(master=self, relief=RAISED, width=50, height=300, bg="floral white")
        self.label_frame = Frame(master=self, relief=RAISED, width=200, height=300, bg="antique white")
        self.entry_frame = Frame(master=self, relief=RAISED, width=200, height=300, bg="antique white")
        self.shopping_list_frame = Frame(master=self, relief=RAISED, width=400, height=300, bg="bisque")

        self.create_list_frame.grid(row=0, sticky="nsew", column=0)
        self.label_frame.grid(row=0, sticky="nsew", column=1)
        self.entry_frame.grid(row=0, sticky="nsew", column=2)
        self.shopping_list_frame.grid(row=0, sticky="nsew", column=3)
        
        
        # Labels 

        self.lb_item = Label(master=self.label_frame, text="Item: ") 
        self.lb_quantity = Label(master=self.label_frame, text="Quantity: ")
        self.lb_type = Label(master=self.label_frame, text="Product type: ")
        
        self.lb_result_list = Label(master=self.shopping_list_frame, text="")

        self.lb_item.pack(fill=X)
        self.lb_quantity.pack(fill=X)
        self.lb_type.pack(fill=X)
        self.lb_result_list.pack(fill=X)

        # entries

        self.entry_item = Entry(master=self.entry_frame)
        self.entry_quantity = Entry(master=self.entry_frame)
        self.entry_type = Entry(master=self.entry_frame)

        # self.entry_item.focus()
        # self.entry_quantity.focus()
        # self.entry_type.focus()
        # self.entry_item.bind("<Return>", self.return_entry)
        # self.entry_quantity.bind("<Return>", self.return_entry)
        # self.entry_type.bind("<Return>", self.return_entry)
        
        self.entry_item.pack(fill=X)
        self.entry_quantity.pack(fill=X)
        self.entry_type.pack(fill=X)
        
        

        # Buttoms 

        btn_create = Button(text="Create List")
        btn_add = Button(text="Add item", command=self.on_btn_add_clicked)
        btn_create.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        btn_add.grid(row=0, column=2)
                
                #lambda:[self.funcA(), self.funcB(), self.funcC()])
                #command=lambda:[self.on_btn_add_clicked, self.return_entry])
        
    def run(self):
        self.mainloop()
        
        
    def on_btn_add_clicked(self):
     
        # err = " "
        # try:
        #     str(self.entry_item.get())
        #     str(self.entry_type.get())
        #     int(self.entry_quantity.get())
        # except ValueError: 
        #     print("Not okay")
        #     err = "Make sure that Item and Product Type are string and Quantity is an integer."
        #     messagebox.showerror("Warning", err)
        # else:
            # self.controller.add_product(self.entry_item.get(),
            #                               self.entry_type.get(),
            #                               int(self.entry_quantity.get()), "")
            # print("Okay")
            
            # self.return_entry()
            
        try:
            self.controller.add_product(self.entry_item.get(),
                                    self.entry_type.get(),
                                    int(self.entry_quantity.get()), "")
        except ValueError:
            err = "Make sure that Item and Product Type are string and Quantity is an integer."
            messagebox.showerror("Warning", err)
        


        self.entry_item.delete(0, END)
        self.entry_type.delete(0, END)
        self.entry_quantity.delete(0, END)
            
            
    def return_entry(self):
   
        a = self.entry_item.get()
        b = self.entry_quantity.get()
        c = self.entry_type.get()
        
        result = "> Item: {}, Quantity: {}, Type: {}".format(a, b, c)
        
        self.lb_result_list["text"] = result












    
    
    
            
        # a = self.entry_item.get()
        # b = self.entry_quantity.get()
        # c = self.entry_type.get()
        
        # result = "> Item: {}, Quantity: {}, Type: {}".format(a, b, c)
        
        # self.lb_result_list.config(text=result)
        