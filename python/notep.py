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
# marks = int(input("enter marks: "))

# if(marks >= 90):
#     grade = "A"
# elif (marks >= 80 and marks < 90):
#     grade = "B"
# elif (marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of student is : ", grade)

# # nesting:

# age = int(input("enter the age: "))
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("they cannot drive")

# learnt a thing that to do more commits
# for better contribution chart
# string revise
# str1 = "this is apna college lecture'revision"
# str2 = 'my name prithvirajmandal'
# str3 = "there are so many car's"
# print(str3)
# str4 = """thats the "incredibille" car."""
# print(str4)
# escape sequence characters are used to give formatting to string
# example \n nextline   \t tab
# stra = "apna"
# strb = "college"
# concat = stra + " " + strb
# print(concat)
# print(len(stra))
# finallen = len(stra) + len(strb)
# print(finallen)
# print(len(concat))
# indexing character adress number
# ch = stra[1]
# print(ch)
# slices
# accessing parts of a string
# start index and end index betwwen data is slice
# str = "apna college"
# print(str[1:6 ])
# print(len(str))
# print(str[5:len(str)])
# print(str[5:])
# print(str[5:12])
# negative indexing
# apple -5a -4p -3p -2l -1e
# str = "apple"
# print(str[-3 : -1])
# string functions
# str = "i am prithvi"
# print(str.endswith("vi"))
# print(str.capitalize())
# strr = "i am studying python form apna college"
# print(strr.replace("python","java"))
# print(strr.replace("co","ja"))
# print(strr.replace("i","j"))
# print(strr.find("a"))
# str.endswith
# str.capitalize
# str.replace replaces target with desiredtarget
# str.find gives index
# str.count gives count number of targets
# age = 19
# if(age <= 24):
#     print("youth")
# else:
#     print("middle aged")
# if(age >= 18):
#     print("can vote")
#     print("can drive")
# else:
#     print("is minor")
#     print("str.len")
# lecture 3 list and tuples

# list is a mutable we can add(append)and remove data unlike tuple = immutable(fixed)

# marks of a student stored in a list 
# marks = [19, 18, 20, 19, 16]
# print(marks)
# print(type(marks))
# print(marks[0],marks[4])
# print(len(marks))

#list can store multiple datatypes also 
# student = ["prithvi", 99, "kolkata"]
# print(student)
# # print(student[2])
# # print(type(student))
# # print(len(student))
# print(student[0])
# student[0] = "piku"
# print(student)
#list can store multiple datatypes also 
# student = ["prithvi", 99, "kolkata"]
# print(student)
# # print(student[2])
# # print(type(student))
# # print(len(student))
# print(student[0])
# student[0] = "piku"
# print(student)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# print(a<b,"less")
# print(a>b, "great")
# print(a<=b,'lessequal')
# print(a>=b, 'greatequl')
# print(aa==b, 'equal')
# print(aa!=b, 'noteq')

# a = 21
# b = 2
# aa = a

# ba = a+b
# print('ba' , ba)

# num =3
# print(num)
# num%=2
# print(num)

# str = "hello prithvi"
# print(str)
# print(len(str))
# print("does string ends with i:",str.endswith("i"))
# print(str.capitalize())
# print(str.replace("i","a"))
# print(str.find("prithvi"))
# print(str.count("l"))
# age = int(input("enter age:"))
# if(age>=18):
#     print("eligible for license")
# elif(age >= 16 and age < 18):
#     print("can have learners permit")
# else:
#     print("underage!")

# guy = ["prithvi", 535 , "lateral"]
# print(type(guy))
# print(guy)

# list = [12,14,51,13,11]
# print(list)
# print(type(list))
# print(list[-3:])
# list.append(61)
# print(f"updated list1\n {list}")
# list.sort()
# print(f"updated list2\n {list}")
# list.sort(reverse=True)
# print("desc list:", list)
# fruit = ["mango", "banana", "guava"]
# fruit.reverse()
# print(fruit)
# # fruit.sort(reverse=True)
# # print("updated list\n ", fruit)
# fruit.insert(2, "apple")
# print(fruit.append("banana"))
# fruit.remove("banana")
# fruit.pop(1)
# print(fruit)
# tup = (12,13,14,15)
# print(tup)
# print(tup[1:2])
# print(fruit.count("banana"))
# print(tup.count(12))
# dictionaries are used to store data as key value pairs it is a data structure

# dictionar = {
#     "keyone" : "prithvi"
# }
# print(dictionar["keyone"])

# mydat = {
#     "myname":"prithvi",
#     "myage" : 19,
#     "mygender": "male",
#     "mytuple" : ("python",1,"hello"),
#     "mylist" : ["python",1,"hello"]
# }
# print(mydat["myname"])
# print(type(mydat["mylist"]))
# mydat["name"] = "prithviraj" #overwrite
# mydat["surname"] = "mandal" #add value
# print(mydat)
# numlist = [2,1,3]
# print(numlist)
# print(numlist.reverse())
# print(numlist)
# print(type(numlist))
# print(len(numlist))
# print(numlist.append(5))
# print(numlist)
# print(numlist.sort())
# print(numlist.sort(reverse=True))
# print(numlist)
# langlist = ["hindi","enlgish","hindi","telugu"]
# print(langlist.reverse())
# print(langlist.sort())
# print(langlist.remove("hindi"))
# print(langlist)
# langlist.pop(2)
# print(langlist)
# langtuple = ("hindi","telugu","hindi")
# print(langtuple)
# print(langtuple.index("telugu"))
# print(langtuple.count("hindi"))
# mov1 = input("enter your fav1:")
# mov3 = input("enter your fav3:")
# mov2 = input("enter your fav2:")

# movies = [mov1,mov2,mov3]
# mov4 = input("enter your fav4:")
# movies.append(mov4)
# print(movies)
# songs = []
# songs.append(input("enter song 1 :"))
# songs.append(input("enter song 2 :"))
# songs.append(input("enter song 3 :"))
# print(songs)

# copysongs = songs.copy()
# copysongs.reverse()
# if(songs == copysongs):
#     print("palindrome")
# else:
#     print("not palindrome")
# tuplegrade = ["C","D","A","A","B","B","A"]
# print(tuplegrade.count("A"))
# tuplegrade.sort()
# print(tuplegrade)
# notebook = {
#     "name" : "prithvi",
#     (000,1234) : "coordinates",
#     19 : "my age",
#     "is_adult" : True,
#     "scores" : {
#         "nuclear physics" : [12,14,15,15],
#         "space myths" : [12,14,15,15],
#         "rocket science" : [12,14,15,15],
#         "socialize robots" : [12,14,15,15],
#     }
# }
# print(type(notebook))
# print(notebook)
# notebook["name"] = "Prithviraj"
# print(notebook)
# print(notebook[(000,1234)])
# print(notebook["scores"]["nuclear physics"])
# print(notebook.keys())
# print(notebook.values())
# print(len(notebook))
# print(notebook["scores"].keys())
# print(list(notebook.keys()))
# print(notebook.items())
# print(notebook["name"])     #it gives error
# print(notebook.get("name")) #it does not give error it checks if didn't find gives none
# print(notebook)
# new_notebook = {
#     "city" : "ramagundam",
#     "name" : "PRITHVIRAJ MANDAL"
# }
# print(notebook.update(new_notebook))
# print(notebook)

"""set is similar like dictionary but only saves values and ignores duplicates,
elements=immutable only but set entirely is mutable can comply changes"""
# collection = {1,22,"prithvi0","ramagundam",True}#here true and 1 are likely similar so set ignores one
# print(collection)
# print(len(collection))
# null_collection = {}
# print(type(null_collection))#dictionary has also same {} so to create a null set use method set()
# collection_null = set()
# print(type(collection_null))
# collection_null.add("hello")
# collection_null.add("adding in null set using add method")
# collection_null.add(12.55)
# collection_null.add((12,13,14))#also we can add tuples beacuse it is hashable
# print(collection_null.pop())

"""mutable types are not hashables which don't support to be added"""
# print(collection_null)
# collection_null.remove("adding in null set using add method")
# print(collection_null)
# collection_null.pop() #removes random value
# print(collection_null)
# collection_null.clear()#removes / clears everything
# print(collection_null)
# print(len(collection_null))

# set1 = {1,2,3,4,3,4,5}
# set2 = {2,3,3,4,5,6}
# print(set1)
# print(set1.union(set2))
# print(set1.intersection(set2))

""" lecture4 task1 add values in dictionary"""
# taskdict = {
#     "table" : [("a piece of furniture","lists of facs and figures")],
#     "cat" : "a small animal"
# }
# print(taskdict)
# print(len(taskdict))
# lecture4 task 2 given a list find redundant length
# givenlist = ["python","java","C++","python","javascript","java","python","java","C++","C"]
# print(givenlist)
# solution_set = set(givenlist)
# print(solution_set)
# print("classrooms needed for each subject:",len(solution_set))

"""lecture4 task3 empty dictionary add marks of 3 subjects one by one by user input (watched)"""
# stud_dict = {}
# print(type(stud_dict))
# maths = int(input("enter marks for maths:"))
# stud_dict.update({"maths": maths})


# chem = int(input("enter marks for chem:"))
# stud_dict.update({"chem": chem})


# bio = int(input("enter marks for bio:"))
# stud_dict.update({"bio": bio})
# print(type(stud_dict))
# print(len(stud_dict))
# print(stud_dict)

"""lecture4 task4 find a way to store 9 and 9.0 in a set
we have to solutions i.one we can save as a str | ii.we can save both in a tuple then save them"""

# set9a = {9,"9.0"}
# print(type(set9a))
# print(set9a)

# set9b = set()
# set9b.update(("int",9))
# set9b.update(("float",9.0))
# print(set9b)

# set9c = {
#     ("int",9),
#     ("float",9.0)
# }
# print(set9c)

""" lecture 5 loops in python"""
# while loop
# coin_count = int(input("enter number of coins counted:"))
# amount = 0
# while coin_count <=10:
#     amount += 1
#     print("adding 1 rupee to count")
#     coin_count+=1
# print(amount)

# i = 1 
# while i <=3000:
#     print("i love you...", i)
#     i += 1
# print("hello")


"""understanding break"""
# a = 1
# while a < 6:
#     print(a)
#     if a == 3:
#         break
#     a += 1
# print("end")

"""example if our code is like"""
# given_tuple = (1,4,9,16,25,36,49,64,81,100)
# print("given tuple is :",given_tuple)
# print("select x within given tuple")
# x = int(input("enter x to find:"))
# i = 0
# while i < len(given_tuple):
#     if(given_tuple[i] == x):
#         print("x found at index:",i)
#     else:
#         print("finding...")
#     i += 1
# print("end")

"""gives finding because even it gets an answer,it still searches for any possible second answer
until loop ends"""
# so it looks like

# given_tuple = (1,4,9,16,25,36,49,64,81,100)
# print("given tuple is :",given_tuple)
# print("select x within given tuple")
# x = int(input("enter x to find:"))
# i = 0
# while i < len(given_tuple):
#     if(given_tuple[i] == x):
#         print("x found at index:",i)
#         break
#     else:
#         print("finding...")
#     i += 1
# print("end")

#  so it ends after it met a solution condition

"""understanding continue """
# i = 0
# while i <= 5:
#     if (i == 3):
#         i += 1 
#         continue #continue acts as skip for 3 even it met continue checking
#     print(i)
#     i += 1
# print("end")

# """proper tic tac to explantion"""
# board = [" " for i in range(9)]
# player = "X"

# while True:
#     # display board
#     print(board[0], "|", board[1], "|", board[2])
#     print("---+---+---")
#     print(board[3], "|", board[4], "|", board[5])
#     print("---+---+---")
#     print(board[6], "|", board[7], "|", board[8])

#     pos = int(input("Player " + player + " choose position (1-9): ")) - 1

#     # if position already taken → skip rest of loop
#     if board[pos] != " ":
#         print("Position already occupied! Try again.")
#         continue   # same player gets another chance

#     # update board
#     board[pos] = player

#     # check winner (simple row example)
#     if board[0] == board[1] == board[2] == player or \
#        board[3] == board[4] == board[5] == player or \
#        board[6] == board[7] == board[8] == player:
#         print(" Player", player, "wins!")
#         break

#     # switch player
#     player = "O" if player == "X" else "X"

# break = is used to terminate loop when encountered condiditon
# continue = terminates execution in the current iteration & continues executioin of the loop
# with the next iteration 

"""understanding for"""
# veggies = ["potato","tomato","cucumber"]

# for val in veggies:
#     print(val)

# for i in range(9):
#     print(i)
# name = "prithvi"
# for v in name:
#     print(v)
#     if(v == "i"):
#         print("skipping")
#         break
# else:
#     print("end")

# else is used to print an optional statement for an loop
# The else block runs only if the loop finishes normally (without hitting a break).
# If the loop is interrupted by break, the else block is skipped.

"""understanding range"""
# range function gives a sequence of numbers,
# starting from 0 by default,increments by 1 and stops before specified number
# seq = range(10)
# startstop = range(2,10)
# startstopstep =  range(2,10,2)
# for i in seq:
    # print(i)

# can write in 3 types
# range(10) = given stop before
# range(2,10) = given start, stop before
# range(2,10,2) = given start, stop before and step size

"""understanding pass keyword"""
# it is used to give a loop a null statement so it has a placeholder which can be
# used later in future

# for i in range (10):
#     # hello
# print("future work")
# this expects something in for block so we use pass so in future we can add anything

# for i in range (10):
#     pass
# print("future work")

# also used in conditional statements

# a = 10
# if (a < 100):
#     # hello
# print("did check")

# solution
# a = 10
# if (a < 100):
#     pass
# print("did check")

# lecture 6 functions and recursion
"""understanding functions"""
# block of statements that perform a specific task by calling them
# def func_name(parameter1, parameter2):   /function definition
#           sum = parameter1+parameter2
#           print(sum)
#           return sum

# func_name(argument1, argument2) / calling a function & arguments are values to pass on parameter

# # example1
# def add(a, b):
#     print(a + b)   # just prints result

# result = add(3, 4)   # function runs
# print("Result is:", result)

# example2
# def add(a, b):
#     return a + b   # sends result back

# result = add(3, 4)   # function returns 7
# print("Result is:", result)


# def calc_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# calc_sum(134,3)

# def avertre(a, b, c):
#     aver = (a+b+c)/3
#     print("average of three:", aver)
# avertre(2,3,4)

# def calavg(a, b, c):
#     avg = (a+b+c)/3
#     return avg
# result = calavg(2,3,4)
# print(result)

# functions are two types predefined functions and userdefined 
# predefined include print() len() type() range()

# to print to statements in same line use end = " " becuase in predefined code we have end="\n"

# print("hello prithvi", end=" ")
# print("this is actually second line but includes in line one because end is a space", end="$")
# print("u can also use anything to add at end and continue statement like $ used in between second and this line")

"""understanding default parameters"""
# assigning a default value to a parameter, which is used when no argument is passed.
# constraint is first it should have a non-default parameter then a default parameter can be given
# example which works
# def adda(a, b=2):
#     return a + b
# ad = adda(1)
# print(ad)

# example which not works
def adda(a=1, b):
    return a + b
ad = adda(1)
print(ad)