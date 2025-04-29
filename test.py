# def dec(fun):
#     def inner(a,b):
#         a,b = b,a
#         return a,b
#     return inner

# @dec
# def myfun(a,b):
#     return a,b
# print(myfun(5,10))


# num1 = int(input("Enter Your Number:"))
# num2 = int(input("Enter Your Number:"))
# if num2==0:
#     print("Number Should Not be Zero")
# result = num1/num2
# print(result)


# base = float(input("Enter Your Number:"))
# height = float(input("Enter Your Number:"))
# area = 0.5 * base * height
# print(area)


# swapping two number
# num1 = int(input("Enter Your Number:"))
# print(num1)
# num2 = int(input("Enter Your Number:"))
# print(num2)

# temp = num1
# num1 = num2
# num2 = temp
# print(num1 , num2)


# without using temp swapping two number
# number1 = int(input("Enter Your Number:"))
# number2 = int(input("Enter Your Number:"))
# number1,number2 = number2 , number1
# print(number1,number2)


# Write a Python program to display calendar.
# import calendar
# year = int(input("Enter Year:"))
# Month = int(input("Enter Month:"))
# result = calendar.month(year,Month)
# print(result)



# solve quadratic equation

# import math
# a = float(input("Enter Your Number:"))
# b = float(input("Enter Your Number:"))
# c = float(input("Enter Your Number:"))

# discriminant = b**2 - 4*a*c
# print(discriminant)


# if discriminant >0:
#     root1 =(-b + math.sqrt(discriminant)/(2*a))
#     root2 =(-b - math.sqrt(discriminant)/(2*a))
#     print(root1)
#     print(root2)


# elif discriminant==0:
#     root = -b/(2*a)
#     print(root)
# else:
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#     print(f"Root 1: {real_part} + {imaginary_part}i")
#     print(f"Root 2: {real_part} - {imaginary_part}i")



# number = float(input("Enter Your Number:"))
# if number>0:
#     print("positive")
# elif number ==0:
#     print("zero")
# else:
#     print("Negative")



# def myfun(num):
#     poisitive=[]
#     Negative=[]
#     Zero=[]
#     for i in num:
#         if i>0:
#             poisitive.append(i)
#             print(poisitive)
#         elif i ==0:
#             Zero.append(i)
#             print(Zero)
#         else:
#             Negative.append(i)
#             print(Negative)
#     return poisitive , Negative , Zero


# number = [1,-3,0,76,89]
# positive, Negative , Zero = myfun(number)
# print(positive)
# print(Negative)
# print(Zero)


# number = int(input("Enter Your Number: "))
# if number%2==0:
#     print("Even")
# else:
#     print("odd")


# def check(num):
#     Even=[]
#     Odd=[]
#     for i in num:
#         if i%2==0:
#             Even.append(i)
#         else:
#             Odd.append(i)
#     print("Even Number:", Even)
#     print("Odd Number:" , Odd)

# list1=[1,2,3,45,6]
# print(check(list1))




# prime Number 
# number = int(input("Enter Your Number :"))

# Flag = False
# if number == 1:
#     print(f"{number} is not a prime number")
# elif number > 1:
#     for i in range(2,number):
#         print(i)
#         if number%i==0:
#             Flag = True
#             break
# if Flag:
#     print(f"{number} is not a prime number")
# else:
#     print(f"{number} is prime number")



# prime=[]
# non_prime=[]

# for number in range(1,100):
#     # print(number)
#     # print("1st Loop")
#     if number>1:
#         is_prime = True
#         for i in range(2,number):
#             # print(i)
#             # print("second Loop")
#             if number%i==0:
#                 is_prime = False
#                 break
#         if is_prime:
#                 prime.append(number)
#         else:
#              non_prime.append(number)

# print(prime)
# print(non_prime)


# lower=1
# upper = 10

# print(f"{lower} and {upper}")
# for number in range(lower,upper+1):
#     if number >1:
#         for i in range(2,number):
#             if number%i==0:
#                 break
#         else:
#             print(number)  
# print() 
    
    

# Even=[]
# Odd=[]
# for i in range(1,101):
#     if i%2==0:
#         Even.append(i)
#     else:
#         Odd.append(i)
# print(Even)
# print(Odd)



# Factorial Problem

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# number=int(input("Enter Your number"))
# print(factorial(number))


# number=int(input("Enter Your number"))
# factorial = 1
# if number<1:
#     print("Factorial does not exist for negtive number")
# elif number ==0:
#     print(" Factorial of 0 is also 1")
# else:
#     for i in range(1,number+1):
#         factorial = factorial*i
#     print(f"factorial of {number} : {factorial}" )



# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} :", i*j)


# number = int(input("Enter Number: "))
# sum =0
# for i in range(1,number+1):
#     sum=sum+i
# print(f"The sum of {number} : {sum}")



# def sum1(num):
#     total=0
#     for i in num:
#         total =total+i
#     return total
# list1=[1,2,3,4,5]
# print(sum1(list1))



# def bodymass(w,h):
#     return w/h**2
# w=int(input("Eneter Your Weight"))
# h=int(input("Enter Your Height"))
# print(bodymass(w,h))


# def cubesum(num):
#     if num<0:
#         return 0
#     else: 
#         result=sum([i**3 for i in range(1,num+1)])
#         return result
    
# number=int(input("Enter Yor Number :"))
# print(cubesum(number))


# find the largest Element
# def largest(arr):
#     if not arr:
#         return "Array is Empty"
#     else:
#         largest_element=arr[0]

#         for i in arr:
#             if i>largest_element:
#                 largest_element=i
#         return largest_element

# list1=[23,5,41,6,78,98,8]
# print(largest(list1))



# find the smallest number
# list1 = [1,2,3,4,5]
# number=list1[0]
# for i in list1:
#     if i<number:
#         number=i
# print(number)



# Sorting Alphabet
# mystr=input("Enter Your Word :")
# words = [word.capitalize() for word in mystr.split()]
# words.sort()
# print("The Sorted Words ")
# for word in words:
#     print(word)


# Write a Python Program to Remove Punctuation From a String
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ 0123456789'''
# mystr = input("Enter Your ....... ")
# words=""
# for i in mystr:
#     if i not in punctuations:
#         words=words+i
# print(words)


# list1 = [1,2,3,4,5]
# number=1
# for i in list1:
#         number= number*i
# print(number)



# find the second largest Element
# salary = [28976735,698847,4764753,69774,57463458,895463]
# unique_salary=list(set(salary))
# data = unique_salary.sort(reverse=True) 
# print(unique_salary)
# print(len(unique_salary))
# print(data)

# if len(unique_salary)>=2:
#     print(f"The second largest salary is : {unique_salary[1]}")




# Write a Python program to find N largest elements from a list.
# def find_largestElement(lst,n):
#     sorted_list = sorted(lst,reverse=True)

#     largestElement = sorted_list[:n]
#     return largestElement

# number=[2,22,31,78,97,65,42,90,74,52,21,41,81,90]
# n=int(input("Enter Number:"))
# print(find_largestElement(number,n))


# Write a Python program to Remove empty List from List.
# lst = [[1,2,3],[],[7,6,4,3],[8,9,0,1,2,3],[],[124,32],[12,3,4,5,6,],[]]
# filtere_list = [i for i in lst if i]
# print(filtere_list)


# Write a Python program to Count occurrences of an element in a list.
# def count_ElementOccurence(lst,num):
#     count=lst.count(num)
#     return count

# number=[1,1,2,3,4,5,6,3,4,5,2,7,8,9,9,4,5,6]
# n = int(input("Enetr Your Number :"))
# print(count_ElementOccurence(number,n))



# def count(lst,num):
#     count_num=0
#     for i in lst:
#         if i ==num:
#             count_num+=1
#     return count_num

# number = [1,1,2,3,4,5,6,3,4,5,2,7,8,9,9,4,5,6]
# n = int(input("Enter Your Number :"))
# print(count(number,n))



# Write a Python program to find words which are greater than given length k.
# def find_lenofword(word,n):
#     lst=[]
#     for i in word:
#         if len(i)>n:
#             lst.append(i)
#     return lst

# words=word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
# num=int(input("Enter Your Number :"))
# print(find_lenofword(words,num))


# Write a Python program for removing 𝑖𝑡ℎ character from a string.
# removed_chars = []
# def find(word,num):
#     if num<0 or num>=len(word):
#         return word
#     removed_chars.append(word[num])
#     result=word[:num]+word[num+1:]
#     print(result)
#     return result

# words="MohammMed  Farooqui"
# num=int(input("Enter Your ith Number :"))
# print(find(words,num))
# print(removed_chars)



# Write a Python program to check if a given string is binary string or not
# def check_binary(inpu):
#     for i in inpu:
#         if i not in "01":
#             return False
#     return True
# bin_num=input("Eter Your number :")
# print(check_binary(bin_num))


# Write a Python program to find uncommon words from two Strings.
# def uncommon(str1,str2):
#     word1=set(str1.split())
#     word2=set(str2.split())

#     uncommon_word=word1.symmetric_difference(word2)
#     uncommon_list = list(uncommon_word)
#     return uncommon_list

# str1=input("Enter Your Sentences :")
# str2=input("Enter Your Sentences :")
# print(uncommon(str1,str2))


# Write a Python program to Extract Unique dictionary values.
# my_dict = {
#  'a': 10,
#  'b': 20,
#  'c': 10,
#  'd': 30,
#  'e': 20
# }
# uniq_val=set()
# for i in my_dict.values():
#     uniq_val.add(i)
# data=list(uniq_val)
# print(data)



# Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:

# user_input=input("Enter Your password : ")
# letter=0
# digit=0

# word=[]
# number=[]

# for i in user_input:
#     if i.isalpha():
#         word.append(i)
#         letter=letter+1
#     elif i.isdigit():
#         number.append(i)
#         digit=digit+1

            
# data1 = "".join(word)
# data2 = "".join(number)

# # Output results
# print("Letters:", data1, "Count:", letter)
# print("Digits:", data2, "Count:", digit)




































































































