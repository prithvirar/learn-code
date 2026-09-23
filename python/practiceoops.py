"""create a student class with arguments name,marks and create a method to print average of marks"""
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def avermarks(self):
#         print(f"average marks of {self.name}:", sum(self.marks)/len(self.marks))
    
# s1 = Student("prithvi", [99, 98, 100])
# print(s1.name)
# print(s1.marks)
# s1.avermarks()


"""create class Account 2 attributes:AccNO. & Balance, create methods for debit,credit get balance"""
class Bank:
    def __init__(self, Accn, Baln):
        self.Accn = Accn
        self.Baln = Baln
    def credit(self,cred):
        self.Baln += cred
        print(f"{cred} dollars were credited to Account {self.Accn} ")        
    def debit(self,deb):
            self.Baln -= deb
            print(f"{deb} dollars were debited from Account {self.Accn} ")
    def cbal(self):
         print(f"current balance of {self.Accn} is: ", self.Baln)

cust1 = Bank(8790, 1111111111)
cust2 = Bank(9618, 9999999999)
cust1.credit(123)
cust1.debit(3456)
cust1.credit(9876)
cust1.debit(5000)
cust1.cbal()
