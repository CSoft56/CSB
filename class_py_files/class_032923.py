"""
1. Classes
2. Inheritance
"""

class Account:
    x = 100

    def add_account(self):
        print(self.x)

    def delete_account(self):
        pass

    def list_accounts(self):
        pass


obj = Account()
obj2 = Account()

print(obj.x)
print(obj2.x)

obj.x = 200
print(obj.x)
print(obj2.x)

obj2.x = 300

obj3 = Account()
print(obj.x)
print(obj2.x)
print(obj3.x)


"""
Constructor/Inititalizer in Python 
"""

class MySample:
   def __init__(self, my_value):
       self.number = my_value

   def get_number(self):
       return self.number


if __name__ == '__main__':
    var = MySample(560560)
    print(var.get_number())