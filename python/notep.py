# classes from apna college python series

# basics = None
# print("prithvi")
# name = "prithvi raj mandal"
# age = 19
# mybalance = 1000.50
# is_student = True
# print("name:", name)
# print("age:", age)
# print("balance:", mybalance)
# print("is student:", is_student)
# print(type(name))
# print(type(age))
# print(type(mybalance))
# print(type(is_student))


# operators = None
# Arithematic_operators = None
# a = 10
# b = 5
# print("sum", a + b)
# print("difference", a - b)
# print("product", a * b)
# print("power", a ** b)
# print("quotient", a / b)
# print("floor division", a // b)
# print("modulus", a % b)

# Comparison_operators = None
# print("a > b:", a > b)
# print("a < b:", a < b)
# print("a == b:", a == b)
# print("a != b:", a != b)
# print("a >= b:", a >= b)
# print("a <= b:", a <= b)

# assignment_operators = None
# num = 10
# num = 10 + 10
# print(num)
# num += 10
# print(num)
# num -= 5
# print(num)
# num *= 2
# print(num)
# num /= 5
# print(num)
# num **= 3
# print(num)

# logical_operators = None
# x = True
# print(x)
# y = False
# print(y)
# print(not x)
# print(not y)
# p = 20 
# q = 10
# print(not (p > q))
# val1 = True
# val2 = True
# print("ans of and:", val1 and val2)
# val3 = False
# print("ans of and:", val1 and val3)
# print("ans of or:", val1 or val3)
# print("and operator:", (q==p) and (p<=q))

# type_conversion = None
# a = 10
# b = 2.5
# consum = a + b
# print(consum)
# type_casting = None
# a = int("10")
# b = 10.5
# cassum = a + b
# print(cassum)
# c = float("10")
# cassum1 = a + c
# print(cassum1)
# d = "prithvi"
# e = float("prithvi")
# cassum2 = a + e
# # print(cassum2)
# p = 3.14
# pi = str(p)
# print(type(p))
# print(type(pi))

# comments in python
# single line #

# """
# multi line comment
# """

# # inputs in python
# # input()
# valin = input("enter some value:")
# print(valin)
# print(type(valin))
# valin = int(input("enter some value:"))
# print(valin)
# print(type(valin))
# valin = float(input("enter some value:"))
# print(valin)
# print(type(valin))

# practice inputs

# name = input("enter your name: ")
# age = int(input("enter your age: "))
# balance = float(input("enter your balance: "))
# print("my name is ", name)
# print("my age is ", age)
# print("my bank balance is ", balance)
# print(type(name))
# print(type(age))
# print(type(balance))

# day 2 of python
# string 
# it is a datatype that stores sequence of characters

# basic operations
# concatenation
# hello + world = helloworld

# length of str
# len(str)

# str = "this is a string..."
# str1 = "can add numbers"
# str2 = str + str1
# print(str1)
# lens = len(str)
# len2 = len(str2)
# str functions
# print(str[0:4])
# print(str[-5:-2])
# print(str.endswith("..."))
# print(str.endswith("yes"))
# print(str.capitalize())
# print(str)
# print(str.replace("a", "b"))
# print(str.find("i"))
# print(str.count("i"))
# conditional statements

# age = 17

# if(age >= 18):
#     print("is major")
#     print("can vote")
# elif(age == 17):
#     print("is almost major")
# else:
#     print("is minor")

# nested
marks = int(input("enter marks: "))

if(marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of student is : ", grade)

# nesting:

age = int(input("enter the age: "))
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("they cannot drive")