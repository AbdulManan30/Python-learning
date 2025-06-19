# Tuple is a immutable container where we store many values like String, int etc 
a = (1,2,2,3,4,'Manan', 73.5, False)
# a[3] = "Kuki" # It can not change because it is immutable
# print(a)

# Some tuple methods
print(a.count(2)) # it will give us the total count of element present in a tuple
print(a.index(73.5)) # it will give us the index of 73.5 in the tuple

print(2 in a) # it check that 2 is present in a tuple or not

print(a * 2) # it will multiple the tuple by 2 

b = (1,2,3,4,5,6,7,8,4345)

print(min(b)) # it will give us the smallet value present in a tuple
print(max(b)) # it will give us the longest value present in a tuple