from abstract_demo import *

obj=Scooty(2)
obj.start()
#-----------------------------------------------

# Accesss Modifier
#public: we can accees methods attribute from the outside the class
#protected : we can access within th calss or in derived calss
#private : we can access only inside the class 

#This is Public Acces Modifier example
class Student:
    def __init__(self,name) -> None:
        self.name=name
        pass
    def display(self):
        print(f'{self.name}')
obj=Student("Steve")
obj.display()
        

#protected : we can access within th calss or in derived calss
class Student:
    def __init__(self,name,rollnum) -> None:
        self.name=name
        self._rollnum= rollnum # using one underscore we make protected attribute
        pass
    def display(self):
        print(f'{self.name} {self._rollnum}')
        
        
class Branch(Student):
    pass
obj=Branch("Steve",33)
obj.display()
# print(obj.name)
# print(obj._rollnum)

#--------------------------------------

#private : we can access only inside the class 


class Student:
    def __init__(self,name,rollnum , age) -> None:
        self.name=name
        self._rollnum= rollnum # using double underscore we make private attribute
        self.__age=age
        pass
    def __display(self):
        print(f'{self.name} {self._rollnum} {self.__age}')
        
        
# class Branch(Student):
#     pass
# obj=Branch("Steve",33,24)
# obj.display()

s1=Student("Mohammed",17,24)
print(s1._Student__age)
s1._Student__display()

#----------------------------------------------------------


#Encapsulation:
