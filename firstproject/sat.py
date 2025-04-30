""" # Set ============= set type data =============
set and its methods 
Definition and usage

* declearation
* add elements
* access elements 
* remove elements 
* update elements 
* extra meth

useful for tasks that involve membership testing, removing duplicates, 
and performing mathematical set operations like union, intersection, and difference"""



myset={7,9,1,2,3,True,0,False}
print(myset)

#ACCesing set
myset={7,9,1,2,3,True,0,False}
print(7 in myset)
print(11 not in myset)
for i in myset:
    print(i)
    
#add : use when we want to add single item
# [for multiple use====> update()]   
myset={7,9,1,2,3,True,0,False}
myset.add(90)
print(myset)

myset={7,9,1,2,3,True,0,False}
myset1={7,9,1,2,3,True,0,False,88,77,66,44}
print(myset.intersection(myset1))#return coomon 
print(myset.union(myset1))#return all except duplicate
myset.update(myset1)
print(myset)

#remove
myset={7,9,1,2,3,True,0,False}
myset.remove(9)#remove this item
myset.discard(7)#remove this item
myset.pop()#remove random item
print(myset)
myset.clear()#clears all item in which we have in the set 


