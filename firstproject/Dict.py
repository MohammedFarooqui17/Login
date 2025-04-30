"""
# Dictionary ============= Mapping type data =============
dict and its methods 
Definition and usage

* declearation
* add elements
* access elements 
* remove elements 
* update elements 
* extra methods """


mydict = dict(name='jhon',age=90, designations='marketing')
print(mydict)


mydict={'name':'steve','country':'Australia' , 'position':'Batsman'}
#print(mydict)
print(mydict['name'])
print(mydict.get('country'))
print(mydict.keys())
print(mydict.values())

mydict={'name':'steve','country':'Australia' , 'position':'Batsman'}
mydict['name']='Brain'
mydict['country']='Westindies'
print(mydict)
print(mydict.items())#return each item in a dictionary, as tuples in a list.


mydict={'name':'steve','country':'Australia' , 'position':'Batsman'}
#mydict.update({'name':'LARA','country':'Westindies'})
mydict['position']='batsman'
mydict.pop('name')
mydict.popitem()# method removes the last inserted item
print(mydict)

mydict={'name':'steve','country':'Australia' , 'position':'Batsman'}
del mydict['position']
print(mydict)

mydict={'name':'steve','country':'Australia' , 'position':'Batsman'}
mydict.clear()#this will clear all the items which we have in the dictionary
print(mydict)

#Nested Dictionary
mydict={ 'player':{'name':'steve','country':'Australia' , 'position':'Batsman'},
         'player2':{'name':'jack','country':'England' , 'position':'Batsman'},
         'player3':{'name':'Anderson','country':'England' , 'position':'Bowler'}
         }
print(mydict)
print(mydict['player3']['name'])
print(mydict['player3'])
#-----------------------------------------------------------

