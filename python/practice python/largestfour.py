a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = int(input("enter c value: "))
d = int(input("enter d value: "))
# !!!wrong attempt!!!
# if(a < b):
#     if(b < c):
#         if(c < d):
#             print("d is largest")
#         else:
#             print("c is largest")

# if(d < c):
#     if(c < b):
#         if(b < a):
#             print("a is largest")
#         else:
#             print("b is largest")

if((a>b) and (a>c) and (a>d)):
    print("a is greatest value(",a,")")

if((b>a) and (b>c) and (b>d)):
    print("b is greatest value(",b,")")
    
if((c>b) and (c>a) and (c>d)):
    print("c is greatest value(",c,")")
    
if((d>b) and (d>c) and (d>a)):
    print("d is greatest value",(d))