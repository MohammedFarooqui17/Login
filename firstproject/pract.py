str = """
AI technology is widely used throughout industry, government, and science.
Some high-profile applications include advanced web search engines (e.g., Google Search); 
recommendation systems (used by YouTube, Amazon, and Netflix); interacting via human speech 
(e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo);
generative and creative tools (e.g., ChatGPT and AI art); 
and superhuman play and analysis in strategy games (e.g., chess and Go).[2] However,
many AI applications are not perceived as AI: "A lot of cutting edge AI has filtered into general applications,
often without being called AI because once something becomes useful enough and common enough
it's not labeled AI anymore."[3][4]
"""

lines = str.split('/n')
mylist = []
count = 0
for x in lines:
    count += x.count('AI')
    mlist = x.replace('AI','Artificial Intelligence')
    mylist.append(mlist)
result ='/n'.join(mylist)
print(result)
print('Total count of Artificial Intelligence:',count)

#----------------------------------------------------
name = "Mohammed"
list=[]
for x in name:
        list.append(x)
list.reverse()
reverse_result="".join(list)
print(reverse_result)

#-----------------------------------------------------

str = 'Artificial Intelligence'
list=[]
for x in str :
    list.append(x)
list.reverse()
result = ''.join(list)
print(result)
    
#--------------------------------------------------------

list = ['Mohammed' , 'Ahmed' , 'farooqui' , 'From........']
mylist=[]
for x in list :
    mylist.append(x)
mylist.reverse()
result=''.join(mylist)
print(mylist)
print(mylist[3])


str ='hello how are you'
list = []
for x in str :
    list.append(x)
    count = count('a','e','o','h')
list.reverse()
print()
    
#--------------------------------------------------------

#list comprehension
list = [1,2,3,4,5]
list2=[]
for x in list:
    list2.append(x)
print(list2)

#unpacking 
mytuple=(1,2,3,4)
(a , b , c ,d)=mytuple
print(d)


#--------------------------------------------------------

mytuple = (1,2,3,4)
mylist = list(mytuple)
mylist[0]=100
mytuple=tuple(mylist)
print(mytuple)
print(mytuple.count(2))
print(mytuple.index(3))

for x in mytuple:
    print(x)
#--------------------------

import numpy as np 

list = (1,2,3,4,5)
arrays = np.array(list)
print(arrays)
print(type(arrays))

#1D Array
array = np.arange(1,7)
print(array)

#2D Array
array = np.arange(1,7).reshape(2,3)
print(array)


import array as arr





















