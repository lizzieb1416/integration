from mvc.view.result_frame import ResultFrame
from mvc.model import *
from tkinter import *
import time

window = Tk()

SL = Shopping_list()
PRODUCT1 = Product()
PRODUCT2 = Product()

PRODUCT1.name = "pomme"
PRODUCT1.item_type = "fruit"
PRODUCT1.quantity = 4

PRODUCT2.name = "banane"
PRODUCT2.item_type = "legume"
PRODUCT2.quantity = 6



RF = ResultFrame(master=window, relief=RAISED, width=400, height=300, bg="bisque")

SL.attach(RF)

SL[PRODUCT1.name] = PRODUCT1

window.mainloop()