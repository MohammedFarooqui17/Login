from abstract_class import Vehicle


class Scooty(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("start with self")

class Car(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("start with self")
        
class Bike(Vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("start with Kick")