# List Comprehension
"""
Another way of creating a list in Python
Improves readability
We can write it in single line
It is generally faster than a normal for loop
"""

# Input: [10, 20, 30]
# Output: [100, 400, 900] Squares of all elements in a given list

l = [10, 20, 30]
print([x*x for x in l])

# Input: [1, 2, 3, ....10]
# Output: cubes of all even numbers in the list   [8, 64 .... 1000]

l = range(1, 11)
print([x*x*x for x in l if x % 2 == 0])

# Nested list comprehension
print([x*x*x for x in [y for y in l if y%2 == 0]])

print([x*x*x for x in [y for y in [z for z in l if z%2 == 0 and z != 10]]])


# Dictionary comprehension
# Input: {'a': 10, 'b": 20, 'c': 30}
# Outout: {'a': 100, 'b': 400, 'c': 900}

d = {'a': 10, 'b': 20, 'c': 30}
print({k: v*v for k, v in d.items()})

d2 = {k: v*v for k, v in d.items() if k != 'c'}
d2.update({'c': d['c']})
print(d2)


# lambda function

"""
It is a keyword to create and call a function in python
It doesn't have a name for it, so it is called as anonymous functions
You can write it in single line so improves readability of code 
It is meant for simple operations
It will returns a object
lambda <input>: <operation>
"""

# Return square of given value
def my_func(x):
    return x*x

print(my_func(10))

obj = lambda x: x*x
print(obj(10))

obj = lambda x: x*x if x % 2 != 0 else x
print(obj(10))
print(obj(3))

obj = lambda x, y: x*y if x % 2 != 0 else x
print(obj(10, 20))
print(obj(11, 20))

"""
File Management
1. Open a file
2. Read data from file
3. Write data to file
4. Close the file
"""

# Opening file using with statement
# Reading data using read()
with open('../data/csb_data.txt') as f:
    data = f.read()
    print(data)


# Opening file using with statement
# Reading data using readlines()
with open('../data/csb_data.txt') as f:
    lines = f.readlines()
    print(lines)


# Find the count of each word in a file
with open('../data/csb_data.txt') as f:
    lines = f.readlines()
    count_dict = {}
    for item in lines:
        words = item.split()
        for word in words:
            # if word in count_dict:
            #     count_dict[word] = count_dict[word] + 1
            # else:
            #     count_dict[word] = 1

            count_dict[word] = count_dict.get(word, 0) + 1
    print(count_dict)


# Add a line to the existing file
with open('../data/csb_data.txt', 'w') as f:
    f.write('Test with line1')

# Add a line to the existing file
with open('../data/csb_data.txt', 'a') as f:
    f.write('\nTest with line2')

l = [10, 20, 30]
# Add a line to the existing file
with open('../data/csb_data.txt', 'a') as f:
    f.write('\n')
    f.write(str(l))


l = [10, 20, 30]
# Add a line to the existing file
with open('../data/csb_data.txt', 'a') as f:
    import json
    f.write('\n')
    f.write(json.dumps(l))

# Other way to open file
f = open('../data/csb_data.txt')
print(f.read())
f.close()
