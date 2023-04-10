"""
Decorators:
- Design Patter
- It can be a function or class
- Helps to modify the functionality of another function in run time
- We can call it using '@' symbol
"""


def check_value(venkat):
    def helper(*args, **kwargs):
        if args[1] != 0:
            return venkat(*args, **kwargs)
        else:
            return "Second arg value can't be zero"

    return helper


@check_value
def my_div(a, b):
    return a/b


if __name__ == '__main__':
    print(my_div(10, 2))
    print(my_div(10, 5))
    print(my_div(10, 3))
    print(my_div(10, 1))
    print(my_div(10, 0))
