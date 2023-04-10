"""
Decorators
design pattern
it can be a function or class
helps to modify the functionality to another function in run time
we can call it using '@' symbol
"""

def check_value(Mahitha):
    def helper(*args, **kwargs):
        if args[1] !=0:
            return Mahitha(*args, **kwargs)
        else:
            return"second value cannot be zero"
    return helper

@check_value
def my_div(a,b):
    return a/b


if __name__ =='__main__':
    print(my_div(20,2))
    print(my_div(20, 5))
    print(my_div(20, 3))
    print(my_div(20, 1))
    print(my_div(20, 0))