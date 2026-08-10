grade = ("C","B","C","A","C","B","C","C","A","C","D","C")

list = list(grade)
# a tuple data can be copied into a list using list_name = list(tuple_name)
print(grade)
print(type(grade))
print(list)
print(type(list))
print(list.sort())

list.sort()
print("sorted list:\n", list)