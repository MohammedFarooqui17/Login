"""(1)A programming language is a set of instructions written by the programmers to deliver
the instructions to the computer to perform and accomplish a task"""

#(2) Keywords in Python are reserved words that have special meanings and purposes within the language.
#They form the basic syntax and structure of Python programs"""
#example:del , import , if , else , elif , try , catch , except , continue , break , as , assert , pass , return , etc......

#3 - variable , valid declearation  
# should start from chararter or alpha numeric a-z A-Z or 1-9
# cannot use resrverd words while we declaring variables
#example 
a = 9 
A = 9
__num11 = 55 
#camel case varaible 
myVariableName = "John"
#Pascal Case
MyVariableName = "name"
#Snake Case
my_variable_name = 9999


 # 4:what is data in programming : it is nohing but the information about somthing anf it can be many types like it can
 # string , integer , float etc 
 
 # 5 :basic data types ( with practical Operations )
 
a = int(16) 
b = str('name')
c = float(9.1)
d = True 

a= 9
b = 9.000
c = 'name' 
list=[1,2,3,4]
xyz = (1,2,2)
dict={1,2,3}
dit={"one":1}
a=True
print(type(a))


""" 
6 - what is Operators ( with practical Examples )
 types of operators
 1 - Arethmetic Operators
 2 - Relational & Comparision Operators
 3 - Logical & Bitwise Operator
 4 - membership Operator
 6 - Identity Operators"""
 
 # Operators are used to perform operations on variables and values.
 
 # 1 :  1 - Arethmetic Operators
 
x = 10
y = 7
print(x+y) #addition
print(x-y)#substractions
print(x*y)#multiplications
print(x/y)#division
print(x%y)#modules
print(x**y)#exponention
print(x//y)#floor

#Python Assignment Operators

x=5
x+=5 
x-=6
x**=3
x/=6

x=2
y=7
print(x**y)
# Python Comparison Operators

x==y
y!=y
x>y
x<y
x>=y
x<=y


# Python Logical Operators
x = 5
print(x > 3 and x > 10)#False

x = 7
print(x==7 or x!=7)#True
print(x!=7 or x>10)#False

x= 2
print(x==2)#False
print(x!=2)

# Python Identity Operators
x=[1,2,3,4]
y=[1,2,3]
print(x is y)
print(x is not y)

#Python Membership Operators
x=['apple','banana']
print('banana' in x)
print('apple' not in x )