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