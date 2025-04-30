class employee:
    increment=2
    def __init__(self,fname,lname,department,salary):
        self.fname=fname
        self.lname=lname
        self.department=department
        self.salary=salary
        pass
    def increase(self):
        self.salary=self.salary*employee.increment
        
emp1=employee('steve','jhonson','account',10000000)
emp2=employee('mechgrath','james','marketing',4000000)

print(emp1.salary)
emp1.increase()
print(emp1.salary)
#--------------------------------------------------------------
class employee:
    increment=2
    def __init__(self,fname,lname,department,salary):
        self.fname=fname
        self.lname=lname
        self.department=department
        self.salary=salary
        pass
    def increase(self):
        self.salary=self.salary*employee.increment
        
    @classmethod    
    def change_increment(cls,amount):
        cls.increment=amount
        pass
        
emp1=employee('steve','jhonson','account',10000000)
emp2=employee('mechgrath','james','marketing',4000000)

print(emp1.salary)
employee.change_increment(4)
emp1.increase()
print(emp1.salary)
#-------------------------------------------------

class employee:
    increment=2
    def __init__(self,fname,lname,department,salary):
        self.fname=fname
        self.lname=lname
        self.department=department
        self.salary=salary
        pass
    
    def increase(self):
        self.salary=self.salary*employee.increment
        
    @staticmethod   
    def isopen(days):
        if days=='sunday':
            return False
        else:
            return True
        
        
emp1=employee('steve','jhonson','account',10000000)
emp2=employee('mechgrath','james','marketing',4000000)


print(emp1.salary)
emp1.increase()
print(emp1.salary)
#print(employee.isopen('sunday'))
print(emp1.isopen('sunday'))

class programmer(employee):
    def __init__(self, fname, lname, department, salary,language,exp):
        super().__init__(fname, lname, department, salary)
        self.language=language
        self.exp=exp
        
emp3=employee
        
#-------------------------------------------------))

def myfunc(x,y):
    if x % 2 == 0 and y % 2 == 0:
        return x*y
    else:
        return x+y

print(myfunc(6,9))


str = 'hello'
result=[]
for i in str:
    result.append(i)
    
result.reverse()
reversed_str = "".join(result)
print(reversed_str.upper())


str = 'hello morning'
duplicate=[]
unique = []

for i in str :
    if str.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
    else:
        unique.append(i)
print(duplicate)           
print(unique)


name = 'mohammed'
result = []
for i in name :
    result.append(i)
result.reverse()
reverse_result="".join(result)
print(reverse_result.upper())



dict = {'Name':'Abraham','Designation':'Manager','Company':'HP'}
dict['Location'] = 'Mumbai'
dict.update({'Name':'STEVE'})
print(dict.get('Designation'))
print(dict.keys())
print(dict.values())


dict = {'Name':'Abraham','Designation':'Manager','Company':'HP'}
dict.pop('Name')
dict.update({'Name':'Jordan'})
dict.popitem()
del dict['Company']
del dict
dict.update({'Name':'Abraham','Designation':'Manager','Company':'HP'})


dict={'Name':'Abraham','Designation':'Manager','Company':'HP'}
print("This is the keys",dict.keys,"This is the values")
print("values")
for i in dict:
    print(dict[i]) 
print('keys')   
for i in dict:
    print(i)
    


































