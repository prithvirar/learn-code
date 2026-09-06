# def calc(n):
#     if (n==0):
#         return 0
    
#     return calc(n-1) + n
# print(calc(5))

list1 = [12,13,14,15,16]

def prin(n):
    if n==-1:
        return 0
    return prin(n-1)
    for i in range(n):
        print(list1[i])
prin(5)