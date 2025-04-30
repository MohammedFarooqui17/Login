# function:
#Lambda
"""Lambda functions are best used in situations where you need a simple, short-lived function,
particularly when you require a function as an argument to another function"""
a = lambda a , b :a/b
print(a(8,2))


def apply_operation(x, y, operation):
    return operation(x,y)
result = apply_operation(4, 5, lambda a, b: a + b)
print(result)  

def myfunc(x,y,func):
    return func(x,y)
result=myfunc(4,5, lambda x,y:x*y)
print(result)

"""Functions in Python are used to encapsulate reusable pieces of code.
They allow you to break down your program into smaller,
more manageable parts, making your code more organized, readable, and maintainable.
Here are some common situations and requirements where using functions is beneficial:"""

def function(a,b):
    return a + b  
print(function(2,3))



def calculate_rectangle_area(length, width):
    return length * width

def main():
    
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_rectangle_area(length, width)
    print("The area of the rectangle is:", area)
    
if __name__ == "__main__":
    
    main()


def function(x):
    return 5 + x  
print(function(5))



#-----------------------------------
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def find_max(a, b):
    if a > b:
        return a
    return b


def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result


def main():
    
    num = 10
    result = check_even_odd(num)
    print(f"{num} is {result}")
    

    max_value = find_max(10, 20)
    print(f"Maximum value is {max_value}")
    

    sum_result, diff_result = calculate(10, 5)
    print(f"Sum: {sum_result}, Difference: {diff_result}")

if __name__ == "__main__":
    main()
#-------------------------------------------------------------
# Default parameter

def myfunc(name,country='England'):
    print(name,country)
myfunc('Mohammed')
myfunc()


#**kwargs :This way the function will receive a dictionary of arguments

def myfunc(**person):
    print('My name is :',person['name'])
myfunc(name='Mohammed', lname='Farooqui')


#args* :This way the function will receive a tuple of arguments, 
def myfunc(*person):
    print('My name is :',person[1])
myfunc('Mohammed', 'Farooqui')



# Positinal argument/keywords argument
def myfunc(length,breadth):
    return length*breadth
print(myfunc(length=7,breadth=8)) 

def myfunc(x,y):
    return x +y
print(myfunc(6,8))


#-----------------------------------------------------------------
#Lambda in List Comprehensions
numbers = [1, 2, 3, 4, 5]
incremented_numbers = [(lambda x: x + 1)(x) for x in numbers]
print(incremented_numbers)



























