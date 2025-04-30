"""
# Numeric Data Types : Numeric data types are types of data that consist of numbers,
# which can be computed mathematically 
# with various standard operators such as add, minus, 
* - int:Integer data types are a category of data types in programming languages that represent whole numbers. 
These numbers can be positive, negative, or zero, 
* - float  :Float data types represent numbers that have a fractional component"""

# STRING  :
#String data types represent sequences of characters and are used for storing and manipulating text. 
#EXAMPLE:

str = 'Hello'
print(str[0])
print(len(str))

str = 'Hello'
for x in str :
    print(x)
    
str = 'Hello Morning'
if 'Hello' in str :
    print('yes')
    
str = 'Hello Morning'
if 'Morning' not in str :
    print('no')
else:
    print('yes')
    
str = 'Hello Morning'
print('hello' in str)
print('hello' not in str)

#slicing
str ='  Hello Morning  '
print(str[-5:-3])

str ='  Hello Morning  '
print(str.upper())
print(str.lower())
print(str.strip())#remove the white space from begning or ending
print(str.replace('H','h'))


str ="Hello * Morning"#The split() method splits the string into substrings if it finds instances of the separator
print(str.split(","))


#concatenation
s='hello'
S='Hello'
print( s +" "+ S)
print(s+S)



# format String :
a = 'steve'
age=21
name = f"My name is : {a}  and  {age} olds"
print(name)

a = 19
b = 90
c = f'The sum of this two numbers is :{a + b : .3f}'#Modifier
print(c)


# ESCAP CHARACTR:To insert characters that are illegal in a string, use an escape charac

A = "PYTHON PRACTICE IN \" 90\" "
print(A)

a = ' hello\n world'
print(a)

str = 'HELLO hgiug{no}'
print(str.capitalize())#it will capitalized first character of string
print(str.casefold())#Converts string into lower case
print(str.count('hello'))#	Returns the number of times a specified value occurs in a string
print(str.endswith(''))#check the mention condition if met return true or false 
print(str.format(no=8))
print(str.index('g'))
print("d".join(str))#will join this d into out str 
print(str.swapcase())#make the upper case if it will in lower
print(str.title())#convert each first word in uppercase 

