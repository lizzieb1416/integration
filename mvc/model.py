from interface.ISubject import ISubject
import base64

class Product():
    
    def __init__(self, ):
        self.name = None
        self.item_type = None
        self.quantity = None
        self.unity = None
        
    def __repr__(self):
        return "{} type, {} {}".format(self.item_type, self.quantity, self.unity)
        
class Shopping_list(ISubject):
    
    def __init__(self):
        self.name = None
        self._dic = {}
        
        self.observer_list = []
    
    def attach(self, observer):
        self.observer_list.append(observer)
        
    def detach(self, observer):
        self.observer_list.remove(observer)
    
    def notify(self):
        for observer in self.observer_list:
            observer.update(self)

    def __setitem__(self, key, value):
        self._dic[key] = value
        self.notify()
    
    def __getitem__(self, key):
        return self._dic[key]
    
    def __delitem__(self, key):
        self._dic[key]
        self.notify()
        
    def __len__(self):
        return self._dic.__len__()
    
    def keys(self):
        return self._dic.keys()
        
    def values(self):
        return self._dic.values()
        
    def __repr__(self):
        return "product list: {}".format(self._dic)
    
    def encode(self):
        return str(self._dic).encode('utf-8')

   
   
   
   
   
   
    
# class controller(shopping_list):
    
#     def __init__(self, name, place, item_type):
#         shopping_list.__init__(self, name, place, item_type)
    
#     def __repr__(self):
#         return "\nShopping list name: {} \nEstablishment: {} \nItem's type: {} \n\nITEMS LIST: ".format(self.name, self.place, self.item_type, self._items_to_buy_dic)
    
#     def __getitem__ (self, item):
#         return self._items_to_buy_dic[item]
    
#     def __setitem__ (self, item, quantity):
#         '''In case i need to change the quantity of any item'''
#         self._items_to_buy_dic[item] = quantity 
    
#     def __delitem__ (self, item):
#         self._items_to_buy_dic[item]
        
#     def __len__ (self):
#         '''Give this number at the end of the list'''
#         return self._items_to_buy_dic.__len__()
    
    
# fruits_list = controller("Fruits shopping", "Casino", "fruits")

# # print(fruits_list)

# fruits_list["framboises"] = 2

# # print(len(fruits_list))


# # TODO 1.  



