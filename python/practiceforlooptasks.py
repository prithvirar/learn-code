# my version to print a list

# listsquare = []
# value = None
# for i in range(1,11):
#     value = i**2
#     listsquare.append(value)
# print(listsquare)
# print("end")

# print values from list using for loop

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in nums:
#     print(i)
# print("end")

# search a number x from given tuple
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# given_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter value for x:"))
# for i in given_tuple:
#     if(i == x):
#         print("found x at index:",given_tuple.index(i))
#         break
#     else:
#         print("searching...found",i)
# print("end")

# simpler version
# given_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter value for x:"))
# val = 0
# for i in given_tuple:
#     if (i == x):
#         print("number x found at index:",val)
#     val += 1
# print("end")

# used linear searching here
# it searches first node checks then goes to another (traversal)

# for i in range(1,101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)


# n = int(input("enter n:"))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# factorial for given n using for
n = int(input("enter n:"))
fact = 1
i = 1
for i in range(1,n+1):
    print("before i",i)
    print("before fact",fact)
    fact *= i
    i += 1
    print("after fact",fact)
    print("after i",i)

print(fact)