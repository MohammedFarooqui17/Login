"""# Tuple ============= Sequencial type data =============
Tuple and its methods 
Definition and usage

* declearation
* extra methods"""


mytuple = ('apple',)
print(type(mytuple))


tuple = ('jack','fraser',1,1,2,True,3.2)
print(tuple[1:4])

tuple1= ('jack','fraser',1,1,2,True,3.2)
x = list(tuple1)
x[1]='Mack-Fraser'
tuple1=tuple(x)
print(tuple1)



mytuple = ('Australia','newzeland','england','swierland')
mylist=list(mytuple)
mylist[3]='Africa'
mytuple=tuple(mylist)
print(mytuple)



#Unpacking
mytuple = ('Australia','newzeland','england','swierland')
(country1,country2,*country)=mytuple
print(mytuple.count('newzeland'))
print(mytuple.index('newzeland'))
print(*country)




mytuple = (1,2,3,4,5)
# (apple,banana,*orange)=mytuple
# print(orange)
mylist = list(mytuple)
mylist[0]='Mohammed'
mytuple=tuple(mylist)
print(mytuple)