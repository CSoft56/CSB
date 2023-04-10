"""
1.classes
2.Inheritance
"""
class Account:
    x=100

    def add_account(self):
        pass

    def add_account(self):
        pass

obj= Account()
obj2= Account()
print(obj.x)
print(obj2.x)

obj.x =200
print(obj.x)
print(obj2.x)

obj.x = 300

obj3=Account()
print(obj.x)
print(obj2.x)
print(obj3.x)






class Mysample(object):

    def _init_(self, my_value=None):
        self.x = my_value

    def get_x(self):
        return self.x


if __name__ == '__main__':
    var = Mysample(10)
    print(var.get_number())
