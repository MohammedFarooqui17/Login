"""# list ============= Sequencial type data =============
# used to store a collection of items.
list and its methods 
Definition and usage

* declearation
* add elements
* access elements 
* remove elements 
* update elements 
* extra methods"""

list = [1,2,'fruit','sports',True,3.2]
list[3]='footbal'
list.append(33)
list.pop()
print(list)

list=[1,3,2,4,8,7,6,9]
list[2]='cricket'
#list.insert(0,'Sports')
list1=[1,3,2,4,8,7,6,9]
list.remove(1)
list.extend(list1)
del list1
print(list1)
print(list)

list=[1,3,2,4,8,7,6,9]
del list
print(list)

list=[1,3,2,4,8,7,6,9]
list.clear()
print(list)



# List Comprehension
"""List comprehension offers 
a shorter syntax when you want to create a new list based on the values of an existing list."""

list=['jhon','bard','steve','michel','jackson']
list1=[]

for x in list:
    if 'e' in x:
        list1.append(x)
print(list1)


list = ['name', 'jack','william','stack','holland','hyden','clark']
list1 = []
for i in list :
    if 'a' in i:
        list1.append(i)
print(list1)
     
     
     
     
     
list = ['name', 'jack','william','stack','holland','hyden','clark']
newlist = []
for x in list:
     if 'a' in x:
         newlist.append(x)
print(newlist)
     
    
   
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     