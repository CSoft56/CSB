class MySample:
   def __init__(self, my_value):
       self.number = my_value

   def get_number(self):
       return self.number


class AnotherClass:
    def __init__(self, t):
        print('Testtttttt')
        self.t = t


if __name__ == '__main__':
    var = MySample(560560)
    print(var.get_number())

    obj2 = AnotherClass(3000)
    print(obj2.t)