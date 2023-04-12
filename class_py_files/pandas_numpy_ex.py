"""
Pandas and Numpy
"""

import numpy as np
import pandas as pd

# Creating a new numpy array
l = [10, 20, 30, 40]

a = np.array(l)

print(a)

l2 = [[1, 2, 3], [4, 5, 6]]

b = np.array(l2)

print(b)


data = [
    ['John Smith','123 Main St', 34],
    ['Jane Doe', '456 Maple Ave', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ]
columns = ['name', 'address', 'age']

df = pd.DataFrame(data=data, columns=columns)

print(df)


class MyException(Exception):
    pass


# raise MyException('It is custom exception')


df2 = pd.read_csv('sampl.csv')
