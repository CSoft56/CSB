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
     def get_x(self):
        return self.x


s1 = Mysample(10)
print(s1.get_x())