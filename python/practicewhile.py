# print numbers 1 to 100
# value = 1
# while value <= 100:
#     print(value)
#     value += 1
# print("program ended")

# print numbers 100 to 1
# value = 100
# while value >= 1:
#     print(value)
#     value -= 1
# print("program ended")

# print multiplication table for a given input n
# n = int(input("enter the multiple:"))
# while n<=10:
#     print(f"{n} x 1 =", n*1)
#     print(f"{n} x 2 =", n*2)
#     print(f"{n} x 3 =", n*3)
#     print(f"{n} x 4 =", n*4)
#     print(f"{n} x 5 =", n*5)
#     print(f"{n} x 6 =", n*6)
#     print(f"{n} x 7 =", n*7)
#     print(f"{n} x 8 =", n*8)
#     print(f"{n} x 9 =", n*9)
#     print(f"{n} x 10 =", n*10)
#     break
# print("the multiple table")

# version 2 for multiple short and simple 
# n = int(input("enter the multiple:"))
# i = 1
# while i<=10:
#     print(n,"x",i,"=",n*i)
#     i+=1
# print("the multiples of n until 10")

# print the elements of the following list
# [1,4,9,16,25,36,49,64,81,100]
# until = 1
# while until <= 10:
#     print(until**2)
#     until += 1
# print("program ended")

# print the elements of the following in a list
# [1,4,9,16,25,36,49,64,81,100]
# until = 1
# temp = None
# listsquare = []
# while until <= 10:
#     temp = until**2
#     until += 1
#     listsquare.append(temp)
# print(listsquare)
# print("program ended")


# print the elements of the following list using while
# [1,4,9,16,25,36,49,64,81,100]

# given_list = [1,4,9,16,25,36,49,64,81,100]
# print(len(given_list))
# n = len(given_list)-1
# i = 0
# while i <= n:
#     print(given_list[i])
#     i += 1
# print("end")    

# print the elements of the following list using while 
# traverse = visiting each item in a data structure
# ["ironman","thor","superman","batman"]
# hero = ["ironman","thor","superman","batman"]
# idx = 0
# while idx < len(hero):
#     print(hero[idx])
#     idx +=1

# search for a number x in the following tuple
# (1,4,9,16,25,36,49,64,81,100)
# given_tuple = (1,4,9,16,25,36,49,64,81,100)
# print("given tuple is :",given_tuple)
# print("select x within given tuple")
# x = int(input("enter x to find:"))
# i = 0
# while i < len(given_tuple):
#     if(given_tuple[i] == x):
#         print("x found at index:",i)
#     i += 1
# print("end")


n = int(input("enter n:"))
sum = 0
i = 1
while i <= n:
    print(i)
    print("sum before ", sum)
    sum += i
    print('SUM',sum)

    i +=1
print(sum)