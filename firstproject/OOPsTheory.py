#what is class varaivles 
""" class variable is a variable that is shared among all instances of a class.
It is defined within the class but outside any instance methods. 
Class variables are often used for attributes and methods that are common to all instances of a class.

Class Variables:

Shared among all instances.
Defined at the class level.
Accessed using the class name or instances.
"""

#what is static variables
""""static variables" usually refers to class variables. 
Class variables, also known as static variables in some other programming languages,
are variables that are shared among all instances of a class. They are defined within a class 
but outside of any instance methods. 
These variables are not tied to any particular instance of the class
and maintain a single shared value across all instances."""


#what is class methods
"""
"""

class Person:
    
    increment_salary=1.5
    
    def __init__(self,name,age,salary,designation) -> None:#constructor with parameter
        self.name=name
        self.age=age
        self.salary=salary
        self.designation= designation
    

    def display_info(self):
        print(f'{self.name} {self.age} {self.designation}  {self.salary*Person.increment_salary}')
        
    @classmethod    
    def chech_cls(cls , newinc_salary):
        cls.increment_salary=newinc_salary
        return Person.increment_salary 
    
    # we use this when we dont need to the class instance or their variables or 
    # we can say we want to perform somthing independently or we can call it by using
    # class name or by intace name also
    @staticmethod  
    def sta_M():
        return Person.increment_salary
    
    
emp1=Person('steve',28,15000,'Manager')
#emp1.display_info()
print(emp1.increment_salary)   
emp1.chech_cls(3)
emp1.display_info()
# print(emp1.sta_M(3,9))
print(emp1.sta_M())



#satatic Methods
"""Bound to the Class: Static methods are associated with the class itself, 
not with any particular instance of the class.
Access Class Variables: Static methods can access class variables but not instance variables.
No Access to self or cls: Static methods do not take self or cls as their first parameter.
They operate independently of instances and the class itself."""

    
#Explicit Default Constructor:
class person:
    def __init__(self):#constructor without parameter
        self.name='Mohammed'
        self.age=24
obj=person()
print(obj.name)

#----------------------------------------------------------------------------
# Inheritance


class parent:
    def __init__(self,name,age,) -> None:
        self.name=name
        self.age=age
        pass    
    def display(self):
        print(f'{self.name} {self.age}')
        
# obj=parent("jordan",50)
# obj.display()

class son(parent):
    def __init__(self, name, age,profession,salary) -> None:
        super().__init__(name, age)
        self.profession=profession
        self.salary= salary
    def display2(self):
        print(f'{self.name} {self.age} {self.profession} {self.salary}')
        
obj2=son('Michal',24,'Artist',400000)
obj2.display2()




#Multiple Inheritance 


class Person1:
    def mathod1(self):
        print("This is parent 1")
class Person2(Person1):
    def method2(self):
        print("This is parent 2")
class child(Person1,Person2):
    def mathod3(self):
        print("This is parent 1")
obj=child()
obj.mathod1()
obj.method2()
obj.mathod3()
    
  

  
# PLOYMORPHISM :method name same but with different behaviour 
    
# same name wih different parameters is called overloading
class person:
    def myfunc(self,a):
        print(a)
obj=person()
obj.myfunc(1,2)#this will give errors because we havent define two varaible in func so according to def not 
obj.myfunc("hello")


#  same methods name with different classe name overriding
class person:
    def myfunc(self):
        print("Hello")
class friend(person):
    def myfunc(self):
     super().myfunc()
     print("how r u")
obj=friend()
obj.myfunc()


# duck Typing
"""
Duck typing is a concept in dynamic programming languages like Python, 
where the type or class of an object is less important than the methods
it defines or the way it behaves. The name comes from the saying, 
"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck." 
In programming, this means that if an object implements the necessary methods or behavior, 
it can be used in place of another object, regardless of its class"""

"""Duck typing allows objects of different classes to be used interchangeably 
if they implement the same methods.
This form of polymorphism doesn't rely on a common base class, 
enabling more flexible and decoupled designs."""

class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swim!")

class Person:
    def quack(self):
        print("I can imitate a duck by saying Quack!")

    def swim(self):
        print("I can swim too!")

def make_it_quack_and_swim(duck_like):
    duck_like.quack()
    duck_like.swim()
    
# obj=Duck()
# obj.quack()
# obj.swim()

# obj1=Person()
# obj.quack()
# obj.swim()
make_it_quack_and_swim(Duck())
make_it_quack_and_swim(Person())

#----------------------------------------

#oprator overloading : operator perform beyond its predefiend capability

class Complexnumber:
    def __init__(self , num1,num2) -> None:
        self.num1=num1
        self.num2=num2
        pass
    def __add__(self,other):
        return f"{self.num1+other.num1}+{self.num2+other.num2}i"
        #return str(self.num1+other.num2)+ "+" + str(self.num2+other.num2) + "i"
c1=Complexnumber(1,2)
c2=Complexnumber(4,5)
print(c1+c2)


#--------------------------------------------------

# Method overloading: same method name with the different parameter is called overloading
#python does not suuport method overloadinbg , but we can achive by using some other ways  
# by using default parameter and args and kwargs
# it is compile time polymorphism
# it occures in the same calsss

class Demo:
    
    def add(x,y):
        return x+y
    
    def add(x,y,z):
        return x+y+z
obj=Demo()
print(obj.add(2,3))
print(obj.add(2,3,5))


# in the above program we defined same method name which is add() but when we create and perform any 
#operations  out of all the method which we have defined it considered only the latest one just like the 
# above code they considered only the second one add Fiunction so when we run the program will get error 
# so for this we can achive this method overloading by using the default parameter or args just like this 



class Demo:
    def add(self ,x,y,z=0):
        return x+y+z
    # def add(self,x,y,z):
    #     return x+y+z
   
obj=Demo()
print(obj.add(2,3))
print(obj.add(2,3,5))

#-----------------------------------------------------------------------------------------------------

#Method Overrriding 
#same method with same parameter but with different locations is called method overriding
#it is runtime polymorphism
# it occure in different classes
#example


class Father:
    def sleep(self):
        print("Thry sleep 10 to 5 AM")

    def eat(self):
        print("Eating")
class Son(Father):
    def sleep(self):
        print("I sleep 2 to 10 AM")
        super().sleep()
son1=Son()
son1.sleep()

#-----------------------------------------------


# Abstractions : it is a process of identifying  which features are to be
# hidden and which one to be shown to the user is called abstractions
# we can achive abstraction by using abc a(abstract base class) module 
#An abstract method is a method that has a declaration but does not have an implementation.


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance
    
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to savings account {self.account_number}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from savings account {self.account_number}. New balance is {self.balance}")
        else:
            print("Insufficient funds")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to checking account {self.account_number}. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from checking account {self.account_number}. New balance is {self.balance}")
        else:
            print("Insufficient funds")
            



savings = SavingsAccount("S12345", 1000)
savings.deposit(200)
savings.withdraw(150)
print(f"Savings Account Balance: {savings.get_balance()}")

checking = CheckingAccount("C12345", 500)
checking.deposit(300)
checking.withdraw(100)
print(f"Checking Account Balance: {checking.get_balance()}")

#-----------------------------------------------------------------------------------------------


"""
Encapsulation is the practice of bundling data and methods within a single unit, like a class, 
and controlling their access, whereas abstraction is about hiding complex implementation details
and exposing only the essential functionalities"""


"""hiding the complex implementation details of a system and exposing only
the essential features and functionalities.
It allows programmers to focus on what an object does rather than how it does it."""

#---------------------------------------------------------------------------
from abc import ABC , abstractmethod
class Vehicle(ABC):
    def __init__(self,n):
        self.noof_tyers=n
        
    @abstractmethod   
    def start(self):
        pass
    
class Scooty:
    def __init__(self):
        self.noof_tyers=2
    def start(self):
        print("start with self")

class Car:
    def __init__(self):
        self.noof_tyers=4
    def start(self):
        print("start with self")
        
class Bike:
    def __init__(self):
        self.noof_tyers=2
    def start(self):
        print("start with Kick")

#----------------------------------------------


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
# we can access private varaible by using public method name mingly and private method


class Student:
    def __init__(self,name,rollnum , age) -> None:
        self.name=name
        self._rollnum= rollnum # using double underscore we make private attribute
        self.__age=age
        pass
    
    def disp(self):
        print(f'{self.name}  {self.__age}')
        
    def __display(self):
        print(f'{self.name} {self._rollnum} {self.__age}')
        
        
# class Branch(Student):
#     pass
# obj=Branch("Steve",33,24)
# obj.display()

s1=Student("Mohammed",17,24)
print(s1._Student__age)
s1._Student__display()#this is name mingly
s1.disp()#this is is public method we can also access private attribute by using this

#----------------------------------------------------------


#Encapsulation: Wrapping or bundled somthing in a single unit is called Encapsulations 
# it is like a sheild which protect our data from outside the world
# we hide the data by using access modifier
# the best way to access private things by using the getter and setter methods 



class Student:
    def __init__(self,name,rollnum , age) -> None:
        self.name=name
        self._rollnum= rollnum # using single underscore we make protected attribute
        self.__age=age  # using double underscore we make private attribute
        pass
    
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age<30:
            print(" Inavlid age is given")
        else:
            self.__age= age
    
    def disp(self):
        print(f'{self.name}  {self.__age}')
        
    def __display(self):
        print(f'{self.name} {self._rollnum} {self.__age}')
        
        
class Branch(Student):
    def show(self):
        print({self.__age})
    pass
obj=Branch("Steve",33,24)
obj.disp()

s1=Student("Mohammed",17,24)
print(s1.get_age())
s1.set_age(25)
print(s1.get_age)
# print(s1._Student__age)
# s1._Student__display()#this is name mingly
# s1.disp()#this is is public method we can also access private attribute by using this

#-----------------------------------------------------------------------------

# Multiple Inhertance

# Single Inheritance --> one child inherite from one parent class single inheritance
# Multiple Inheritance--> one child class inherit more than one parent class
# Multilevel Inheritance
# Hierarchial inheritance
# Hybrid Inheritance

#-------------------------------------------------------------------------------------

# Multiple Inheritance--> one child class inherit more than one parent class

#{this will call or inherit their own work method so for this if we want to inherit same method which
#are present in all classes we will access like this like the below one becuse if same methods are present
# in each class they follow MRO mmethod resolve order which is nothing but it check first in his own class
# after that they check according to inheritated classes like here we inherited human and male so after
# checking ther own one will check human first and than male because of mro}
class Human:
    def eat(self):
        print("they eat")
    def sleep(self):
        print("they sleep")
class Male:
    def work(self):
        print("They work")
    def lift(self):
        print("They can lift")
class Son(Human,Male):
    def play(self):
        print("they can play")
    def work(self):
        print("they can work")
obj=Son()
obj.work()#this will call or inherit their own work method so for this if we want to inherit same method which
#are present in all classes we will access like this like the below one becuse if same methods are present
# in each class they follow MRO mmethod resolve order which is nothing but it check first in his own class
# after that they check according to inheritated classes like here we inherited human and male so after
# checking ther own one will check human first and than male because of mro
Male.work(obj)#



#example with constructor

class Parent1:
    def __init__(self, name):
        self.name = name
        print(f"Parent1 initialized with name: {self.name}")

    def method1(self):
        print("Method 1 from Parent1")

class Parent2:
    def __init__(self, age):
        self.age = age
        print(f"Parent2 initialized with age: {self.age}")

    def method2(self):
        print("Method 2 from Parent2")

class Child(Parent1, Parent2):
    def __init__(self, name, age):
        Parent1.__init__(self, name) 
        Parent2.__init__(self, age)  
        print(f"Child initialized with name: {self.name} and age: {self.age}")

    def method3(self):
        print("Method 3 from Child")

child = Child("Alice", 30)
child.method1() 
child.method2()  
child.method3()  


#-----------------------------------------------------------------------------


# Multilevel Inheritance :

class parent1:
    def eat(self):
        print("they eat")
        
class parent2(parent1):
    def sleep(self):
        print("they sleep")
class boy(parent2):
    def play(self):
        print("they play")
obj=boy()
obj.eat()
obj.sleep()
obj.play()
#--------------------------------------------------


# Hierarchial Inheritance


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def info(self):
        print(f"I am a {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Woof"

    def info(self):
        super().info()
        print(f"I am a {self.breed} breed")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        return "Meow"

    def info(self):
        super().info()
        print(f"I have a {self.color} color")

dog = Dog("Dog", "Golden Retriever")
cat = Cat("Cat", "Black")

dog.info()
print(f"My sound is: {dog.sound()}")
print()
cat.info()
print(f"My sound is: {cat.sound()}")
 
    

#-------------------------------------------------------------------------

# return keyword values pass to in another function 

def func(x):
    return x+1
def func2(x,y):
    return x+y, x-y
output=func2(9,7)
final_op=func(output)
print(final_op)
#--------------------------------------------------------------


# File handling 

# for text

file=open('file.txt','w+')
file.write("python practicing here ")
print(file.tell())# to check where is my pointer
file.seek(0)# to set our pointer
data=file.read()
print(data)
file.close()


# for binary(images)

file=open("images.jpg",'rb')
file1=open('images1.jpg','wb')
for i in file:
    file1.write(i)
    

# Begginers Methods 

# file = open("example.txt" , "r")

# # data = file.read()  # return all data in a string type

# # data = file.readline()  # return first line of the file

# data = file.readlines()  # return list object each element of the list is file data 

# print(data)

# file.close()


# with open("example.txt" , "r") as file:
    
#     data = file.readlines()
    
# print(data)




# with open("example1.txt" , "w") as file:
    
#     text = "i am file what about you."
    
#     file.write(text)
    


# with open("example2.txt" , "a") as file:
    
#     # text = "Hello how are you"
#     text = "\ni am fine what about you"
    
#     file.write(text)
    
    

# r+ (Read + write )


# with open("example.txt" , 'r+') as file:
    
#     # read
#     data = file.read()
    
#     print(data)
    
#     # Set cursor position 
#     file.seek(3)
    
#     # write 
#     text = "python"
#     file.write(text)
    
    
# with open('example3.txt' , "w+") as file:
    
#     # write
#     text = "hello one point one"
#     file.write(text)
        
#     # set position
#     file.seek(1)
    
#     # read
#     data = file.read()
#     print(data)

#------------------------------------------------------------------
































         







































 


















    
    
    
    
    
    
    