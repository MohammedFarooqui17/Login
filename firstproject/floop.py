# for loop :A for loop is used for iterating over a sequence (iterate over a sequence of iterable objects)
# (that is either a list, a tuple, a dictionary, a set, or a string). 

list = [1,2,3,'sports',True,False]
for x in list :
    print(x)
    if x =='sport':
        break
  


for x in range(6):
    if x == 3:
        continue
    print(x)
    
    
mylist = [1,2,3,4,5,6]
for x in mylist:
    if x ==3:
        continue
    print(x)
    
for x in range(1,6,2):
    print(x)
    
    
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key,value in my_dict.items():
    print(key , value)
    
list = [1,2,3,4,5]
for x in list:
    print(x)
    
mytuple=(1,2,3,4,5)
for x in mytuple:
    print(x)
    
myset={1,2,3,4}
for x in myset:
    print(x)
    
#range:   
for i in range(10, 2, -2):
    print(i)   
for i in range( 2, 10, 2):
    print(i)
        
        
list = [1,2,]
list2 = [3,4]
for x in list:
    for i in list2:
        print(x ,i)
        
        
list =['green','red','yellow','blue']
for x in list:
    print(x)
    for i in x:
        print(i)
        
        
        
        
        
        
for i in range (2,5):
    for j in range(1,11):
        print(i,"*",j , '=', i*j)
        
        
    
        
n = 5 #int(input("enter the number:"))
for i in range(1, n + 1 ):
    print(i*' * ' )
    


star=5 #int(input("enter the number:"))
i=1
while i < star:
     print('* '*i)
     i+=1


user_input = int(input("enter number:"))
star = lambda n:''.join('* ' * n)
i = 1
while i<user_input:
    print(star(i))
    i += 1



user_input=9#int(input('enter the number:'))
star=lambda n:''.join('* '*n)
for i in range(1,user_input+1):
    print(star(i))


for i in range(4):
    for j in range(4):
       print("*  ",end='')
    print()
        


user_input = int(input("Enter Number :"))
Star = lambda n : ''.join('*'*n)
for i in range(1,1+user_input):
    print(star(i))





















