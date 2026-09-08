# lecture 1
# wap to input to numbers & print their sum

# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# sum = a + b
# print("sum equals to:", sum)

# wap to input a side of a square and print its area

# side = int(input("enter side value:"))
# area = side*side
# print("area of given square:", area)

# wap to input 2 floating values and print their average

# x = float(input("enter x value:"))
# y = float(input("enter y value:"))

# avg = (x+y)/2
# print("avg of given float values:", avg)

# wap to input 2 int numbers a,b print true if a is greater than or equal to b. if not false

# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# print(a>=b)

# lecture 2
# wap to input users first name and print its length

# name = input("enter your first name:")
# print("length of ur name",len(name))

# wap to find occurance of any char in given string ex i

# name = input("enter your first name:")
# print("index of first occurance:", name.find("i"))
# print(name.endswith("i"))
# print(name.replace("i","u"))
# print(name.capitalize())
# print(name.count("r"))
# print(name.__contains__("pr"))

# wap to check if a number entered by user is even or odd

# a = int(input("enter a value:"))
# if(a%2==0):
#     print("even")
# else:
#     print("odd")

# wap to find the greatest of 3 numbers input by user

# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# c = int(input("enter c value:"))
# if (a>b and a>c):
#     print("a is greater among 3 values")
# elif(b>a and b>c):
#     print("b is greater among 3 values")
# else:
#     print("c is greater among 3 values")


# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# c = int(input("enter c value:"))
# d = int(input("enter d value:"))

# if (a>b and a>c and a>d):
#     print("a is greater among 3 values")
# elif(b>a and b>c and b>d):
#     print("b is greater among 3 values")
# elif(c>a and c>b and c>d):
#     print("c is greater among 3 values")
# else:
#     print("d is greater among 3 values")
# great = max(a,b,c,d)
# print(great)

# Program to find the largest of 4 numbers using conditionals

# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# c = int(input("Enter c value: "))
# d = int(input("Enter d value: "))

# if (a >= b and a >= c and a >= d):
#     print("a is greatest:", a)
# elif (b >= a and b >= c and b >= d):
#     print("b is greatest:", b)
# elif (c >= a and c >= b and c >= d):
#     print("c is greatest:", c)
# else:
#     print("d is greatest:", d)


# wap to find given value is multiple of 7 or not
# Program to find the largest of 4 numbers using conditionals

# a = int(input("Enter a value: "))
# if(a%7==0):
#     print("it is multiple of seven")
# else:
#     print("it is not multiple of seven")

# lecture 3
# list1 = [1,2,3,4,5,6,7]
# slicing = listname[starting and ending] /ending doesn't print one behind
# print(list1[0:7]) # length is 7 ending index is 6 actually n+1 = 7
# print(list1[-7:-1])
# print(list1.append(8))
# print(list1)
# print(list1.index(7))
# print(list1.sort(reverse=True))
# print(list1)
# print(list1.reverse())
# print(list1)
# list1.insert(6,"hello")
# list1.insert(7, 8)
# print(list1)
# print(list1)
# list1.append(1)
# print(list1)
# list1.remove(1)
# list1.pop(3)
# print(list1)
"""
pop(Index)
list.append(element)
list.remove(first occurance of element)

list.insert(index , element)"""

# tuple1 = (1,2,3,4,5,6,6,7,6)
# print(tuple1)
# print(tuple1[-4:-1])

# print(tuple1.index(4))
# print(tuple1.count(6))

# wap to enter 3 strings and store them in a list
listmov = []

# fav1 = input("enter fav1:")
# listmov.append(fav1)
# fav2 = input("enter fav2:")
# listmov.append(fav2)
# fav3 = input("enter fav3:")
# listmov.append(fav3)
# print(listmov)

# listmov.append(input("enter fav movie"))
# listmov.append(input("enter fav movie"))
# listmov.append(input("enter fav movie"))

# print(listmov)

# wap to check list is palindrome

# a = int(input("enter a value:"))
# b = int(input("enter b value:"))
# c = int(input("enter c value:"))
# d = int(input("enter d value:"))
# e = int(input("enter e value:"))

# listnum = [a,b,c,d,e]

# listnumcop = listnum.copy()
# listnumcop.reverse()
# if (listnumcop == listnum):
#     print("list is palindrome")
# else:
#     print("list is not palindrome")

# wap to count the no. of students with A grade from given list
# grade = ("C","D","A","A","B","B","A")
# print("no. of students with A grade:", grade.count("A"))

#store the above in a list sort the values to A to D
# new_grade = grade.copy()
# new_grade.sort()
# print(new_grade)

# dictnames = {
#     101 : "prithvi",
#     102 : "priyanka",
#     103 : "saloni",
#     104 : "swati",
    
#     "score" : {
#         "mathmarks" : [0,99,22,92,20],
#         "sciencemarks" : [0,93,52,62,70]
#     }
# }
# print(dictnames["score"]["mathmarks"])
# print(dictnames.items())
# print(dictnames.get(101))
# city = {

# "cities" : "ramagundam"   
# }
# dictnames.update(city)
# print(dictnames)

# sets = {1,2,1,2,3,4,5,6}
# print(sets)
# in sets repeated elements are stored only once so it is resoluted to {1,2,3,4,5,6}
# set stores immutable elements but is not immutable it is mutable 
# emp_set = set()
# emp_set.add(1)
# print("empset is :",emp_set)
# sets.add(8)
# sets.remove(1) # removes all occurances of the element
# print(sets)
# sets.pop()
# sets.union(emp_set)
# print(sets)
# sets.intersection(emp_set)
# print(sets)

# store following word meanings into a dictionary
# table = "a piece of furniture", "lists of facts & figures"
# cat = "a small animal"

# taskdict = {
#     "table" : ["a piece of furniture", "lists of facts & figures"],
#     "cat" : "a small animal"
# }

# print(taskdict)

# listsub = ["python","java","c++","python","javascript","java","python","java","c++","c"]

# sets = {"python","java","c++","python","javascript","java","python","java","c++","c"}

# print(len(sets))

# wap to input marks of 3 subjects and store them in dictionary, start with an empty dictionary
# and add one by one,use subject name as key and marks as value

# scoredict = {}
# math = int(input("enter math marks:"))
# phy = int(input("enter phy marks:"))
# bio = int(input("enter bio marks:"))

# scoredict.update({"maths" : math})
# scoredict.update({"physics" : phy})
# scoredict.update({"biology" : bio})

# print(scoredict)

# wap to store 9 and 9.0 in a set figure it out
# set9 = set()
# set9.add(int(9))
# set9.add("9.0")
# print(set9)

# wap to print numbers 1 - 100 using while loop
# a = 0
# while(a<100):
#     a+=1
#     print(a)

# wap to print numbers 100 - 1 using while loop
# a = 100
# while(a>1):
#     a-=1
#     print(a)

# wap to print a multiplication table of a number
# m = 2
# i=1
# while(i<11):
#     print(f"{m}x{i}=",m*i)
#     i+=1

# wap to print the elements of list using a loop
# listsq = [1,4,9,16,25,36,49,64,81,100]
# i=0
# while(i<10):
#     print(listsq[i])
#     i+=1
# a=1
# while(a<11):
#     print(a**2)
#     a+=1

# wap to print sum of first n natural numbers using while
# n = int(input("enter n:"))
# sum = 0
# i = 0
# while (i<=n):
#     sum += i
#     i+=1
# print(sum)

# wap to find factorial of first n numbers using for
# n = int(input("enter n:"))
# fact = 1
# i = 1
# for i in range(1,n+1):
#     fact *= i
#     print(fact)

# waf to print the length of list (list is parameter)
# fruits = ["apple","banana","custard","dragon"]
# def callen(l):
#     print(len(l))
# callen(fruits)

# waf to print the elements of a list in a single line
# fruits = ["apple","banana","custard","dragon"]
# def listline(list):
#     for i in list:
#         print(i, end=" ")
# listline(fruits)
# print(" ")
# print("end")

# waf to print the factorial of n 
# def factcal(n):
#     fact = 1
#     i = 1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# factcal(int(input("enter n:")))

# waf to convert usd to inr
# def convert(n):
#     print("USD-INR VALUE =",n*94.49)

# usd = int(input("enter usd:"))
# convert(usd)

# wa recursive function to print sum of first n natural numbers
def calcsum(n):
    sum = 0
    print(n)
calcsum(5)