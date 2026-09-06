 # write a function to print length of list. [list is the parameter for function]
cities = ["delhi", "mumbai", "chennai", "kolkata", "dehradun"]

# def len_list(l):
#     print(len(l))
#     return len(l)
# prod = len_list(cities)
# print("length of list:",prod)

# write a function to print elements of list in a single line

# def prilist(lost):
#     for el in lost:
#         print(el, end=" ")
#     return lost

# version doubting
# def prilist(lost):
#     for el in lost:
#         print(el, end=" ")
#     return lost
# newl = prilist(cities)
# print()
# print("it should be other",newl)

# corrected
# cities = ["delhi", "mumbai", "chennai", "kolkata", "dehradun"]

# def prilist(lust):
#     result = ""   # empty string
#     for el in lust:
#         result += el + " "   # add each city with a space
#     return result.strip()    # return the final string

# newl = prilist(cities)
# print("It should be other:", newl)

# waf to print a factorial of a number (number is parameter) number / n
# my proper try
# def calfact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
# result = calfact(int(input("enter n:")))
# print(result)

# my confused try
# def calcfact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
#     return fact
# calcfact(int(input("enter n:")))
# print("the fact of 5:", calcfact(5))

# waf to convert usd to inr
# def concur(n):
#     con = n*94.49
#     print(con)
#     return con
# res = concur(int(input("enter n:")))
# # try 2
# def concur(n):
#     con = n*94.49    
#     return con
# res = concur(int(input("enter n:")))
# print("res",res)


# homework to print even or odd string depending on n and n should be given by user input
# def evenodd(n):
#     if (n % 2 == 0):
#         print("EVEN")
#     else:
#         print("ODD")
# evenodd(int(input("enter n:")))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))