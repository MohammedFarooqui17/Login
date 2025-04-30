list=['name','steve','peterson','cook']
for x in list:
    print(x)
    for i in x:
        print(i)
       
        
list=['name','steve','peterson','cook']       
index=0
while index<len(list):
    print(list[index])
    index+=1



my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
keys = list(my_dict.keys())
#print(keys)
index = 0
while index < len(keys):
    key = keys[index]
    #print(key)
    value = my_dict[key]
    #print(value)
    print(f"Key: {key}, Value: {value}")
    index += 1

    
my_dict={'profession':'cricketer','name':'Broad','age':39,'country':'england'}
# for key,value in my_dict.items():
#     print(key,value)
keys=list(my_dict.keys())
index=0
while index<len(keys):
    key=keys[index]
    value=my_dict[key]
    print(key,value)
    index+=1
    
    
list=[1,2,3,4,'list','tuple','dict','set']
index=0
while index < len(list):
    # print(list[index])
    index+=1
    # if index==4:
    #     break
    if index==3:
        continue
    print(list[index])
    

list1=[1,2,3,4]
index=0
while index<len(list1):
        print(list1[index])
        index+=1



