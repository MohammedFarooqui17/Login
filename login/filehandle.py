# import pymysql

# def Dbconnection():
#     mydatabase=pymysql.connect(
#         host='Localhost',
#         user='root',
#         passwd='root',
#         database='mohammed'
#     )
    
#     pointer=mydatabase.cursor()
    
#     return pointer , mydatabase

# pointer,mydatabase=Dbconnection()

# # query="create database mohammed;"
# # query="create table emp(id int auto_increment primary key, fullname varchar(25),department varchar(15));"
# #query="insert into emp (fullname,department) values('hardy','Manager');"
# # name=input("enter name:")
# # department=input("enter depname:")
# # query=f"insert into emp(fullname,department) values('{name}','{department}');"
# query="DELETE from emp where id in(9,10);"
# # query="insert into emp (fullname,department) values('jordan','Account');"
# pointer.execute(query)
# mydatabase.commit()
# # mydatabase.rollback()
# # pointer.execute('commit;')
# # data=pointer.fetchall()
# # print(data)
# # pointer.close()
# # mydatabase.close()


# num1=int(input("enter number1:"))
# num2=int(input("enter number2:"))

# try:
#     result=num1/num
#     print(result)
# except Exception as var: # by using this we can print the exception informations
#     print(var)
#     print(var.__class__) 

# import sys
# num1=int(input("enter number1:"))
# num2=int(input("enter number2:"))

# try:
#     result=num1/num2
#     print(result1)
# except :
#     print(sys.exc_info()[0])#this will give class name of error like nameerror etc
#     print(sys.exc_info()[1])# this will give information about errors


# try:
#     age=int(input("enter your age:"))
#     if age <0:
#         raise ValueError("invalid age")
#     print("you age is :",age)
    
# except ValueError as var:
#     print(var)



# # user define exception
# class FiveDivisionError(Exception):
#     def __init__(self): 
#         print("cannot divide by five")
#     pass
    
# try:
#     n1=int(input("Enter First Number:"))
#     n2=int(input("Enter Second Number:"))
    
#     if n2==5:
#         raise FiveDivisionError#("cannot divide by five")
#     div=n1/n2
#     print("division is : ",div)
# except (FiveDivisionError,ZeroDivisionError) as var:
#     print(var, end="")
    
    
# import time   
# class BalanceExceptionError(Exception):
#     pass 
# class AttemptExceptionError(Exception):
#     pass
# attempt=1
# def withdraw():
#     global attempt
#     saved_pin=12345
#     balance = 10000
#     pin=int(input("Enter your pin"))
#     if pin == saved_pin:
#         try:
#             amt=float(input("Enter amount withdraw:"))
#             temp_bal= balance-amt
#             if temp_bal<1000:
#                 raise BalanceExceptionError("insufficient balance")
#             balance=balance-amt
#             print("remained balance is :",balance)
#         except Exception as obj:
#             print(obj)
            
#     else:
#         ans=input("Do you want to continue again:(y/n):")
#         if ans.lower()=='y':
#             attempt+=1
#             try: 
#                 if attempt==4:
#                     raise AttemptExceptionError("Too manay attempt, your account is bloacked for an hour")
#             except Exception as obj:
#                     print(obj)
#                     time.sleep(3600)
#             else:
#                 withdraw()
#         else:
#             print("Thank you")
#             return
# withdraw()

    

# #except-hook

# import sys
# def format_traceback(exc_type,exc_value,exc_traceback):
#     print("somthing is wrong ")
#     print(exc_type)
#     print(exc_value)
#     print(exc_traceback)
# sys.excepthook=format_traceback
# def add():
#     print(10+'hel')
# add()


# #assert-statement



# def valid_age(age):
#     assert (age>=20),"age can not be negative"
#     print('your age is :',age)
# valid_age(20)
# valid_age(-90)


#_------------------------------------------------


#how to create thread:

# steps : 1) import thread class 2) create a func containing code exec parelly 
# 3) create object of thread/ new thread  4) start new thrad


# # steps : 1) import thread class 
# from threading import Thread

# #2) create a func containing code exec parelly 
# def display():
#     for i in range(4):
#         print("hello ")
# #3) create object of thread/ new thread      
# t1=Thread(target=display)# we give this new thread a task or work by using argument which is nothing bt target

# #4)create start new thrad
# t1.start()

# #----------------------------------

# # second way

# def display(n,msg):
#     for i in range(n):
#         print(msg)
        
# t1=Thread(target=display,args=(4,'Moahmmed'))
# t2=Thread(target=display,kwargs={'n':4,'msg':'Mohammed'})
# t1.start()# it will run in a seprate memory
    
# #----------------------------------------

# # how to create thread for methods 

# class Examples:
#     def display(n,msg):
#         for i in range(n):
#             print(msg)
        
# t1=Thread(target=display,args=(4,'Moahmmed'))
# t2=Thread(target=display,kwargs={'n':4,'msg':'Mohammed'})
# t1.start()

# for i in range(5):
#     print("wellcome")
    
# #-------------------------------------
# class Examples:
#     @classmethod  #@static we call class method and static by using class reference which is Exampls
#     def display(self,n,msg):
#         for i in range(n):
#             print(msg)
        
# t1=Thread(target=t1.Examples,args=(4,'Moahmmed'))#static we call class method and ststic by usimng class reference which is Exampls
# t2=Thread(target=t2.Examples,kwargs={'n':4,'msg':'Mohammed'})
# t1.start()#when this line execute python interpreter run a method and the name is run() it run thread parally

# for i in range(5):
#     print("wellcome")
    
# #--------------------------------

# # how to create thread by using extending thread class

# from time import sleep
# from threading import Thread

# videos=['oops syslbus','sontructor','destructor','file handling']

# class Myclass(Thread):
#     def run(self):
#         for i in videos:
#             print(f"{i}")
#             sleep(3)
#             print(f"{i}")
        
# t1=Myclass()
# t1.start()

# for i in range(4):
#     sleep(0.4)
#     print("checking copyrigts")
# #--------------------------------------------

# # how to configure threads names
# # what are he threading identity numbers


# def display():
#     for i in range(3):
#         print("xyz") 
        
# def show():
#     for i in range(7):
#         print("abc") 
# t1= Thread(target=display)
# t2=Thread(target=show)
# print(t1.name)
# print(t2.name)# by using this we cxan see thread name also we can change this thread name

# #also we can change this thread name
# t1.name='Mohammed'


# # also we cxan change main thread name for this whe should main thread object for that we use cuurect thread func 
# #current_thread().name="xyx"

# print(t1.ident)
# print(t1.native_id) # this identity will assign when we start this thread

# # to know the program id 
# #import os 
# #os.getpid() 

#--------------------------------------------------------------

# count of current running threads

# Details of all threads

# built in function:

# 1) is_alive(): check thread is running or not
# 2) main_thread(): retrurn main threads details : to get this import fisrt this function
# 3) active_count(): nmber of running thread :: to get this import fisrt this function
# 4)enumerates():  list of all running threads :to get this import fisrt this function
# 5)get_native_id : know netive id of thraeds



# def display():
#     for i in range(3):
#         print("xyz") 
        
# def show():
#     for i in range(7):
#         print("abc") 

# t1= Thread(target=display)
# print("befor",t1.is_alive()) # will return  false because it is not in running
# t1.start()
# print("after",t1.is_alive())
# #print(active_count()) import first this function
# #print(enumerates()) import first this function
# #print(get_native_id()) import first this function
# t2=Thread(target=show)


#----------------------------------------------


def deco(addition):
    def inner():
        result=addition()
        num3=int(input("Enter Third Number:"))
        result=result+num3
        return result
    return inner


@deco
def addition():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    result=num1+num2
    return result
print(addition())

print(type(addition))
print(type(deco))






# how to apply multiple decorator on one function


# def deco1(getname):
#     def inner():
#         return getname().upper()
#     return inner

    
# def deco2(getname):
#     def inner():
#         return getname().split()
#     return inner


# @deco2
# @deco1
# def getname():
#     name=input("Eneter your name :")
#     sirname=input("Enter your sirname:")
#     fulname= name + " "+ sirname
#     return fulname
# print(getname())


# one decorator apply on multiple functions
# def deco(func):
#     def inner(*args):
#         for num in args [1:]:
#             if num==0:
#                 return "cannot divide  by zero"
#         return func(*args)
#     return inner

# @deco
# def div1(x,y):
#     return x/y
# @deco
# def div2(x,y,z):
#     return x/y/z

# print(div1(6,8))
# print(div2(7,8,6))

from typing import Any

# two types of decorator 
#1: function based
#2: class based

# class Decorator(object):#object is present bydefault if we dont send this then its fine
#     def __init__(self,func) -> None:
#         self.function=func # this func is nothis but add() we assighn this with self.fuction variable
#         pass 
    
#     def __call__(self, a,b) -> Any:
#         result=self.function(a,b) # original function (this will call add())
#         return result**2
#         pass
# @Decorator
# def add(a,b):
#     return a+b

# #obj=Decorator(add()) # add function is not present in decoerator calss that y we send this 
# #print(obj(10,20))# if we want this obj act like a function then we will write call() method 
# print(add(2,4))
# #print(callable(obj))# this will return false because __call__() are not present in Decorator class so for 
# # this we will write __call__ method 


class Decorator(object):
    def __init__(self,func):
        self.function=func
        
    def __call__(self,*args):
        try:
            if any([isinstance(i,str) for i in args]):
                raise TypeError("cannot pass string as argument")
            else:
                return self.function(*args)
        
        except Exception as obj:
            print(obj)
    
@Decorator
def add(*args):
    sum=0
    for num in args:
        sum=sum+num
    return sum
print(add(10,10,9))
print(add(10,'10',9))
    




# =====================================================================


# FILE HANDLING







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

# with open ("test2.txt","w") as file:
    
#     text= "Hello How are you"
#     file.write(text)
    
    
    
# with open("test.txt",'r') as file:
#     data=file.read()
#     print(data)
    
    
# with open("test.txt",'a') as file:
#     text="\nHello Python"
#     file.write(text) 
    
    
# with open("test2.txt","w+") as file:
#     text="Mohammed"
#     file.write(text)
    
#     file.seek(0)
#     data=file.read()
    
#     print(data)
#     file.close()

# with open("test2.txt",'r+') as file:
#     data=file.read()
#     print(data)
    
#     file.seek(0)
    
#     text="How are you"
#     file.write(text)
    
    
# with open("test2.txt",'a') as file :
#     text="\nMohammed here"
    
#     file.write(text)
    
    



# with open("file.txt",'w+') as file :
#     text="hello good morning"
#     file.write(text)
#     file.seek(0)
#     data=file.read()
#     print(data)
#     data1=file.tell()
#     print(data1)
#     pass
# #--------------------------------------------------
# with open("file.txt",'w+') as file:
#     text=" This is Mohammed"
#     file.write(text)
    
#     data=file.tell()
#     print(data)
    
#     file.seek(0)
    
#     data1=file.read()
#     print(data1)
    
#     data=file.tell()
#     print(data)
    
#     file.close()
    
# age=input("enter your name") 
# with open("data.txt",'w') as file :
#     file.write(age)
#     file.close()
    
# with open("data.txt",'r') as file:
#     data=file.read()
#     print(data)
    
# with open("data.txt",mode='r+', buffering=10, encoding="utf-8") as file:
#     data=file.read()
#     print(data)
    
#     text="\nand the new attributes is buffering for me"
#     file.write(text)
    
#     file.close()#this will delete the object from the memory if we wil not close 
    # then garbage collector automatically will destroy file object and close file automatically 
    #  but this is not good because in garbage collect it may be there is unexpected opeartion and if there 
    # will be than  more chances our data can be corrupt and memory will waste
    
    
   # file this is nothing but a class which return the object of class


# to check wheather file is exist o r not will return if exit else false
# import os
# data=os.path.isfile("mohd.txt")
# print(data) 

# # copy content one filr to another

# with open("data.txt",'r') as file1:
#     with open ("test2.txt",'w') as file2:
#         data=file1.readlines()
#         for line in data:
#             file2.write(line)


# Rnaming Multiple file name

# import os 
# path=input("enter your path")
# path=path.replace('\\','/')
# print(path)
# print(os.listdir(path))


# def main():
#     i=1
    



# with open("data.txt","w+") as file:
#     text="Mohammed here "
#     file.write(text)
    
#     data1=file.truncate(14)
#     print(data1)
    
#     data=file.read()
#     print(data)
    
    
    

















































































