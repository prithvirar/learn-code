val1 = int(input("enter value1: "))
val2 = int(input("enter value2: "))
val3 = int(input("enter value3: "))

if val1 >= val2 and val1 >= val3:
    print("greatest value is: ", val1)
elif val2 >= val1 and val2 >= val3:
    print("greatest value is: ", val2)
else:
    print("greatest value is: ", val3)