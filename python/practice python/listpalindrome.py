list = []
list.append(int(input("enter your value:")))
list.append(int(input("enter your value:")))
list.append(int(input("enter your value:")))
list.append(int(input("enter your value:")))
list.append(int(input("enter your value:")))
# you can also check for characters but for now only trying for int values...
newlist = []
newlist = list.copy()
newlist.reverse()
# print(f"{list} \n ,{newlist}")

if(list == newlist):
    print("given list is a palindrome...")
else:
    print("given list is a not palindrome...")
