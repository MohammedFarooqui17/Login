# idealy while loop used for complex conditions 
#break : used for that our code should be finished base on given condition
#continue: used when we want to skip any perticular iterations

i=0
while (i<3):
    print(i)
    i=i+1
    

i = 6
while i < 0 :
    print(i)
    i=i-1
    
i = 6
while i > 0 :
    print(i)
    i=i-1
else:
    print('done')
    
i = 2
while i < 5:
    j = 1
    while j < 11:
        print(i, "*", j, '=', i * j)
        j += 1
    i += 1
    
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

i=0
while i<6:
    i=i+1
    if i==3:
        continue
    print(i)

    
# Nested while loop    
x = [1, 2]
y = [4, 5]
i = 0
while i < len(x) :
  j = 0
  while j < len(y) :
    print(x[i] , y[j])
    j = j + 1
  i = i + 1
  
  
  
#infinite:
  '''An infinite loop in Python is a loop that never terminates 
  unless an external intervention occurs (like manually stopping the 
  program or a break statement within the loop). This can be useful in various scenarios,
  such as continuously checking for a certain condition,
  running a server, or continuously waiting for user input'''
  
counter = 0
while True:
    print(counter)
    counter += 1
    
    
i = 1
star=5
while i <=star:
    print('*'*i)
    i=i+1

for i in range (2,5):
    for j in range(1,11):
        print(i,"*",j , '=', i*j)   
        
        
        
list =['Mohammed','Ahmed','Farooqui']
i=0
while i < len(list):
    print(list[i])
    i+=1

dict={'name':'styris','lname ':'bernard','country':'newzeland','profession':'Rugby'}
keys=list(dict.keys())
index=0
while index < len(keys):
    key=keys[index]
    values=dict[key]
    print(key,values)
    index+=1


list1=[1,2,3,4,5]
list2=['Styris','steve','james','obrain','allen']
i=0
while i < len(list1):
    j=0
    while j < len(list2):
        print(list1[i] ,list2[j])
        j+=1
    i+=1 
    
    
for i in range(2,11):
    for j in range(1,11):
        print(i,'*',j, '=' , i*j)


i=2
while i < 11:
    j=1
    while j < 11:
        print(i,'*',j , '=' ,i*j)
        j+=1
    i+=1
    # if i==3:
    #     break
    
    
dict={'name':'styris','lname ':'bernard','country':'newzeland','profession':'Rugby'}
for keys, values in dict.items():
    print(keys,values)
    # if keys=='country':
    #     break
    

   
    
dict = {'name':'xyz','designation':'uk'}
keys=list(dict.keys())
index=0
while index < len(keys):
    key=keys[index]
    value=dict[key]
    print(key,value)
    index+=1
    
list=[1,2,3,'Mohammed','xyz']
i=0
while i < len(list):
    print(list(i))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    i+=1

    
class Person:#it is nothing but a blueprint which means a templates or format
    def __init__(self,fname,lname,age,):#self is nothing but a refence of intance or object
        self.fname=fname
        self.lname=lname
        self.age=age
        pass
    def myfunc(self):
        print(f'{self.fname}  {self.lname} {self.age}')
        
obj=Person('Mohammed','Farooqui',24)
obj.myfunc()