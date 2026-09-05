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
given_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter value for x:"))
val = 0
for i in given_tuple:
    if (i == x):
        print("number x found at index:",val)
    val += 1
print("end")