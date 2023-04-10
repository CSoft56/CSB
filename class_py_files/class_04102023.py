"""
Exception Handling
- Any error that occures at run time
- Keywords:
    - try
    - except
    - finally
    - else
    - raise
- Exception is base class for all Exceptions
"""

def my_div(a, b):
    try:
        res = a/b
        l = ['a', 'b', 'c']
        print(l[0])
        print(l['abc'])
    # except (ZeroDivisionError, IndexError) as e:
    #     res = "Please enter non zero values for b or index out of range"
    #     print(e)

    except Exception as ef:
        res = "UnKnown exception"
        print(ef)

    return res

print(my_div(10, 2))

