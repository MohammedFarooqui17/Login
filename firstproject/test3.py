import test2 

test2.main()

def myfunc():
    return lambda x , y : x + y
print(myfunc(3,5))
a = lambda x , y : x + y
print(a(3,5))