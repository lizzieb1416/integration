from __future__ import annotations

from abc import ABC, abstractmethod


class IObserver(ABC):
    
    @abstractmethod
    def update(self, subject: ISubject): # : subject:ISubject. i was having an error when running main
        pass
    
    @abstractmethod
    def update_error(self, error: Exception):
        pass

class ISubject(ABC):
    
    @abstractmethod
    def attach(self, observer: IObserver):
        pass
    
    @abstractmethod 
    def detach(self, observer: IObserver):
        pass
    
    @abstractmethod
    def notify(self):
        pass
    
    @abstractmethod
    def notify_error(self):
        pass
    
class IController(ABC):
    
    @abstractmethod
    def add_product(self, name, item_type, quantity, unity):
        pass
    
    @abstractmethod
    def del_product(self, name):
        pass
    
    @abstractmethod
    def subscribe_to_model(self, observer): # Controller is not an observable but is a bridge to attach to the model
        pass
    
    @abstractmethod
    def unsubscribe_to_model(self, observer):
        pass