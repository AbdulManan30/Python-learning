# union means it combine both sets values and dublicated value it write only one time like this example below
a = {1,5,3,2,7,8}
b = {2,1,4,5,3,7}
print(a.union(b)) # it will return {1,2,3,4,5,7,8}

# intersection means that write dublicated value only
print(a.intersection(b)) # output will be {1,2,3,5,7}