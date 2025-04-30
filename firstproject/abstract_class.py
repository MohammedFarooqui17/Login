from abc import ABC , abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.noof_tyers=n
        
    @abstractmethod   
    def start(self):
        pass
    
    def display(self):
        print("calling vehicle class")
