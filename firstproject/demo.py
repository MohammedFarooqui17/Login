# Encapsulations and Access Modifier with inheritance
class Demo:
    def __init__(self,name,age,salary) -> None:
        self.__name=name    #Private
        self._age=age       #protected
        self.salary=salary  #public
        pass   
        
class Test(Demo):
    def __init__(self, name, age, salary,designations) -> None:
        super().__init__(name, age, salary)
        self.designation=designations   
        
    def display(self):
        print(f"The name of Emplyee is: \n  and his age is: {self._age}  \n salary is : {self.salary} \n Designation is : {self.designation} ")
             
obj=Test("Brad",24,3500000,"Manager")
# print(obj.__name)
# print(obj._age)
# print(obj.salary)
obj.display()

#--------------------------------------------------------------

class Demo:
    def __init__(self,name,age,salary) -> None:
        self.__name=name    #Private
        self._age=age       #protected
        self.salary=salary  #public
        pass   
        
class Test(Demo):
    def __init__(self, name, age, salary,designations) -> None:
        super().__init__(name, age, salary)
        self.designation=designations   
        
    def display(self):
        print(f"The name of Emplyee is: \n  and his age is: {self._age}  \n salary is : {self.salary} \n Designation is : {self.designation} ")
             
obj=Test("Brad",24,3500000,"Manager")
# print(obj.__name)
# print(obj._age)
# print(obj.salary)
obj.display()

#----------------------------------------------

# Duck Typing

class EmailNotification:
    def __init__(self,email_address) -> None:
        self.email_address = email_address
        
    def send(self,message):
        print(f"Sending Email to {self.email_address} : {message}")
        pass

class SMSNotification:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"Sending SMS to {self.phone_number}: {message}")

class PushNotification:
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"Sending push notification to device {self.device_id}: {message}")
        
def notify(notification_system, message):
    notification_system.send(message)


email = EmailNotification("user@example.com")
sms = SMSNotification("+1234567890")
push = PushNotification("device123")
notify(email, "Hello via Email!")
notify(sms, "Hello via SMS!")
notify(push, "Hello via Push Notification!")
#----------------------------------------------------------------------------------------------

#  Method Overloading

class Rectangle:
    def __init__(self, width=None, height=None):
        if width is not None and height is not None:
            self.width = width
            self.height = height
        elif width is not None:
            self.width = width
            self.height = width
        else:
            raise ValueError("Invalid arguments. Must provide at least one dimension.")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


rect1 = Rectangle(10, 20)
rect2 = Rectangle(15) 

print(rect1)  
print(f"Area: {rect1.area()}, Perimeter: {rect1.perimeter()}") 

print(rect2) 
print(f"Area: {rect2.area()}, Perimeter: {rect2.perimeter()}")  
#------------------------------------------------------------

class Rectangle :
    
    def __init__(self,  width=None , height=None) -> None:
        
        if width is not None and height is not None:
            self.width=width
            self.height= height
            
        elif width is not None:
            self.width=width
            self.width=height
            
        else:
            print("Please provide correct input")
            
        pass
    
    def area(self):
        return self.width * self.height
    
    def perameter(self):
        return 2*(self.width +self.height)
    
    def __str__(self) -> str:
        print(f"width{self.width} \n height{self.height}")
        
rect=Rectangle(22,23)
print(f'{rect.area()}  {rect.perameter()}')


#------------------------------------------------------------------


# Abstractions 

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
            


print()
savings = SavingsAccount("S12345", 1000)
print(savings.balance)
savings.deposit(200)
savings.withdraw(150)
print(f"Savings Account Balance: {savings.get_balance()}")

checking = CheckingAccount("C12345", 500)
checking.deposit(300)
checking.withdraw(100)
print(f"Checking Account Balance: {checking.get_balance()}")

#---------------------------------------------------------------------------------------------------

"""A decorator is a function that takes another function and extends the behavior
of the latter function without explicitly modifying it.
Python allows "nested" functions ie (a function within another function)"""


""" when to use: You'll use a decorator when you need to change the behavior
of a function without modifying the function itself."""


def custom_decorator(func):
    
    def inner_func(a,b):
        if b > a :
            a,b=b,a
        return func(a,b)
    
    return inner_func
    
@custom_decorator
def division(a,b):
    return a/b

x1=division(5,2)
x2=division(2,5)

print(x1)
print(x2)


#-------------------------------------------------------------------------------------


a=int(input("enter your number"))
print(a)








































