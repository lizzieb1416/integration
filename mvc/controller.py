import mvc.model as model

class Controller():
    
    def __init__(self, imodel):
        self._sl = imodel
        
    def add_product(self, name, item_type, quantity, unity):
        
        try:
            int(quantity)
        except ValueError:
            print("Quantity should be a integer")
            raise ValueError("Quantity should be a integer")
        else:    
            produit = model.Product()
            produit.name = name
            produit.item_type = item_type
            produit.quantity = quantity
            produit.unity = unity        
            self._sl[name] = produit
        
    def del_product(self, name):
        try:
            self._sl[name]
        except KeyError:
            print("This item does not exist in the shopping list")
            raise KeyError("This item does not exist in the shopping list")
        else:   
            del self._sl[name]
    
    def subscribe_to_model(self, observer): # Controller is not an observable but is a bridge to attach to the model
        self._sl.attach(observer)
    
    def unsubscribe_to_model(self, observer):
        self._sl.detach(observer)

#modif. arguments in list
#it is not necessary to add item_type, quantity or unity to add an item 



    