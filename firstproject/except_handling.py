# Exception Handling

num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

try:
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("divide by zero is not possible")
    
except NameError:
    print("variable name is wrong")
else:
    print("exceptions is not occurng")

finally:
    print("always execute")    

#--------------------------------------------------------
# how to print exception name and exceptions informations
# for this there are two ways
# 1 : using exceptions class object 
# 2 : using system module

# how to print exception name and exceptions informations
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

try:
    result=num1/num2
    print(result)
except ZeroDivisionError as var: # by using this we can print the exception informations
    print(var)
    
#1 : using exceptions class object   
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

try:
    result=num1/num2
    print(result)
except ZeroDivisionError as var: # by using this we can print the exception informations
    print(var.__class__) # this will call the class and all the exception name is nothing a class
    
    
# if we dont know which error will get then we write like this

num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

try:
    result=num1/num2
    print(result)
except Exception as var: # by using this we can print the exception informations
    print(var) 
    print(var.__class__)


# 2 : using system module

import sys


num1=int(input("enter number1:"))
num2=int(input("enter number2:"))

try:
    result=num1/num2
    print(result)
except :
    print(sys.exc_info()[0])#this will give class name of error like nameerror etc
    print(sys.exc_info()[1])# this will give information about errors
   

#-------------------------------------

# raise keyword (statement): is used for raising exception for perticular condition

try:
    age=int(input("enter your age:"))
    if age <0:
        raise ValueError
    print("your age is :",age)
    
except ValueError:
    print("valid age")
#---------------------------------
    
try:
    age=int(input("enter your age:"))
    if age <0:
        raise ValueError("invalid age")
    print("you age is :",age)
    
except ValueError as var:
    print(var)
    
    
#---------------------------------------------------------------

# user define exception
class FiveDivisionError(Exception):
    def __init__(self): 
        print("cannot divide by five")
    pass
    
try:
    n1=int(input("Enter First Number:"))
    n2=int(input("Enter Second Number:"))
    
    if n2==5:
        raise FiveDivisionError#("cannot divide by five")
    div=n1/n2
    print("division is : ",div)
except (FiveDivisionError,ZeroDivisionError) as var:
    print(var, end="")
    
    
    
    
import time   
class BalanceExceptionError(Exception):
    pass 
class AttemptExceptionError(Exception):

    pass
attempt=1
def withdraw():
    global attempt
    saved_pin=12345
    balance = 10000
    pin=int(input("Enter your pin"))
    if pin == saved_pin:
        try:
            amt=float(input("Enter amount withdraw:"))
            temp_bal= balance-amt
            if temp_bal<1000:
                raise BalanceExceptionError("insufficient balance")
            balance=balance-amt
            print("remained balance is :",balance)
        except Exception as obj:
            print(obj)
            
    else:
        ans=input("Do you want to continue again:(y/n):")
        if ans.lower()=='y':
            attempt+=1
            try: 
                if attempt==4:
                    raise AttemptExceptionError("Too manay attempt, your account is bloacked for an hour")
            except Exception as obj:
                    print(obj)
                    time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you")
            return
withdraw()
#-----------------------------------------------------------------

# with file


try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
#-------------------------------------------------------



#excepthook

import sys
def format_traceback(exc_type,exc_value,exc_traceback):
    print("somthing is wrong ")
    print(exc_type)
    print(exc_value)
    print(exc_traceback)
sys.excepthook=format_traceback
def add():
    print(10+'hel')
add()


#--------------------------------------------

#assert statement



def valid_age(age):
    assert (age>=20),"age can not be negative"
    print('your age is :',age)
valid_age(20)
valid_age(-90)

#------------------------------------------

# Multi-Threading : A thread is nothing but a flow of execution in a computer programm


#how to create thread:

# steps : 1) import thread class 2) create a func containing code exec parelly 
# 3) create object of thread/ new thread  4) start new thrad


# steps : 1) import thread class 
from threading import Thread

#2) create a func containing code exec parelly 
def display():
    for i in range(4):
        print("hello ")
#3) create object of thread/ new thread      
t1=Thread(target=display)# we give this new thread a task or work by using argument which is nothing bt target

#4)create start new thrad
t1.start()

#----------------------------------

# second way


def display(n,msg):
    for i in range(n):
        print(msg)
        
t1=Thread(target=display,args=(4,'Moahmmed'))
t2=Thread(target=display,kwargs={'n':4,'msg':'Mohammed'})
t1.start()# it will run in a seprate memory
    
#----------------------------------------

# how to create thread for methods 

from threading import Thread
class Examples:
    def display(self,n,msg):
        for i in range(n):
            print(msg)
        
t1=Thread(target=display,args=(4,'Moahmmed'))
t2=Thread(target=display,kwargs={'n':4,'msg':'Mohammed'})
t1.start()

for i in range(5):
    print("wellcome")
    
#-------------------------------------

class Examples:
    @classmethod  #@static we call class method and ststic by using class reference which is Exampls
    def display(self,n,msg):
        for i in range(n):
            print(msg)
        
t1=Thread(target=Examples,args=(4,'Moahmmed'))#static we call class method and static by using class ref which is Exampls
t2=Thread(target=Examples,kwargs={'n':4,'msg':'Mohammed'})
t1.start()#when this line execute python interpreter run a method and the name is run() it run thread parally

for i in range(5):
    print("wellcome")
    
#--------------------------------

# how to create thread by using extending thread class

from time import sleep
from threading import Thread

videos=['oops syslbus','sontructor','destructor','file handling']

class Myclass(Thread):
    def run(self):
        for i in videos:
            print(f"{i}")
            sleep(3)
            print(f"{i}")
        
t1=Myclass()
t1.start()

for i in range(4):
    sleep(0.4)
    print("checking copyrigts")


#--------------------------------------------

# how to configure threads names
# what are he threading identity numbers


def display():
    for i in range(3):
        print("xyz") 
        
def show():
    for i in range(7):
        print("abc") 
t1= Thread(target=display)
t2=Thread(target=show)
print(t1.name)
print(t2.name)# by using this we can see thread name also we can change this thread name

#also we can change this thread name
t1.name='Mohammed'


# also we cxan change main thread name for this whe should main thread object for that we use cuurect thread func 
#current_thread().name="xyx"

print(t1.ident)
print(t1.native_id) # this identity will assign when we start this thread

# to know the program id 
#import os 
#os.getpid() 

#--------------------------------------------------------------

# count of cuurent running threads

# Details oif all threads

# built in function:

# 1) is_alive(): check thread is running or not
# 2) main_thread(): retrurn main threads details : to get this import fisrt this function
# 3) active_count(): nmber of running thread :: to get this import fisrt this function
# 4)enumerates():  list of all running threads :to get this import fisrt this function
# 5)get_native_id : know netive id of thraeds




def display():
    for i in range(3):
        print("xyz") 
        
def show():
    for i in range(7):
        print("abc") 

t1= Thread(target=display)
print("befor",t1.is_alive())#will return  false because it is not in running
t1.start()
print("after",t1.is_alive())
#print(active_count()) import first this function
#print(enumerates()) import first this function
#print(get_native_id()) import first this function
t2=Thread(target=show)

# join method : 
# t1.join() means stop the execution of other untill the t1 executed


#----------------------------------------------

# Race Conditions:

"""
it is a bug genrated when you do multi-processing.it occurs because two or more threads 
tries to update the same variable and result  into unreliable ouput
concurrent accesses to shared resources can lead to race condition """


from threading import *

class Bus:
    def __init__(self,name, avail_seat) -> None:
        self.avail_seat= avail_seat
        
        pass
    def reserve(self,need_seat):
        print(self.avail_seat)
        if self.avail_seat>=need_seat:
            nm=current_thread().name
            print(f"{need_seat}  and {nm}" )
            self.avail_seat-=need_seat
        
        else:
            print("sorry")


b1=Bus("xyz",2)
t1=Thread(target=b1.reserve,args=(1,),name="abc")
t2=Thread(target=b1.reserve,args=(1,),name="axyz")
t1.start()
t2.start()

#---------------------------------------------------------

# how to avoid race condition: by using three ways 1)lock 2)unlock 3)semaphore and these are syncronizations tecq
# for locking we use aquire() syntax:lockobj.aquire([blocking=True],timeout=-1)
# by using release() method we unlock program or thread 

from threading import *
lock=Lock()
class Bus:
    def __init__(self,name, avail_seat,l) -> None:
        self.avail_seat= avail_seat
        self.l=l
        
        pass
    def reserve(self,need_seat):
        self.l.aquire()
        print(self.avail_seat)
        if self.avail_seat>=need_seat:
            nm=current_thread().name
            print(f"{need_seat}  and {nm}" )
            self.avail_seat-=need_seat
        
        else:
            print("sorry")
        self.l.release()


b1=Bus("xyz",2,lock)
t1=Thread(target=b1.reserve,args=(1,),name="abc")
t2=Thread(target=b1.reserve,args=(1,),name="axyz")
t1.start()
t2.start()

# Example 2 
# : how to avoid race condition by using lock 

from threading import *
from time import sleep

mylock=Lock()
def task(mylock,msg):
    mylock.aquire() # we can use default valuese in this method blocking(true,false) and timeout(-1,2) but avoid 
    for i in range(5):
        print(msg) 
    sleep(3)
    mylock.release()
    
t1=Thread(target=task,args=(mylock,'Mohammed'))
t2=Thread(target=task,args=(mylock,'Farooqui'))
t1.start()
t2.start()

#---------------------------------------------------------------------------


# r-lock 
# you cannot aquire multiple times using lock mechenism if we use then will get some errror or stuck code
# but in r-lock we can use mutiple time aquire method it is same as lock the difference is we create object
# by using RLock() class 
#------------------------------------------------------------

# semaphore :
# when we are using lock and r lock at a time only one thread is allowed to execute but sometimes 
# our requirement is to execute a perticular number of thread at a time which means we want to execute 3 
# thread at a time in this case we use semaphore 

# where we use : used to limit the access to the shared resources with limited capacity

# object create like s=Semaphor() this we can aquire many times but also release them equally 
# also we pass the numbrs inside the method that how many thread you want to run 


#-----------------------------------------------------------------------------------

# thread communications: three ways:
# 1) by creating event object
# 2) by creating condition object 
# 3) by using queue module


# FIRST-WAY
# by using first way: two thread only can communicate by the signal and the signal name is (flag) it can be true
# or it can be False  when it is true then other signal will communicate  
# for waiting we will use waite() method for perticular thread that thay can waite 
# sending the signal to other thread we use set() method this method will change th vlaue of flag which can
# be either true or false reset() when signal is false or true we can reset value by using this 
# Event object Methods:
# set(): set the internbal flag to true by default its value is false
# reset() : if we want to change value true to false 
# is_set(): it return boolean values use to check the condition : return true if internal flag is true
# wait([timeout]):  keep thread2 on waite till t1 can send any signal



# examples : tracffic signal

import threading
from time import sleep

e=threading.Event()

def light_switch():
    while True:
        print("light is green")
        e.set()
        sleep(5)
        print("ligh is red")
        e.clear()
        sleep(5)
        e.set()
        
def traffic_message():
    e.wait()
    while e.is_set():
        print("you can go")
        sleep(1)
        e.wait()
    
t1=threading.Thread(target=light_switch)
t2=threading.Thread(target=traffic_message)
t1.start()
t2.start()
#-------------------------------------------------------------------------


# 2) by creating condition object
# BY USING THIS  MULTPLE THREAD CAN COMMUNICATE LIKE THREAD1 WILL GIVE SIGNAL TO THE T2,3,4 ETC THEN THEY WILL EXECUTE
# USE TO COMMUNICATE WITH MULTIPLE THREADS
# EVENT-OBJECT: COMMUNICATIONS BTW TWO THREADS
#  CONDITION IS ALSO A CLASS OF THREADING MODULE WE CAN MAKE OBJECT LIKE CON=THREADING.CONDITION([LOCKOBJ])
#METHOODS
# WAITE(): USED TO BLOCK THE THREAD WAITE UNTILL SIGNAL FROM T1
# NOTIFY():USED ONLY WHEN WE COMMUNICATE FROM A SINGLE THREAD
# NOTIFY_ALL: USED TO COMMUNICATE FROM ALL THREAD
# THESE METHOD MUST ONLY BE CALLED WHEN THE CALLING THREAD HAS AQUIRED AND LOCK


#-----------------------------------------------------------------
 
# 3) by using queue module
# METHODS 
#  PUT(ITEMS, BLOCK=TRUE): USED TO INSERT ELEMENT INTO QUEUE
# GETS(): USED TO DELETE ELEMET FTROM QUEUE 
# BENEFITS : THREAD SAFE : NO RACE CONDITION WILL OCCURE
# IMPLEMENTS ALL REQUIRED LOCKING SEMENTIC

# ---------------------------------------------------

# DAEMON THREADS :

# NON DAEMONS THREAD(NON - SUPPORTIVE THREAD): EIDTOR , SHELL , TERMINAL THSESE ARE NON D
# PROGRAM WILL NOT TERMINATE UNTILL ALL NON - DAEMON THREADS GETS COMPLETED
# USE: FOR TASK SUCH AS MONITORING , BACKGROUND SERVICES , OR CLEANUP OPERATIONS


# DAEMON THREAD( SUPPORTIVE THREADS):  TEXT HIGHLIGHTING ,MEMORY MANAGEMENT DEMO T
# WHEN ALL THE NO DE THRED GETS TERMINATED AUTOMATICALLY DAEMON THRD ALSO GETS TERMINATED
# IT IS A THREAD WHICH RUNS CONTINOUSLY IN BACKGROUND AND RPOVIDE SUPPORT TO OTHER NON-DEM T
# PROGRAM WILL NOT TERMINATE UNTILL ALL NON - DAEMON THREADS GETS COMPLETED
# USE: FOR TASK SUCH AS MONITORING , BACKGROUND SERVICES , OR CLEANUP OPERATIONS
# NATURE CHANGE T1.DAEMON=TRUE (BUT YOU CANT CHNAG DEMN NATURE OF RUNNING THREAD)
# DAEMONS NATURE BY DEFAULT IT IS NON DAEMON


#--------------------------------------------------------

# TIMER OBJECTS AND BARRIER OBJECTS : MOSTLY USED FOR SYNCRONIZATIONS
#-------------------------------------------------------------

# two types of decorator 
#1: function based
#2: class based


# def deco(addition):
#     def inner():
#         result=addition()
#         num3=int(input("Enter Third Number:"))
#         result=result+num3
#         return result
#     return inner


# @deco
# def addition():
#     num1=int(input("Enter first number:"))
#     num2=int(input("Enter second number:"))
#     result=num1+num2
#     return result
# print(addition())

# print(type(addition))
# print(type(deco))






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
                                                                                                                                                                                                                                                                                                    

# two types of decorator 
#1: function based
#2: class based


class Decorator(object):#object is present bydefault if we dont send this then its fine
    def __init__(self,add) -> None:#this function came through the obj which we have made below
        self.function=add # this func is nothing but add() we assighn this with self.fuction variable
        
    
    def __call__(self, a,b):
        result=self.function(a,b) # original function (by default this will call add())
        return result**2
    
@Decorator
def add(a,b):
    return a+b
#obj=Decorator(add())
#print(obj(10,20)
print(add(2,4))

#obj=Decorator(add()) #this obj is not call able because call() is not prsent in the class of decorator
# so for that we will write call method which we have written above 
# add function is not present in decoerator class that y we send this 
# obje() if we call this obj then it will call call() like obj.__call() and whatever number we will  send
# inseide obj it will pass inside the __call__() for examlp:obj(10,10)  then obj.__call(a,b)
#print(obj(10,20))# if we want this obj act like a function then we will write call() method 
#
#print(callable(obj))# this will return false because __call__() are not present in Decorator class so for 
# this we will write __call__ method 



#original code
class Decorator(object):
    def __init__(self,add):
        self.function=add
        
    def __call__(self, a,b):
        result=self.function(a,b)
        return result**2
    
@Decorator
def add(a,b):
    return a+b        
        
print(add(2,4))




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

#------------------------------------------------------------


import pandas as pd

#
#1. Creating a DataFrame from a Dictionary
#You can create a DataFrame from a dictionary where the keys are column names
#and the values are lists or arrays representing the column data.

data={
    
    'name':['steve','jhon'],
    'age':[33,77],
    'country':['eng','usa'] 
}

result=pd.DataFrame(data)
print(result)


#2. Creating a DataFrame from a List of Dictionaries
#Each dictionary in the list represents a row in the DataFrame.

data=[
    {'name':'Mohammed','age':24,'country':'india'},
    {'name':'Ahmed','age':24,'country':'india'},
    
]
result=pd.DataFrame(data)
print(result)


#3. Creating a DataFrame from a List of Lists
#The outer list represents rows, and the inner lists represent the values in each row. 
#You can provide column names using the columns parameter.
import pandas as pd
data=[
    ['mohammed',24,'india'],
    ['steve',60,'eng']
]
col=['name','age','country']
result=pd.DataFrame(data, columns=col)
print(result)

#4. Creating a DataFrame from a List of Tuples
#Similar to lists, but using tuples for each row.
import pandas as pd
data=[
      ('mohammed',24,'india'),
    ('steve',60,'eng')
]
col=('name','age','country')
df=pd.DataFrame(data,columns=col)
#print(df)
# scol=df.name#extracting single column
# scol=df['name']#extracting single column
# mcol1=df[['name','age']]# extracting multiple column
# print(scol)

#srow=df.iloc[0]#extracting single rows
#srow1=df.loc[1]
mrows=df.loc[[0,1]]#extracting multiple rows
mrows1=df.iloc[0:2]#extracting multiple rows same we can do with iloc
#print(srow)
print(mrows)
print(mrows1)


#--------------------------------------------

#5. Creating a DataFrame from a List with a Multi-Index
#If you have hierarchical data, you can create a DataFrame with a multi-ind

import pandas as pd

# List of lists
data = [
    ['USA', 'California', 'Los Angeles', 1000],
    ['USA', 'California', 'San Francisco', 900],
    ['USA', 'New York', 'New York City', 1100],
    ['Canada', 'Ontario', 'Toronto', 800],
    ['Canada', 'Quebec', 'Montreal', 700]
]

# Creating the DataFrame
df = pd.DataFrame(data, columns=['Country', 'State', 'City', 'Population'])
df.set_index(['Country', 'State', 'City'], inplace=True)
print(df)


#--------------------------------------------------------------




























































































