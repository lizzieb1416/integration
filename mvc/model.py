from interface.ISubject import ISubject

class Product():
    
    def __init__(self, ):
        self.name = None
        self.item_type = None
        self.quantity = None
        self.unity = None
        
    def __repr__(self):
        return "{} {} {}".format(self.quantity, self.item_type,  self.unity)
        
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
    
    def items(self):
        return self._dic.items()
        
    def __repr__(self):
        return "{}".format(self._dic)
    
    def __getstate__(self):
        '''To pickle'''
        return (self.name, self._dic)
    
    def __setstate__(self, attribut_tuple):
        '''To unpickle'''
        self.name = attribut_tuple[0]
        self._dic = attribut_tuple[1]


   