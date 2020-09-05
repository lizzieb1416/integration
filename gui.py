from tkinter import *
import model
import controller


window = Tk()
window.title("Babylove's Shopping List")
window.columnconfigure([0, 1, 2, 3], minsize=100)
window.rowconfigure(0, minsize=100)

# 4 frames

frame1 = Frame(master=window, relief=RAISED, width=50, height=300, bg="floral white")
frame2 = Frame(master=window, relief=RAISED, width=200, height=300, bg="antique white")
frame3 = Frame(master=window, relief=RAISED, width=200, height=300, bg="antique white")
frame4 = Frame(master=window, relief=RAISED, width=400, height=300, bg="bisque")

frame1.grid(row=0, sticky="nsew", column=0)
frame2.grid(row=0, sticky="nsew", column=1)
frame3.grid(row=0, sticky="nsew", column=2)
frame4.grid(row=0, sticky="nsew", column=3)

# Labels 

lb_item = Label(master=frame2, text="Item: ") 
lb_quantity = Label(master=frame2, text="Quantity: ")
lb_type = Label(master=frame2, text="Product type: ")
lb_result_list = Label(master=frame4, text="This is your list")

lb_item.pack(fill=X)
lb_quantity.pack(fill=X)
lb_type.pack(fill=X)
lb_result_list.pack(fill=X)

# entries

entry_item = Entry(master=frame3)
entry_quantity = Entry(master=frame3)
entry_type = Entry(master=frame3)

entry_item.pack(fill=X)
entry_quantity.pack(fill=X)
entry_type.pack(fill=X)

# Buttoms 

btn_create = Button(text="Create List")
btn_add = Button(text="Add item")
btn_create.grid(row=0, column=0, sticky="n", padx=5, pady=5)
btn_add.grid(row=0, column=2)

window.mainloop()








# window = Tk()
# window.title("Babylove's Shopping List")
# window.geometry("600x400")
# window.rowconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)

# frame_left = Frame(window, relief=RAISED, bd=2)
# frame_right = Frame(window)
# frame_left.grid(row=0, column=0, sticky="ns")


# btn_create = Button(frame_left, text="Create list")
# btn_create.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

# window.mainloop()
