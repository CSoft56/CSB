"""
1.classes
2.Inheritance
"""
class Account:
    x=1000

    def add_account(self):
        pass

    def add_account(self):
        pass

obj= Account()
obj2= Account()
print(obj.x)
print(obj2.x)

obj.x =500
print(obj.x)
print(obj2.x)

obj.x = 800

obj3=Account()
print(obj.x)
print(obj2.x)
print(obj3.x)






class mysample(object):

    def __init__(self, my_value=None):
        self.x = my_value

    def get_number(self):
        return self.x


if __name__ == '_main_':
    var = mysample(30)
    print(var.get_number())










