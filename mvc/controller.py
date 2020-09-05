import mvc.model as model

class Controller():
    
    def __init__(self, imodel):
        self._sl = imodel
        
    def add_product(self, name, item_type, quantity, unity):
        
        try:
            int(quantity)
        except ValueError:
            print("Quantity should be a integer")
            raise ValueError
        else:    
            produit = model.Product()
            produit.name = name
            produit.item_type = item_type
            produit.quantity = quantity
            produit.unity = unity        
            self._sl[name] = produit
        
    def del_product(self):
        pass
    
    

#modif. arguments in list
#it is not necessary to add item_type, quantity or unity to add an item 



    