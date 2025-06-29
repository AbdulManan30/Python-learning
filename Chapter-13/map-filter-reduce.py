# Map function
"""
les = [1, 2, 3, 4, 5, 6]


def result(x):
    return x * x


y = map(result, les)
for i in y:
    print(i)

"""
# Filter
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x % 2 == 0
even = filter(is_even, l)
print(list(even))

"""

# Reduce
"""
from functools import reduce

l = [1, 2, 3, 4, 5]


def sum(a, b):
    return a + b


res = reduce(sum, l)
print(res)
"""
